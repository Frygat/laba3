# TODO Напишите функцию для поиска индекса товара

def find_item_index(items_list, find_item):  # функция, которая принимает 2 аргумента

    for index, item in enumerate(items_list):    # идёт перебор элементов списка, если найден нужный элемент, то возвращаем его индекс
        if item == find_item:
            return index
    return None   # в случае, если предмет не был найден возвращаем None

items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']

for find_item in ['банан', 'груша', 'персик']:
    index_item =  find_item_index(items_list, find_item)
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")