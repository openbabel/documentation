import os
import sys

if os.path.isfile("pybel.py") or os.path.isfile("pybel.pyc"):
    sys.exit("Delete pybel.pyc and move pybel.py to oldpybel.py")

from openbabel import pybel

def heading(text, symbol):
    return text + "\n" + symbol*len(text)

def escape(text):
    return text.replace("*", "\*")

# descriptors
numerical = ["atoms", "bonds", "HBD", "HBA1", "HBA2", "nF", "logP",
        "MW", "tbonds", "MR", "abonds", "sbonds", "dbonds", "TPSA",
        "rotors", "MP"]
textual = ["cansmi", "cansmiNS", "InChI", "InChIKey", "formula", "title"]
filters = ["L5", "smarts", "s"]
all = numerical + textual + filters

unclassified = [desc for desc in pybel.descs if desc not in all]
if unclassified:
    print "UNCLASSIFIED: ", unclassified

desc_sections = [("Numerical descriptors", numerical),
                 ("Textual descriptors", textual),
                 ("Descriptors for filtering", filters)]

text = []
for section, descs in desc_sections:
    text.append(heading(section, "-"))
    text.append("")
    for desc in descs:
        description = pybel._descdict[desc].Description()
        broken = [x.lstrip() for x in description.split("\n")]
        firstline = broken[0]
        maindescription = "\n".join(broken[1:-1]) if broken[-1].endswith("is definable") else "\n".join(broken[1:])

        title = "%s (%s)" % (firstline, desc)
        text.append(".. rubric:: %s" % title)
        text.append("")
        text.append("%s" % escape(maindescription))
        text.append("")

contents = open(os.path.join("Descriptors", "descriptors.rst"), "r").read()
marker = "INSERT AUTOMATICALLY GENERATED CONTENT BELOW"
idx = contents.find(marker) + len(marker)

new_contents = contents[:idx] + "\n\n" + "\n".join(text)
print >> open(os.path.join("Descriptors", "descriptors.rst"), "w"), new_contents

