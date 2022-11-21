from pprint import pprint


def dict_cook_book(file_path):
    with open(file_path, 'r', encoding='utf 8') as file_work:
        menu = {}
        for line in file_work:
            dish_name = line[:-1]
            counter = file_work.readline().strip()
            list_of_ingredient = []
            for i in range(int(counter)):
                dish_items = dict.fromkeys(['ingredient_name', 'quantity', 'measure'])  # временный словарь
                ingredient = file_work.readline().strip().split(' | ')  # перемещение по файлу
                for item in ingredient:
                    dish_items['ingredient_name'] = ingredient[0]
                    dish_items['quantity'] = ingredient[1]
                    dish_items['measure'] = ingredient[2]
                list_of_ingredient.append(dish_items)
                cook_book = {dish_name: list_of_ingredient}
                menu.update(cook_book)
            file_work.readline()

    return (menu)


dict_cook_book('recipes.txt')


def get_shop_list_by_dishes(dishes, persons=int):
    menu = dict_cook_book('recipes.txt')
    print('Ознакомьтесь с Нашим меню :')
    pprint(menu)
    print()
    shopping_list = {}

    try:
        for dish in dishes:
            for item in (menu[dish]):
                # print(item['ingredient_name'])
                # print(item['measure'])
                # print(item['quantity'])
                items_list = dict([(item['ingredient_name'],
                                    {'measure': item['measure'], 'quantity': int(item['quantity']) * persons})])
                if shopping_list.get(item['ingredient_name']):
                    # print(f' Такое {items_list} уже есть в списке. Добавил еще')
                    extra_item = (int(shopping_list[item['ingredient_name']]['quantity']) +
                                  int(items_list[item['ingredient_name']]['quantity']))
                    # print(extra_item)
                    shopping_list[item['ingredient_name']]['quantity'] = extra_item

                else:
                    # shopping_list[item['ingredient_name']]['quantity'] *= persons
                    shopping_list.update(items_list)

        print(f"Для приготовления блюд на {persons} человек  нам необходимо купить:")
        pprint(shopping_list)
    except KeyError:
        print("Вы ошиблись в названии блюда, проверьте ввод")


get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)
