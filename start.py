def start(user_ch):
    user_ch = int(input(
        """
        Добро пожаловать в наш супермаркет!
        Вы можете войти в один из отделов нашего маркета:
        1 - Мясо и молочная продукция
        2 - Хлеб и выпечка
        3 - Мыломойка
        0 - Выйти из магазина
        Ваш выбор: 
        """
    ))
    return user_ch