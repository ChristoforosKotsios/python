#Python 2.7.12
#Christoforos Kotsios for UniPi
#Email: c.kotsios@gmail.com

class py_solution:
    def int_to_Roman(self, num):
        val = [
            1000000, 500000, 100000, 50000, 10000, 5000, 1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4,
            1
            ]
        syb = [
            "!M", "!D", "!C", "!L", "!X", "!V" ,"M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV",
            "I"
            ]
        roman_num = ''
        i = 0
        while  num > 0:
            for _ in range(num // val[i]):
                roman_num += syb[i]
                num -= val[i]
            i += 1
        return roman_num

while True:
    dothis= int(input('Enter A number: '));
    while 1>0:
        if dothis >= 1000000:
            print ("Duo grammes pio pano to grafei. Piso Gianni ta karavia.")
            dothis= int(input('Enter A number'));
        elif dothis == 0:
            print ("Romans and Ancient Greeks has not symbol for zero.")
            break
        else:
            print(py_solution().int_to_Roman(dothis))
            break
    ans = raw_input('Do you want to continue? (Y/n)\n')
    if ans == 'n'or ans== 'N':
        break
