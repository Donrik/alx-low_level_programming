largest_palindrome = 0

for i in range(100, 1000):
    for j in range(i, 1000):
        product = i * j
        if str(product) == str(product)[::-1] and product > largest_palindrome:
            largest_palindrome = product

# Save the result in the file "102-result"
with open("102-result", "w") as file:
    file.write(str(largest_palindrome))

