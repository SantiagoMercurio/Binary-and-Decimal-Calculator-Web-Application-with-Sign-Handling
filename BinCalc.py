signo = input("Will your numbers have a sign? (Y/N) ")
dec1 = input("Enter your first decimal number: ")
dec1 = int(dec1)
dec2 = input("Enter your second decimal number: ")
dec2 = int(dec2)

# Functions to convert Decimal to Binary and vice versa

def Decimal_Binario(Num):
    List = []
    while Num > 0:
        Res = Num % 2
        List.insert(0, Res)
        Num = Num // 2
    Numstr = ""
    for i in List:
        Numstr = Numstr + str(i)
    return Numstr

def Binario_Decimal(Num):
    dec = 0
    i = 0
    while Num > 0:
        Residue = Num % 10
        exp = Residue * (2 ** i)
        dec += exp
        Num //= 10
        i += 1
    return dec

# Binary to one's complement

def bin_c1(Num):
    Num = Num[::-1]
    Num = list(Num)
    for i in range(len(Num)):
        if Num[i] == "1":
            Num[i] = "0"
        elif Num[i] == "0":
            Num[i] = "1"
        temp = "".join(Num)
        temp = temp[::-1]
        return temp

# Function to add binary numbers

def Suma_Bin(Num1, Num2):
    max_len = max(len(Num1), len(Num2))
    Num1 = Num1.zfill(max_len)
    Num2 = Num2.zfill(max_len)
    res = ''
    carry = 0
    for i in range(max_len - 1, -1, -1):
        if int(Num1[i]) + int(Num2[i]) + carry == 0:
            res = '0' + res
            carry = 0
        elif int(Num1[i]) + int(Num2[i]) + carry == 1:
            res = '1' + res
            carry = 0
        elif int(Num1[i]) + int(Num2[i]) + carry == 2:
            res = '0' + res
            carry = 1
        elif int(Num1[i]) + int(Num2[i]) + carry == 3:
            res = '1' + res
            carry = 1
    if carry == 1:
        res = '1' + res
    return res

a = Decimal_Binario(dec1)
b = Decimal_Binario(dec2)

sumadec = (dec1 + dec2)

match signo:
    case "N":
        sumabin = Suma_Bin(a, b)
        sumadec = dec1 + dec2
        if sumadec > 65535:
            print("Error, there is overflow, and the erroneous result would be: ", sumabin)
        else:
            print("Binary sum:", sumabin.zfill(16))
            print("Decimal sum:", sumadec)
    case "Y":
        bin1 = ""
        bin2 = ""
        c1 = ""
        c2 = ""
        c12 = ""
        c22 = ""
        if dec1 < 0 and dec2 < 0:
            dec1 = abs(dec1)
            dec2 = abs(dec2)
            bin1 = Decimal_Binario(dec1)
            c1 = bin_c1(bin1)
            c2 = Suma_Bin(c1, "0000000000000001")
            bin2 = Decimal_Binario(dec2)
            c12 = bin_c1(bin2)
            c22 = Suma_Bin(c12, "0000000000000001")
            print("Bin1:", bin1)
            print("Bin2:", bin2)
            print(c2, "c2")
            print(c22, "c22")

            suma = Suma_Bin(c2, c22)

            print(suma)
            print(sumadec)
        elif dec1 < 0 and dec2 > 0:
            bin2 = Decimal_Binario(dec2)
            c12 = bin_c1(bin2)
            c22 = Suma_Bin(c12, "1")
            bin1 = Decimal_Binario(dec1)
            sumabin = Suma_Bin(c22, bin1)
        elif dec1 > 0 and dec2 < 0:
            bin1 = Decimal_Binario(dec1)
            c1 = bin_c1(bin1)
            c2 = Suma_Bin(c1, "1")
            bin2 = Decimal_Binario(dec2)
            sumabin = Suma_Bin(c2, bin2)
        else:
            sumabin = Suma_Bin(a, b)
        
        sumadec = dec1 + dec2

        print("Binary sum:", sumabin.zfill(16))
        print("Decimal sum:", sumadec)
