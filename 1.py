import json


def f():
    file = open("animals.json").read()
    info = json.loads(file)

    if "animals" in info:

        info = info["animals"]

        def getAnimals(info, typename, type):
            return list(filter(lambda i: typename in i and i[typename] == type, info))


        print(getAnimals(info, "animal_type", "Bird"))
        print(len(getAnimals(info, "active_time", "Diurnal")))
        print(min(info, key=lambda x: float(x['weight_min'])))

try:
    f()
except:
    print("Ошибка")
