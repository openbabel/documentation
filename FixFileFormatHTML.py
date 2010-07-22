import os
import glob

for filename in glob.glob(os.path.join("_build", "html", "FileFormats", "*.html")):
    print filename
    with open(filename, "r") as input:
        text = input.readlines()
    with open(filename, "w") as output:
        for line in text:
            if line.startswith("<kbd><span class=\"option\">"):
                output.write("<kbd><span class=\"option\">" + line[27:])
            else:
                output.write(line)
    
