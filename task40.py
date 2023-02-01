# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Модуль сжатия:
# Для чисел:
# Входные данные:
# 111112222334445
# Выходные данные:
# 5142233415
# Также должно работать и для букв:
# Входные данные:
# AAAAAAFDDCCCCCCCAEEEEEEEEEEEEEEEEE
# Выходные данные:
# 6A1F2D7C1A17E


def RLEcompression(line):
    list = [i for i in line]
    list2 = []
    count = 1
    for i in range(len(list)-1):
        if list[i] == list[i+1]:
            count += 1
        else:
            list2.append(count)
            list2.append(list[i])
            count = 1
    if list[-1] != list[-2]:
        list2.append(1)
        list2.append(list[-1])
    else:
        while list[-1] == list[-1 - i]:
            i += 1
            count += 1
        list2.append(count)
        list2.append(list[-1])
    return list2

line = "111112222334444"
print(RLEcompression(line))