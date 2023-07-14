names = []
for line in open("THANKS", "r"):
    if line.startswith("</li><li>") or line.startswith("<ul><li>"):
        temp = line[line.index("<li>") + 5:].strip()
        if temp.startswith("<a href"):
            idx = temp.find("nofollow")
            temp = temp[idx+10:-4]
        names.append(temp)

output = open("credits.rst", "w")
print("Credits\n=======\n", file=output)
print(".. hlist::\n   :columns: 3\n", file=output)
for name in names:
    print(f"   - {name}", file=output)
output.close()

        
