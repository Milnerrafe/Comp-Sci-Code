a = 10
b = 3

print(f"Addition: {a + b}")
print(f"Modulus: {a % b}")

age = 14
hasPermission = True

if age >= 15 and hasPermission:
    print("Allowed to participate")
else:
    print("Not Allowed")


print(True or False and not True)
# Evaluates as: True or (False and True) -> True or False -> True
