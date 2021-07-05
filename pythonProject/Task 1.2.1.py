FIO= input("Полные Ф.И.О : ")
fio = FIO.split(" ")
f = fio[0]
i = fio[1]
o = fio[2]
print ("{0} {1}.{2}.".format(f, i[:1], o[:1]))