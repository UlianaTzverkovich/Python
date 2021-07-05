def NumF():
    while True:
        num = input('От числа: ')
        if not num.isdigit():
            print('Введенные символы не являются цыфрами')
            continue
        break
    return int(num)


def NumT():
    while True:
        num = input('До числа: ')
        if not num.isdigit():
            print('Введенные символы не являются цыфрами')
            continue
        break
    return int(num)


def num_list(fromm, to):
    return [str(i) for i in range(fromm, to) if len(set(str(i))) == len(str(i))]


print('\n'.join(num_list(NumF(), NumT())))