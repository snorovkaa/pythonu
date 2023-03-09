import csv

try:
    with open("countries.csv") as file:
        lst = list(csv.reader(file))[1::]
        income_min, income_max = list(map(float, input("Минимальный и максимальны доходы через пробел: ").split()))
        with open('a.csv', 'w+') as file_a:
            writer = csv.writer(file_a, lineterminator='\n')
            writer.writerows(list(filter(lambda x: float(x[2]) < income_max and float(x[2]) > income_min, lst)))
        with open('b.csv', 'w+') as file_b:
            writer = csv.writer(file_b, lineterminator='\n')
            writer.writerows(sorted(lst, key = lambda x: float(x[3])))

except:
    print("Ошибка")
