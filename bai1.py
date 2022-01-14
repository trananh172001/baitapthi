ten = str(input("Nhap ten: "))
n = int(input("so ki tu trong ten:"))
print(ten)
khoangcach = ""
for i in range(1, n+1):
    khoangcach = khoangcach + "{" +  str(i) + ":" + str(i*i) + "}" + ","
print(khoangcach)