a, b = 1, 1
results = [1, 1]
for _ in range(0, 100):
    a, b = a + b, a
    results.append(a)

print(*results)