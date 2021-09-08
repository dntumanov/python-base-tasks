# Task - 1
def get_user_info(username: str, age: int, current_city: str) -> str:
    """Get user info"""
    return f'{username}, {age} год(а), проживает в городе {current_city}'


# Task - 2
def get_max_number(*nums) -> int:
    """Get max number"""
    return max(nums)


# Task - 3-4
def attack(attacker: dict, defender: dict):
    """Attack enemy and update health defender"""
    damage_attacker: int = attacker.get('damage')
    defender_health: int = defender.get('health')
    armor_defender: float = defender.get('armor')
    updated_health_defender: dict = {'health': defender_health - get_damage_done(damage_attacker, armor_defender)}
    defender.update(updated_health_defender)


def get_damage_done(damage: int, armor: float):
    """Get sequent damage"""
    return damage / armor

# username, age, current_city = input('Введите имя, возвраст, город через пробел: ').strip().split()
# print(get_user_info(username, age, current_city))
# print(get_max_number(1, 5, 3))


player: dict = {
    "name": "Denis",
    "health":  100,
    "damage": 50,
    "armor": 1.2
}

enemy: dict = {
    "name": "Jora",
    "health":  100,
    "damage": 50,
    "armor": 1.2
}

attack(enemy, player)
print(player)





