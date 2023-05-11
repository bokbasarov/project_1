categories = ["Головной убор", "Верхняя одежда", "Нижняя одежда", "Обувь", "Аксессуары"]

products = [
    ["Кепка", "Шапка", "Шляпа", "Панама", "Бандана Kanye Westа"],
    ["Куртка", "Толстовка", "Ветровка", "Майка", "Футболка", "Джемпер", "Тишка 'Yeezus' в подарок Вилла"],
    ["Джинсы", "Штаны", "Шорты", "Подштанники", "Трусы", "Джинсы 'Big Boys'"],
    ["Кроссовки", "Сапожки", "Тапочки", "Макасины", "Тяги", "Yeezy Foamrunner в подарок $1,5млн"],
    ["Сумка", "Ремень", "Шарф", "Очки", "Нос клоуна", "Парик клоуна", "Кольцо 'MF DOOM' в подарок яхта"]
]

colors = [
    ["Красный", "Синий", "Зеленый", "Черный", "Белый", "Бездарный"],
    ["Черный", "Белый", "Серый", "Бежевый", "Малиновый", "Кофе", "Электро", "Золотой", "Серебряный", "Бронзовый", "Бездарный"],
    ["Розовый", "Фиолетовый", "Желтый", "Ментол", "Изумрудный", "Салатовый", "Бездарный"],
    ["Коричневый", "Оранжевый", "Голубой", "Еврейский", "Фашистский", "Гитлерский", "Бездарный"],
    ["Золотой", "Серебряный", "Бронзовый", "Нацистский", "Кровавый", "Обсидиановый", "Бэдроковый", "Бездарный"]
]

spisok = []

def show_categories():
    print("Категории:")
    for i, category in enumerate(categories):
        print(f"{i+1}. {category}")

def show_products(category_index):
    if category_index < 1 or category_index > len(products):
        print("Че ты вбил?")
        return

    print(f"Товары категории '{categories[category_index-1]}':")
    for i, product in enumerate(products[category_index-1]):
        print(f"{i+1}. {product}")

def show_colors(product_index):
    if product_index < 1 or product_index > len(colors):
        print("Некорректный нум товара")
        return

    print(f"Цвета товара '{products[selected_category-1][product_index-1]}':")
    for i, color in enumerate(colors[product_index-1]):
        print(f"{i+1}. {color}")

def add_to_cart(category_index, product_index, color_index):
    if category_index < 1 or category_index > len(products):
        print("Некорректный номер категории")
        return

    if product_index < 1 or product_index > len(products[category_index-1]):
        print("Некорректный омер товара")
        return

    if color_index < 1 or color_index > len(colors[product_index-1]):
        print("Некорректный индекс цвета")
        return

    category = categories[category_index-1]
    product = products[category_index-1][product_index-1]
    color = colors[product_index-1][color_index-1]

    spisok.append((category, product, color))
    print(f"Товар '{product}' ({color}) добавлен в корзину")

def remove_from_cart(index):
    if index < 0 or index >= len(spisok):
        print("Некорректный индекс")
        return

    item = spisok.pop(index)
    print(f"Товар '{item[1]}' ({item[2]}) удален из корзины")

def show_cart():
    if not spisok:
        print("Корзина пуста")
    else:
        print("Товары в корзине:")
        for i, item in enumerate(spisok):
            print(f"{i+1}. {item[0]}: {item[1]} ({item[2]})")


while True:
    show_categories()
    selected_category = int(input("Выберите категорию: "))

    if selected_category < 1 or selected_category > len(categories):
        print("Некорректный индекс категории")
        continue

    show_products(selected_category)
    selected_product = int(input("Выберите товар: "))

    if selected_product < 1 or selected_product > len(products[selected_category-1]):
        print("Некорректный номер товара")
        continue

    show_colors(selected_product)
    selected_color = int(input("Выберите цвет: "))

    if selected_color < 1 or selected_color > len(colors[selected_product-1]):
        print("Некорректный номер цвета")
        continue

    add_to_cart(selected_category, selected_product, selected_color)
    show_cart()

    continue_shopping = input("Хотите продолжить покупки? (да/нет): ")
    if continue_shopping.lower() != "да":
        break

print("Спасибо за покупки!")

