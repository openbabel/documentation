import os
import pybel
import pdb
import collections

def heading(text, symbol):
    return text + "\n" + symbol*len(text)

compchem = ("Computational chemistry", ['POSCAR', 'tmol', 't41', 'tmol', 'zin', 'moo', 'mop',
            'mopcrt', 'mopin', 'mopout', 'mp', 'mpc', 'nw', 'nwo',
            'outmol', 'mpqc', 'mpqcin', 'CONTCAR', 'pqs', 'hin',
            'adf', 'adfout', 'com', 'g03', 'g09', 'g92', 'g98', 'gal',
            'dmol', 'fch', 'fck', 'fh',
            'qcin', 'qcout', 'gamin', 'gamout', 'jin', 'jout'])
viewers = ("3D viewers", ['mold', 'molden', 'yob', 'vmol', 'gpr', 'pcm',
                          "unixyz"])
common_cheminf = ("Common cheminformatics", ['pdb', 'smi', 'can', 'smiles',
                 'inchi', 'mol2', 'mol', 'cml'])
cheminf = ("Other cheminformatics", ['msi', 'mpd', 'pc', 
                                     'cdxml', 'cdx', 'mcdl'])
crystal = ("Crystallography", ["cif", "acr", "ins", "mcif",
                               "fract", "cssr"])
images = ("Images", ['png', 'svg', 'pov'])
volume_data = ("Volume data", ["cube", "dx"])
utility = ("Utility", ['report', 'copy', 'molreport', 'text', 'txt',
                       'nul', 'xyz', 'xml', "mna", "fpt", "fs",
                       "mpd"])
molecular_dynamics = ('Molecular dynamics',
                      ['gr96', 'txyz', "prep", "mmod"])
thermo = ('Kinetics and Thermodynamics', ["ck", "therm"])
reactions = ("Reactions", ["cmlr", "rxn", "rsmi"])
biology = ("Biological data", ["fasta"])
misc = ("Miscellaneous", ["msms"])
unknown = ("I have no idea what this is", ["feat", "fix", "xed"])
# 'test' format does not appear to exist (although it's on the wiki)
# fastsearch, cml format - added some markup
# (fastsearch missing s option)
# gamessuk not on Windows, gukin, gukout
# inchi refs inchi docs
# mcdl refs paper
# cml refs papers
# mna refs paper
# see also between mol report and report
# see also between cml reaction and mdl rxn
# smiles format link to radical extension
# xml contains ref to two other formats

allformats = set(pybel.informats.keys()) | set(pybel.outformats.keys())
sections = [common_cheminf, utility, cheminf, compchem, crystal, reactions,
            images, viewers, thermo,
            molecular_dynamics, volume_data, misc, biology, unknown]
##sections = [utility]

exts = collections.defaultdict(list)
for format in allformats:
    try:
        formatname = pybel.informats[format]
    except KeyError:
        formatname = pybel.outformats[format]
    exts[formatname].append(format)

indexfile = open(os.path.join("FileFormats", "Overview.rst"), "w")
print >> indexfile, open(os.path.join("FileFormats", "Overview.txt"), "r").read()
##print >> indexfile, heading("Supported File Formats and Options", "=")
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
       
        safename = formatname.replace(" ", "_").replace("/", "_or_")
        print >> sectionfile, "   %s.rst" % safename
        
        output = open(os.path.join("FileFormats", "%s.rst" % safename), "w")
        ref = ".. _%s:\n" % safename
        print >> output, ref
        title = "%s (%s)" % (formatname, ", ".join(exts[formatname]))
        print >> output, heading(title, "=")

        INTRO, WRITE, READ, COMMENTS = range(4)
        data = [[] for i in range(4)]
        N = INTRO
        emptyline = False
        for line in desc.splitlines()[1:]:
            if line.lower().strip().startswith("write options"):
                N = WRITE
                options = True
            elif line.lower().strip().startswith("read options"):
                N = READ
                options = True
            elif N != INTRO and line and line[0]!=" ":
                N = COMMENTS
##            print "Line", N, line                
            data[N].append(line)
            emptyline = line.strip()==""
##            if N==INTRO and emptyline:
##                data[N].append("\n\n")
        if data[INTRO]:
            print >> output, "\n**%s**\n" % data[INTRO][0]
            if len(data[INTRO]) > 1:
                for line in data[INTRO][1:]:
                    print >> output, line.rstrip()
                print >> output, "\n"
##                print >> output, "%s\n" % "\n".join(data[INTRO][1:])

        for x, y in ((READ, "Read"), (WRITE, "Write")):
            firstline = True
            if len("".join(data[x][1:]).strip()) > 0:
                print >> output, heading("%s Options" % y, "~"), "\n"
                for d in data[x][1:]:
##                    if d.strip():
                    if d.startswith("   ") or not d.strip():
                        if firstline:
                            print >> output, ""

                        print >> output, d
                        firstline = False
                        continue
                    else:
                        firstline = True
                
                    d = d.strip()
                    d = d.replace("#", "<num>")
                    broken = d.split()
                    if len(broken[0]) > 1: # Param stuck to option
                        broken = [d[0], broken[0][1:]] + broken[1:]
                    start = 1                        

                    if broken[1][0] in ["<", '"']:
                        
                        broken[1] = "<" + broken[1][1:]
            
                        while True:
                            broken[0] += " " + broken[start]
                            if broken[start][-1] in [">", '"']:
                                break
                            start += 1
                        start += 1
                        
                        broken[0] = broken[0][:-1] + ">"

                    print >> output, "-%s  *%s*" % (broken[0], " ".join(broken[start:]))
                    print  "-%s  %s" % (broken[0], " ".join(broken[start:]))

        if data[COMMENTS]:
            print >> output, heading("Comments", "~")
            for line in data[COMMENTS]:
                print >> output, line.rstrip()
##            print >> output, "\n%s\n" % " ".join(data[COMMENTS])
       
        output.close()
    sectionfile.close()
indexfile.close()
