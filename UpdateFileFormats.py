import os
import pybel
import pdb
import collections

def heading(text, symbol):
    return text + "\n" + symbol*len(text)

compchem = ("Computational chemistry", ['POSCAR', 'tmol', 't41', 'tmol', 'zin', 'moo', 'mop',
            'mopcrt', 'mopin', 'mopout', 'mp', 'mpc', 'nw', 'nwo',
            'outmol',
            'adf', 'adfout', 'com', 'g03', 'g09', 'g92', 'g98', 'gal',
            'cub', 'cube', 'dmol'])
viewers = ("3D viewers", ['mold', 'molden', 'yob'])
common_cheminf = ("Most common cheminformatics", ['pdb', 'smi', 'can', 'smiles',
                 'inchi', 'mol2', 'mol', 'cml'])

allformats = set(pybel.informats.keys()) | set(pybel.outformats.keys())
sections = [common_cheminf, compchem, viewers]

exts = collections.defaultdict(list)
for format in allformats:
    try:
        formatname = pybel.informats[format]
    except KeyError:
        formatname = pybel.outformats[format]
    exts[formatname].append(format)

indexfile = open(os.path.join("FileFormats", "Overview.rst"), "w")
print >> indexfile, heading("Supported File Formats and Options", "=")
print >> indexfile, "\n.. toctree::\n   :maxdepth: 2\n"

seen = set()
for name, codes in sections:
    print >> indexfile, "   %s.rst" % name.replace(" ", "_")
    sectionfile = open(os.path.join("FileFormats", "%s.rst" % name.replace(" ", "_")), "w")
    print >> sectionfile, heading(name, "~")
    print >> sectionfile, "\n.. toctree::\n"

    names = set()
    for code in codes:
        try:
            formatname = pybel.informats[code]
        except KeyError:
            formatname = pybel.outformats[code]
        names.add(formatname)
    names = sorted(list(names))
        
    for formatname in names:

        format = pybel.ob.OBFormat.FindType(exts[formatname][0])
        desc = format.Description()
        print desc
        safename = formatname.replace(" ", "_").replace("/", "_or_")
        print >> sectionfile, "   %s.rst" % safename
        
        output = open(os.path.join("FileFormats", "%s.rst" % safename), "w")

        title = "%s (%s)" % (formatname, ", ".join(exts[formatname]))
        print >> output, heading(title, "=")

        INTRO, WRITE, READ = range(3)
        data = [[] for i in range(3)]
        N = INTRO
        for line in desc.splitlines():
            if line.lower().strip().startswith("write options"):
                N = WRITE
            elif line.lower().strip().startswith("read options"):
                N = READ
            data[N].append(line)

        print >> output, "\n%s\n" % " ".join(data[0])

        for x, y in ((READ, "Read"), (WRITE, "Write")):
            if len("".join(data[x][1:]).strip()) > 0:
                print >> output, heading("%s Options" % y, "~")
                for d in data[x][1:]:
                    if d.strip():
                        d = d.strip()
                        broken = d.split()
                        print >> output, "**%s**" % broken[0]
                        print >> output, "    " + " ".join(broken[1:])
                        print "    " + " ".join(broken[1:])
       
        output.close()
    sectionfile.close()
indexfile.close()
