## Homework. Functions

1. Create a function that accepts the name, age and city of residence of a person as input. The function should return a string of the form "Vasily, 21 years old, lives in the city of Moscow"
2. Create a function that takes 3 numbers as input and returns the largest of them.
3. Let's describe a pair of `player` and `enemy` entities through a dictionary that will have keys and values:
`name` - the string received from the user,
`health = 100,`
`damage = 50`.
> Experiment with damage and life values as desired. 
> Now we need to create the `attack(person1, person2)` function. 
> Note: you can specify your own argument names. ### The function will take the attacker and the attacked as an argument. 
> In the body, the function should get the damage parameter of the attacker and subtract this amount from the health of the attacked. 
> The function itself must work with dictionaries and change their values.

4. Давайте усложним предыдущее задание. Измените сущности, добавив новый параметр - `armor = 1.2` (величина брони персонажа)
   Теперь надо добавить новую функцию, которая будет вычислять и возвращать полученный урон по формуле `damage / armor`
   Следовательно, у вас должно быть 2 функции:
   > Наносит урон. Это улучшенная версия функции из задачи 3. Вычисляет урон по отношению к броне. Примечание. 
   > Функция номер 2 используется внутри функции номер 1 для вычисления урона и вычитания его из здоровья персонажа. 