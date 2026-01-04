def greedy_algorithm(items, budget):
    ratio_items = []
    for name, data in items.items():
        ratio = data["calories"] / data["cost"]
        ratio_items.append((name, data["cost"], data["calories"], ratio))
    
    ratio_items.sort(key=lambda x: x[3], reverse=True)
    
    selected_items = []
    total_calories = 0
    remaining_budget = budget
    
    for name, cost, calories, ratio in ratio_items:
        if remaining_budget >= cost:
            selected_items.append(name)
            total_calories += calories
            remaining_budget -= cost
            
    return selected_items, total_calories

def dynamic_programming(items, budget):
    item_list = list(items.items())
    n = len(item_list)
    dp = [[0 for _ in range(budget + 1)] for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        name, data = item_list[i-1]
        cost = data["cost"]
        calories = data["calories"]
        for b in range(budget + 1):
            if cost <= b:
                dp[i][b] = max(dp[i-1][b], dp[i-1][b - cost] + calories)
            else:
                dp[i][b] = dp[i-1][b]
    
    selected_items = []
    b = budget
    for i in range(n, 0, -1):
        if dp[i][b] != dp[i-1][b]:
            name, _ = item_list[i-1]
            selected_items.append(name)
            b -= items[name]["cost"]
            
    return selected_items, dp[n][budget]

items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

budget = 100

g_items, g_cal = greedy_algorithm(items, budget)
d_items, d_cal = dynamic_programming(items, budget)

print(f"Greedy: {g_items}, Calories: {g_cal}")
print(f"DP: {d_items}, Calories: {d_cal}")