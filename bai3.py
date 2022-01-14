ten = str(input("Nhap ho ten: "))
n = int(input("Nhap so ki tu co trong moi tu trong ten vao: "))
print("Ten cua ban:", ten)
str1 = str(n)
str2 = str1[::-1]

if str1 == str2:
    print("day la so thuan nghich")
else:
    print("day khong la so thuan nghich")
