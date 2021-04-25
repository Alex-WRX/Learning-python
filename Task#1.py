count1 = int(input('Введите число 1 '))
count2 = int(input("Введите число 2"))

def my_div(coun1, count2):
    if count2 == 0:
        count2 = int(input("Введите числе больше 0"))
    result = coun1 / count2
    return result
response = my_div(count1, count2)
print(response)