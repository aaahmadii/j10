import random

random_numbers = [random.randint(1, 100) for _ in range(10)]

even_numbers = [num for num in random_numbers if num % 2 == 0]
odd_numbers = [num for num in random_numbers if num % 2 != 0]

print("لیست اعداد تصادفی:", random_numbers)
print("لیست اعداد زوج:", even_numbers)
print("لیست اعداد فرد:", odd_numbers)
