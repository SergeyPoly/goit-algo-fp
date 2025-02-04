def greedy_algorithm(items, budget):
    # Сортуємо їжу за співвідношенням калорій до вартості (від більшого до меншого)
    sorted_items = sorted(items.items(), key=lambda x: x[1]["calories"] / x[1]["cost"], reverse=True)
    
    total_calories = 0
    chosen_items = {}

    for item, info in sorted_items:
        if budget >= info["cost"]:
            count = budget // info["cost"]  # Беремо максимальну кількість цієї страви
            chosen_items[item] = count
            total_calories += count * info["calories"]
            budget -= count * info["cost"]  # Оновлюємо залишок бюджету

    return chosen_items, total_calories


def dynamic_programming(items, budget):
    dp = [0] * (budget + 1)  # dp[j] - максимальна калорійність при бюджеті j
    chosen = [{} for _ in range(budget + 1)]  # Таблиця для відновлення вибору страв

    for name, data in items.items():
        cost, calories = data["cost"], data["calories"]

        for j in range(cost, budget + 1):
            if dp[j - cost] + calories > dp[j]:  # Якщо вибір страви покращує калорійність
                dp[j] = dp[j - cost] + calories
                chosen[j] = chosen[j - cost].copy()  # Копіюємо попередній стан

                if name in chosen[j]:
                    chosen[j][name] += 1
                else:
                    chosen[j][name] = 1

    max_calories = dp[budget]
    selected_items = chosen[budget]

    return selected_items, max_calories


# Приклад використання:
items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

budget = 100

greedy_result, greedy_calories = greedy_algorithm(items, budget)
dp_result, dp_calories = dynamic_programming(items, budget)

print("\nЖадібний алгоритм:")
print("Обрані страви:", greedy_result)
print("Загальна калорійність:", greedy_calories)

print("\nДинамічне програмування:")
print("Обрані страви:", dp_result)
print("Загальна калорійність:", dp_calories)