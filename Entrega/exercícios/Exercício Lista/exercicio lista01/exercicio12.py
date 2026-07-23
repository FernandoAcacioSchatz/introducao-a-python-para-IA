valores = [2, 4, 6, 1, 1, 2, 2, 3, 4, 4, 5]
print(f"{', '.join(map(str, dict.fromkeys(valores)))}")

print(f"{', '.join(map(str, set(valores)))}")
