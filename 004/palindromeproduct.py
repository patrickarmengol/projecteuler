# work backwards from 999 * 999 and check for palindrome each iteration
# use string reversal for palindrome checks
# keep track of largest palproduct

largest = 0
for i in range(999,99,-1):
    for j in range(i,99,-1):
        product = i * j
        if str(product)[::-1] == str(product):
            if product > largest:
                largest = product
            break
print(largest)
            