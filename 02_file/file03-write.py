f = open(r"bb.txt","w",encoding="utf-8")
s = ["高老大\n","高老三\n","高老四\n"]
f.writelines(s)
f.close()