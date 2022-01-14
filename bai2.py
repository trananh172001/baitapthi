tendem = str(input("Nhap ten dem: "))
n = int(input("Nhap so ki tu cua moi chu cai trong ten dem vao: "))

def Tongsokitu(n):
    s = 0
    while n > 0:
        s = s + n % 10
        n = int(n / 10)
    return s

print("Tổng các chữ số của", n, "là", Tongsokitu(n))