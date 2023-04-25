class Product():
    def __init__(self, id, category, name, srok_godnosti, volume, ves, price):
        try:
            self.id = int(id) #уникальный идентификатор
            self.category = str(category) #категория
            self.name = str(name) #имя
            self.godnost = int(srok_godnosti) #сколько дней может выдержать не портясь
            self.volume = int(volume) #объём в миллилитрах
            self.ves = int(ves) #вес в граммах
            self.price = int(price) #цена
        except ValueError:
            print("Это не число")

milk = Product(124356, "Products", "Milk", 7, 1500, False, 67)

sugar = Product(309475, "Products", "Sugar", 365, False, 750, 72)

chips = Product(263849, "Products", "Chips", 128, False, 150, 103)

butter = Product(786582, "Products", "Butter", 31, False, 450, 327)

lemon = Product(283444, "Products", "Lemon", 36, False, 40, 17) 

spisok_produktov = [sugar, chips, butter, lemon, milk]

try:
    while True:
        a = int(input("Выбирете действие: \n1 Просмотр продуктов. \n2 Фильтрация по колличеству букв в товаре. \n3 Выход."))
        if a == 1:
            print(" ")
            print("У нас есть такие продукты: ")
            print(f"Имя : {milk.name}, ID : {milk.id}, категория: {milk.category}, в нормальных условиях может выдержать не портясь : {milk.godnost} дней, объём : {milk.volume} милилитов, вес : {milk.ves} грамм, цена : {milk.price} рублей.")
            print(" ")
            print(f"Имя : {sugar.name}, ID : {sugar.id}, категория: {sugar.category}, в нормальных условиях может выдержать не портясь : {sugar.godnost} дней, объём : {sugar.volume} милилитов, вес : {sugar.ves} грамм, цена : {sugar.price} рублей.")
            print(" ")
            print(f"Имя : {chips.name}, ID : {chips.id}, категория: {chips.category}, в нормальных условиях может выдержать не портясь : {chips.godnost} дней, объём : {chips.volume} милилитов, вес : {chips.ves} грамм, цена : {chips.price} рублей.")
            print(" ")
            print(f"Имя : {butter.name}, ID : {butter.id}, категория: {butter.category}, в нормальных условиях может выдержать не портясь : {butter.godnost} дней, объём : {butter.volume} милилитов, вес : {butter.ves} грамм, цена : {butter.price} рублей.")
            print(" ")
            print(f"Имя : {lemon.name}, ID : {lemon.id}, категория: {lemon.category}, в нормальных условиях может выдержать не портясь : {lemon.godnost} дней, объём : {lemon.volume} милилитов, вес : {lemon.ves} грамм, цена : {lemon.price} рублей.")

        elif a == 2:
            b = int(input("Выбирете число для сортировки"))
            print(" ")
            print("Итоговые продукты : ")
            print(*(f"Имя: {x.name}, ID: {x.id}, категирия: {x.category}, годность: {x.godnost} дней, вес: {x.ves} грамм, объем: {x.volume} миллилитров, цена: {x.price} рублей." for x in spisok_produktov if len(x.name) > b), sep='\n')

        elif a == 3:
            print(" ")
            print("Выход")
            break

        else:
            print(" ")
            print("Вы ввели неправильное число")

except AttributeError:
   print("Ошибка атрибута: AttributeError")
   