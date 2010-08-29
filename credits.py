names = []
for line in open("THANKS", "r"):
    if line.startswith("</li><li>") or line.startswith("<ul><li>"):
        temp = line[line.index("<li>") + 5:].strip()
        if temp.startswith("<a href"):
            idx = temp.find("nofollow")
            temp = temp[idx+10:-4]
        names.append(temp)

output = open("credits.rst", "w")
print >> output, "Credits\n=======\n"
print >> output, ".. hlist::\n   :columns: 3\n"
for name in names:
    print >> output, "   - %s" % name
output.close()

        
