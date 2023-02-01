#  Напишите программу, удаляющую из текста все слова, содержащие "абв".

text = 'фывабвйцу, кеабвджэ. ячсбвнгш йцукенгвба'
list = []
list1 = []
list = text.split()
for i in range(len(list)):
    if 'абв' not in  list[i]:
        list1.append(list[i])
list1 = " ".join(list1)
print(list1)