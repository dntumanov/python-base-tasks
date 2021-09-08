# Task - 1

def get_filter_list(first_list: list, second_list: list) -> list or str:
    """Возвращает список с удаленными элементами, присуствующие во втором списке"""
    # first_list_without_dupl = list(set(first_list))
    for item in second_list:
        try:
            while True:
                first_list.remove(item)
        except ValueError:
            continue
    return first_list


# Task - 2
def get_unique_item_from_list(list_of_value: list[int]) -> list[int]:
    return [i for i in list_of_value if list_of_value.count(i) == 1]


my_list_1: list = [2, 5, 8, 2, 12, 12, 4]
my_list_2: list = [2, 7, 12, 3]
print(get_filter_list(my_list_1, my_list_2))

my_list_3: list = [2, 2, 5, 12, 8, 2, 12]
print(get_unique_item_from_list(my_list_3))




