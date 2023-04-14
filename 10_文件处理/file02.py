#测试写入中文
f = open(r"b.txt","w",encoding="utf-8")
#f = open(r"b.txt","w")
f.write("乒乒科技\n乒乒人\n")
f.close()