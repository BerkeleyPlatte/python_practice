def sum(num1, num2):
    return num1 + num2

# print(sum(1, 2))

def dif(num1, num2):
    return num1 - num2

# print(dif(1, 2))

def calc(vari):
    return vari(1, 2)

print(calc(sum))

print(calc(dif))
    


