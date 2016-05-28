import os
import sys

if os.path.isfile("pybel.py") or os.path.isfile("pybel.pyc"):
    sys.exit("Delete pybel.pyc and move pybel.py to oldpybel.py")

import pybel
import pdb
import collections

def heading(text, symbol):
    return text + "\n" + symbol*len(text)


compchem = ("Computational chemistry", ['POSCAR', 'tmol', 'tmol', 'zin', 'moo', 'mop',
            'mopcrt', 'mopin', 'mopout', 'mp', 'mpo', 'mpc', 'nw', 'nwo',
            'outmol', 'mpqc', 'mpqcin', 'CONTCAR', 'pqs', 'hin',
            'adf', 'adfout', 'com', 'g03', 'g09', 'g92', 'g98', 'gal',
            'dmol', 'fch', 'fck', 'fh', "gzmat", "caccrt", "cacint",
            'qcin', 'qcout', 'gamin', 'gamout', 'jin', 'jout',
            'fhiaims', 'got', 'pwscf' ,'gukin', 'gukout', 'cache',
            'castep', "abinit", "c09out", "acesin", "acesout",
            'orca', 'orcainp', 'dallog', 'dalmol', 'exyz', 'aoforce'])
viewers = ("3D viewer", ['mold', 'molden', 'yob', 'vmol', 'gpr', 'pcm',
                          "unixyz", "c3d1", "c3d2", "bs", "crk3d",
                          "xsf"])
common_cheminf = ("Common cheminformatics", ['pdb', 'smi', 'can', 'smiles',
                 'inchi', 'inchikey', 'mol2', 'mol', 'cml', 'smy'])
cheminf = ("Other cheminformatics", ['msi', 'pc', "bgf",
                                     'mcdl', "car", "csr"])
crystal = ("Crystallography", ["cif", "acr", "ins", "mcif",
                               "fract", "cssr", "pos"])
twoD_drawing = ("2D drawing", ["ct", "cdxml", "cdx", "ct", "crk2d", "cht"])
images = ("Image", ['png', 'svg', 'pov', "ascii", 'paint'])
volume_data = ("Volume data", ["cube", "dx", 't41', 'pointcloud', 'stl'])
json = ("JSON", ["cdjson", "pcjson"])
utility = ("Utility", ['report', 'copy', 'molreport', 'text', 'txt',
                       'nul', 'xyz', 'xml', "mna", "dat",
                       "mpd", "k", "confabreport"])
fingerprint = ("Molecular fingerprints", ["fpt", "fs", "fps"])
md_and_dock = ('Molecular dynamics and docking',
                      ['gr96', 'txyz', "prep", "mmod", "box", "xtc",
                       "gro", "pdbqt", "CONFIG", "HISTORY", "txyz",
                       "lmpdat", "siesta", "lpmd", "MDFF"])
thermo = ('Kinetics and Thermodynamics', ["ck", "therm"])
reactions = ("Reaction", ["cmlr", "rxn", "rsmi"])
biology = ("Biological data", ["fasta", "pqr"])
misc = ("Miscellaneous", ["msms"])
unknown = ("Obscure", ["feat", "fix", "xed", "alc",
                                           "ccc"])
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
exts = collections.defaultdict(list)
in_exts = set()
out_exts = set()
for format in allformats:
    if format in pybel.informats:
        formatname = pybel.informats[format]
        in_exts.add(formatname)
    if format in pybel.outformats:
        formatname = pybel.outformats[format]
        out_exts.add(formatname)
    exts[formatname].append(format)

sections = [common_cheminf, utility, cheminf, compchem, fingerprint, crystal, reactions,
            images, twoD_drawing, viewers, thermo,
            md_and_dock, volume_data, json, misc, biology, unknown]
classified = set()
for x in sections:
    for y in x[1]:
        for z in exts.values():
            if y in z:
                classified.update(z)
unclassified = [x for x in allformats if x not in classified]
if unclassified:
    sections.append(["Unclassified", unclassified])
    
indexfile = open(os.path.join("FileFormats", "Overview.rst"), "w")
overview = open(os.path.join("FileFormats", "Overview.txt"), "r").read()
print >> indexfile, overview.replace(
    "X formats", "%d formats" % len(exts)).replace(
    "Y formats", "%d formats" % len(in_exts)).replace(
    "Z formats", "%d formats" % len(out_exts))
##print >> indexfile, heading("Supported File Formats and Options", "=")
print >> indexfile, "\n.. toctree::\n   :maxdepth: 2\n"

seen = set()
for name, codes in sections:
    print >> indexfile, "   %s_Formats.rst" % name.replace(" ", "_")
    sectionfile = open(os.path.join("FileFormats", "%s_Formats.rst" % name.replace(" ", "_")), "w")

    sectionref = ".. _%s:\n" % name
    print >> sectionfile, sectionref

    print >> sectionfile, heading(name + " formats", "~")
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
        print formatname

        format = pybel.ob.OBFormat.FindType(exts[formatname][0])
        desc = format.Description()
       
        safename = formatname.replace(" ", "_").replace("/", "_or_")
        print >> sectionfile, "   %s.rst" % safename
        
        output = open(os.path.join("FileFormats", "%s.rst" % safename), "w")
        ref = ".. _%s:\n" % safename
        print >> output, ref
        title = "%s (%s)" % (formatname, ", ".join(exts[formatname]))
        print >> output, heading(title, "=")

        flags = []
#define NOTREADABLE     0x01
#define READONEONLY     0x02
#define READBINARY      0x04
#define ZEROATOMSOK     0x08
#define NOTWRITABLE     0x10
#define WRITEONEONLY    0x20
#define WRITEBINARY     0x40
#define READXML         0x80
#define DEFAULTFORMAT   0x4000        
        if format.Flags() & pybel.ob.NOTWRITABLE:
            flags.append("This is a read-only format.")   
        if format.Flags() & pybel.ob.NOTREADABLE:
            flags.append("This is a write-only format.")
##        print flags
        
        # Read in the parts of the description
        INTRO, WRITE, READ, COMMENTS = range(4)
        symbols = {READ: "a", WRITE: "x"}
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
            data[N].append(line)
            emptyline = line.strip()==""

        # Check for problems with the GUI

        for section in [READ, WRITE]:
            emptyline = problem = False
            for line in data[section]:
                if line == "":
                    emptyline = True
                elif emptyline:
                    problem = True
                    break
            if problem:
                print "    **** This format will have problems with the GUI ****"

        # Handle the parts of the description
        if data[INTRO]:
            if data[INTRO][0].replace("No comments yet", "").strip():
                print >> output, "\n**%s**\n" % data[INTRO][0].strip()
            
            if len(data[INTRO]) > 1:
                for line in data[INTRO][1:]:
                    print >> output, line.rstrip()
                print >> output, "\n"

        if len(flags) > 0:
            print >> output, ".. note:: " + " ".join(flags) + "\n"

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
                    if False:
                        print  "-%s  %s" % (broken[0], " ".join(broken[start:]))

        if data[COMMENTS]:
            print >> output, heading("Comments", "~")
            for line in data[COMMENTS]:
                print >> output, line.rstrip()
       
        output.close()
    sectionfile.close()
indexfile.close()
