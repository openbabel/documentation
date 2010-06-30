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
            'cub', 'cube', 'dmol', 'fch', 'fck', 'fh',
            'qcin', 'qcout'])
viewers = ("3D viewers", ['mold', 'molden', 'yob', 'vmol'])
common_cheminf = ("Common cheminformatics", ['pdb', 'smi', 'can', 'smiles',
                 'inchi', 'mol2', 'mol', 'cml'])
cheminf = ("Other cheminformatics", ['fix', 'msi', 'mpd', 
                                     'cdxml', 'cdx'])
crystal = ("Crystallography", ["cif", "acr", "ins", "mcif",
                               "fract", "cssr"])
images = ("Images", ['png', 'svg', 'pov'])
utility = ("Utility", ['report', 'copy', 'molreport', 'text', 'txt',
                       'nul', 'xyz', 'xml', "mna", "fpt", "fs"])
molecular_dynamics = ('Molecular dynamics',
                      ['gr96', 'txyz', "prep"])
reactions = ("Reactions", ["cmlr"])
# 'test' format does not appear to exist (although it's on the wiki)
# Para break in final comments don't appear
# cml format has a lot of text on wiki
# Also fastsearch

allformats = set(pybel.informats.keys()) | set(pybel.outformats.keys())
sections = [common_cheminf, utility, cheminf, compchem, crystal, reactions, images, viewers,
            molecular_dynamics]
##sections = [images]

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
        print "++++++++++++++++++++++++"
        safename = formatname.replace(" ", "_").replace("/", "_or_")
        print >> sectionfile, "   %s.rst" % safename
        
        output = open(os.path.join("FileFormats", "%s.rst" % safename), "w")

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
            elif emptyline == True and N != INTRO:
                N = COMMENTS
##            print "Line", N, line                
            data[N].append(line)
            emptyline = line.strip()==""
            if N==INTRO and emptyline:
                data[N].append("\n\n")
        if data[INTRO]:
            print >> output, "\n**%s**\n" % data[INTRO][0]
            if len(data[INTRO]) > 1:        
                print >> output, "%s\n" % " ".join(data[INTRO][1:])

        for x, y in ((READ, "Read"), (WRITE, "Write")):
            firstline = True
            if len("".join(data[x][1:]).strip()) > 0:
                print >> output, heading("%s Options" % y, "~")
                for d in data[x][1:]:
                    if d.strip():
                        if d.startswith("   "):
                            if firstline:
                                print >> output, "\n.. note::\n"
##                                print >> output, "::\n"
                            print >> output, d
                            firstline = False
                            continue
                        else:
                            firstline = True
                    
                        d = d.strip()
                        broken = d.split()
                        start = 1
                        if broken[1][0] in ["<", '"']:
                            while broken[start - 1][-1] not in [">", '"']:
                                broken[0] += " " + broken[start]
                                start += 1
##                        print >> output, "**%s**" % broken[0]
##                        print >> output, "    " + " ".join(broken[start:])
                        print >> output, "\n.. cmdoption:: %s\n" % broken[0]
                        print >> output, "  " + " ".join(broken[start:])
##                        print "    " + " ".join(broken[start:])
        if data[COMMENTS]:
            print >> output, heading("Comments", "~")
            print >> output, "\n%s\n" % " ".join(data[COMMENTS])
       
        output.close()
    sectionfile.close()
indexfile.close()
