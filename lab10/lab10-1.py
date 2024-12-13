import math  

def calculate_amortized_cost(n):
    k = int(math.log2(n))  
    cost_powers_of_two = (2 ** (k + 1)) - 1

    num_non_powers_of_two = n - (k + 1)
    cost_others = num_non_powers_of_two

    total_cost = cost_powers_of_two + cost_others

    amortized_cost = total_cost / n

    return total_cost, amortized_cost

n = 10
total_cost, amortized_cost = calculate_amortized_cost(n)
print(f"Total cost (T({n})) = {total_cost}")
print(f"Amortized cost = {amortized_cost:.2f}")
