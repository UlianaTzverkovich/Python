alphaRU = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
a = []
for i in range(0,len(alphaRU)+1):
    for j in range (1,len(alphaRU)+1):
        if len(a)> len(alphaRU)-1:
            break
        a.append(alphaRU[i:j])
print(a)
