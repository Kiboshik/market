from meat_milk import meat_milk_dep
from Bakingfinal import baking_dep
from cleaning_materials import cleaning_dep


global total_cart
total_cart = {}

def greeting():
    total_sum = 0
    print("Здраствуйте")
    greet = int(input("1: Здраствуйте\n 0: Выход\n Ваш выбор-->"))
    while greet > 0:
        print("""
            Добро пожаловать в наш супермаркет!
            Вы можете войти в один из отделов нашего маркета:
            1 - Мясо и молочная продукция
            2 - Хлеб и выпечка
            3 - Мыломойка
            4 - Посмотреть общий счёт
            5 - Пройти в кассу и расшитаться
            0 - Выйти из магазина
            Ваш выбор: 
            """)
        choice = int(input("Ваш выбор-->"))
        if choice == 1:
           total_sum += meat_milk_dep()
        elif choice == 2:
            total_sum += baking_dep()
        elif choice == 3:
            total_sum += cleaning_dep()
        elif choice == 4:
            print(total_sum)
        elif choice == 5:
            try:
                money = int(input("Введите количество денег: "))
            except ValueError:
                print("Вы ввели не число!")

                basket_sum = total_sum
                print(basket_sum)
                if money > basket_sum:
                    change = money - basket_sum
                    print(change)
                elif money == basket_sum:
                    change = 0
                elif money < basket_sum:
                    raise Exception("Вам недостаточно денег!")
                break



        elif choice == 0:
            break







greeting()

if __name__ == "__main__":
    greeting()