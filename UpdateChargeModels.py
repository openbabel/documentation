import os
import sys

if os.path.isfile("pybel.py") or os.path.isfile("pybel.pyc"):
    sys.exit("Delete pybel.pyc and move pybel.py to oldpybel.py")

from openbabel import pybel

def heading(text, symbol):
    return text + "\n" + symbol*len(text)

def escape(text):
    return text.replace("*", "\*")

chargenames = pybel._getpluginnames("charges")
charge_dict = pybel._getplugins(pybel.ob.OBChargeModel.FindType, chargenames)

normal = ["gasteiger", "mmff94"]
different = ["eem", "qeq", "qtpie"]
none = ["none"]
all = none + normal + different

unclassified = [charge for charge in chargenames if charge not in all]
if unclassified:
    print "UNCLASSIFIED: ", unclassified

charge_sections = [("Cheminformatics charge models", normal),
                   ("Special charge models", different)]

text = []
for section, charges in charge_sections:
    text.append(heading(section, "-"))
    text.append("")
    for charge in charges:
        description = charge_dict[charge].Description()
        broken = [x.lstrip() for x in description.split("\n")]
        firstline = broken[0]
        maindescription = "\n".join(broken[1:-1]) if broken[-1].endswith("is definable") else "\n".join(broken[1:])

        title = "%s (%s)" % (firstline, charge)
        text.append(".. rubric:: %s" % title)
        text.append("")
        text.append("%s" % escape(maindescription))
        text.append("")

contents = open(os.path.join("Charges", "charges.rst"), "r").read()
marker = "INSERT AUTOMATICALLY GENERATED CONTENT BELOW"
idx = contents.find(marker) + len(marker)

new_contents = contents[:idx] + "\n\n" + "\n".join(text)
print >> open(os.path.join("Charges", "charges.rst"), "w"), new_contents

