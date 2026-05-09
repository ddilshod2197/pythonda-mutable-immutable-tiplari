# Mutable va Immutable tiplarni ta'riflaydigan funksiya
def tip_turi(tip):
    if tip == list:
        return "Mutable"
    elif tip in [int, float, str, tuple]:
        return "Immutable"

# Tuple ichida list bo'lsa nima bo'ladi?
def tuple_ichida_list():
    my_tuple = (1, 2, [3, 4])
    print("Tuple ichida list:", my_tuple)
    print("List turi:", type(my_tuple[2]))
    print("List turi:", tip_turi(type(my_tuple[2])))

# Main funksiya
def main():
    tuple_ichida_list()

# Main funksiya chaqirish
main()
```

Kodni ishga tushirganda, quyidagilarni ko'ring:

- `tip_turi` funksiyasi `list`, `int`, `float`, `str`, `tuple` kabi turli tipni qabul qiladi va ularni `Mutable` yoki `Immutable` deb qaytaradi.
- `tuple_ichida_list` funksiyasi `tuple` ichida `list` bo'lishini ko'rsatadi. Natijada, `tuple` ichida `list` bo'lishi `Mutable` tipga aylanadi.
