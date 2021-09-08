from math import sqrt

# 1.
fruit1: list[str] = ['мандарин', 'апельсин', 'банан', 'яблоко', 'виноград']
fruit2: list[str] = ['нектарин', 'мандарин', 'дыня', 'персик', 'апельсин']

print([fruit for fruit in fruit1 if fruit in fruit2])

# 2.
print([item for item in range(-100, 101) if item % 3 == 0 and item > 0 and item != 4])


# 3.
def sqrt_nums(lst: list[int]) -> list[float]:
    """Get sqrt list numbers"""
    print(f'Old list {lst}')
    return [
        sqrt(number) if number > 0 else number for number in lst
    ]


print(sqrt_nums([1, -3, 4]))


# 4.
def get_squared_number(number: int) -> int:
    if number == 13:
        raise ValueError('Need a number more or less than 13')
    elif type(number) is str:
        raise TypeError('Need a number')
    else:
        return number**2


user_number = input('Put a number: ')
print(get_squared_number(user_number))

