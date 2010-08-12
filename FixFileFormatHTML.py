import os
import glob

################
# File formats #
################

for filename in glob.glob(os.path.join("_build", "html", "FileFormats", "*.html")):
    input = open(filename, "r")
    text = input.readlines()
    output = open(filename, "w")
    for line in text:
        if line.startswith("<kbd><span class=\"option\">-"):
            output.write("<kbd><span class=\"option\">" + line[27:])
        else:
            output.write(line)

# Fix LaTeX
filename = os.path.join("_build", "latex", "OpenBabel.tex")
startfixing = False
if os.path.isfile(filename):
    input = open(filename, "r")
    text = input.readlines()
    output = open(filename, "w")
    for line in text:
        if line.startswith("\chapter{Supported File Formats and Options}"):
            startfixing = True
        if startfixing and line.startswith("\item [-"):
            output.write("\item [" + line[8:])
        else:
            output.write(line)

#################
# ---errorlevel #
#################

def fix(filename, before, after):
    inputfile = filename
    fixed = False
    if os.path.isfile(inputfile):
        input = open(inputfile, "r")
        text = input.readlines()
        input.close()
        output = open(inputfile, "w")
        for line in text:
            if line.startswith(before):
                output.write(after + line[len(before):])
                fixed = True
            else:
                output.write(line)
    return fixed

fix(os.path.join("_build", "html", "Command-line_tools", "babel.html"),
    "<kbd><span class=\"option\">--errorlevel",
    "<kbd><span class=\"option\">---errorlevel")
fix(os.path.join("_build", "latex", "OpenBabel.tex"),
    "\item [-{-}errorlevel",
    "\item [-{-}{-}errorlevel")
           
print "Fixed HTML and LaTeX"
