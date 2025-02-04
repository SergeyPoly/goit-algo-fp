import random

# Кількість симуляцій
num_rolls = 1000000

# Зберігаємо кількість випадків для кожної можливої суми (від 2 до 12)
sums_count = {i: 0 for i in range(2, 13)}

# Симуляція кидків кубиків
for _ in range(num_rolls):
    roll1 = random.randint(1, 6)
    roll2 = random.randint(1, 6)
    roll_sum = roll1 + roll2
    sums_count[roll_sum] += 1

# Обчислення ймовірностей
sums_probabilities = {k: v / num_rolls * 100 for k, v in sums_count.items()}

# Аналітичні ймовірності (з таблиці)
analytical_probabilities = {
    2: 2.78, 3: 5.56, 4: 8.33, 5: 11.11, 6: 13.89,
    7: 16.67, 8: 13.89, 9: 11.11, 10: 8.33, 11: 5.56, 12: 2.78
}

# Виведення результатів (таблиця порівнянь ймовірностей)
print(f"\n{'Сума':^6} | {'Імовірність (Монте-Карло)':^25} | {'Імовірність (Теоретична)':^25}")
print("-" * 62)

for i in range(2, 13):
    print(f"{i:^6} | {sums_probabilities[i]:>5.2f}%{' ' * 19} | {analytical_probabilities[i]:>5.2f}%")
