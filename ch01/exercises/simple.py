print(10 * 5, 10**2, 15 / 10, 15 // 10, -15 // 10, 15 % 10, 10 % 15, 10 % 10, 0 % 10, 10 / 15)

#technically, the answer is wrong. Since it terminates, it's an approximation of the value and not the exact value. 2/3 is the exact value.

print("Provide the current exchange rate for the Euro to Dollar:")
rate = int(input())
print("Provide the amount of currency to exchange:")
amount = int(input())
total = amount * rate
result = total - 3
print (result)