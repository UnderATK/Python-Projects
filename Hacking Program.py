import random
def crypt():
    global result,key
    choose_strenght = input("Please choose Crypt mode:\n"
                            "1.High Crypt\n"
                            "2.Low Crypt\n"
                            "3.Your Own Crypt\n")
    if choose_strenght == '1':
        str = input("Please enter sentence: ")
        i, num, result = 0, len(str), ""
        key = 27*8-4**3
        for x in range(0, num):
            i = ord(str[x]) + key
            result = result + chr(i)
        return result
    elif choose_strenght == '2':
        str = input("Please enter sentence: ")
        i, num, result = 0, len(str), ""
        key = random.randint(1,10)
        for x in range(0, num):
            i = ord(str[x]) + key
            result = result + chr(i)
        return result
    elif choose_strenght == '3':
        str = input("Please enter sentence: ")
        i, num, result = 0, len(str), ""
        key = int(input("Please enter a number to move: "))
        for x in range(0, num):
            i = ord(str[x]) + key
            result = result + chr(i)
        return result
    else:
        print("Invalid Input")
        crypt()

def de_crypt():
    i, num, result1 = 0, len(result), ""
    for x in range(0, num):
        i = ord(result[x]) - key
        result1 = result1 + chr(i)
    return result1

def file_crypt():
    result2,i = "",0
    key = int(input("Please enter a number to move: "))
    f = open("testmul.txt","r")
    f_lines = f.readlines()
    f.close()
    global a
    for x in f_lines:
        a = x.split(" ")
        for x2 in x:
            try:
                i = ord(x2) + key
                result2 = result2 + chr(i)
            except:
                pass
    file_name = input("Please enter file name to save your crypt: ")
    f = open(file_name,"w")
    f.write(result2)
    f.close()

def BT(x):
    generator = list(map(str,'abcdefghijklmnopqrstuvwxyz'))
    result3 = ''
    for check in x:
        try:
            if str(check == generator):
                result3 = result3 + check
        except:
            pass
    return result3

while True:
    print(" Welcome to Hacking program! ".center(78,'='))
    choose = input("Please select your hack:\n"
                   "1. Crypt\n"
                   "2. De-Crypt\n"
                   "3. Crypt from your file\n"
                   "4. BT file\n"
                   "5. Exit - press 0\n")
    if choose == '0':
        break
    elif choose == '1':
        print(crypt())
    elif choose == '2':
        print(de_crypt())
    elif choose == '3':
        file_crypt()
    elif choose == '4':
        file_choose_BT = input("Please enter file path or file name to BruteForce:\n")
        f = open(file_choose_BT, "r")
        file_gen = f.readlines()
        f.close()
        print(BT(file_gen))
    else:
        print("Wrong Input!")
        break
