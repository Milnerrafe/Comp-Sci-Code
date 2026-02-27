numbers = [10, 20, 30, 40, 50]
print(numbers)

print(f"First element: {numbers[0]}")
print(f"Last element: {numbers[-1]}")

numbers[2] = 35
print(f"Updated list {numbers}")

print(f"The list is, {len(numbers)}, numbers long.")


numbers.pop(1)
numbers.append(26)

print(numbers)
