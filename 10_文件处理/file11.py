# 测试CSV文件的读取和写入
import csv

with open("ee.csv", "w") as f:
    b_csv = csv.writer(f)
    b_csv.writerow(["ID", "姓名", "年龄"])
    b_csv.writerow(["1001", "高淇", "18"])

    c = [["1002", "希希", "3"], ["1003", "东东", "4"]]
    b_csv.writerows(c)

with open("dd.csv", "r") as f:
    a_csv = csv.reader(f)
    print(type(a_csv))
    l = list(a_csv)
    print(type(a_csv))
    print(type(l))
    print("list", l)
    for row in a_csv:
        print("row", row)
