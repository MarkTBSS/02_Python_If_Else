n = 3
print(n)
print(type(n))

result = ""

# n เป็นเลขคี่ (Odd) แสดงผล "Weird"
if n % 2 != 0:
    result = "Weird"

# n เป็นเลขคู่ (Even) และมีค่า 2 ถึง 5 แสดงผล "Not Weird"
if n % 2 == 0 and 2 <= n <= 5:
    result = "Not Weird"

# n เป็นเลขคู่ (Even) และมีค่า 6 ถึง 20 แสดงผล "Weird"
if n % 2 == 0 and 6 <= n <= 20:
    result = "Weird"

# n เป็นเลขคู่ (Even) และมีค่ามากกว่า 20 แสดงผล "Not Weird"
if n % 2 == 0 and n > 20:
    result = "Not Weird"

print(result)
print(type(result))