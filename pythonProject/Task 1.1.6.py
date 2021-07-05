def NumF():
    while True:
        num = input('В диапазоне от 1 до :  ')
        if not num.isdigit():
            print('Введенные символы не являются цыфрами')
            continue
        break
    return int(num)

def simple_num(a):
    if a <= 1 or a % 1 > 0:
        return False
    for i in range(2, a):
        if a % i == 0:
            return False
    return True

def simple_nums(a):
    return [str(i) for i in range(a) if simple_num(i)]
print('\n'.join(simple_nums(NumF())))