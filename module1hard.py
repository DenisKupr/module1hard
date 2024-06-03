### Средний балл ###

grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]  # Список
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}  # Множество
lst_ = list(students)  # Перевод множества в список
res_ = lst_.sort()  # Сортировка списка

aaron_sum = sum(grades[0]) / len(grades[0])  # Расчет среднего балла для Aaron
bilbo_sum = sum(grades[1]) / len(grades[1])  # Расчет среднего балла для Bilbo
johnny_sum = sum(grades[2]) / len(grades[2])  # Расчет среднего балла для Johnny
khendrik_sum = sum(grades[3]) / len(grades[3])  # Расчет среднего балла для Khendrik
steve_sum = sum(grades[4]) / len(grades[4])  # Расчет среднего балла для Steve

# Словарь с ключем в виде Имени и средним балом
dct_ = {
    lst_[0]: aaron_sum,
    lst_[1]: bilbo_sum,
    lst_[2]: johnny_sum,
    lst_[3]: khendrik_sum,
    lst_[4]: steve_sum
}

print(dct_)  # Вывод в консоль

# Решение с помощью цикла

result = {}
for now in range(len(lst_)):
    result[lst_[now]]=sum(grades[now])/len(grades[now])
print(result)

