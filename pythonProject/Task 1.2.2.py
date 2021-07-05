str = list(input("Введите любые символы: "))
sum = 0
for i in range(0, len(str)):
    if str[i].isdigit():
        sum+=int(str[i])
print (sum) 