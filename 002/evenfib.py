# eww ugly code
# somehow, i struggled to come up with a solution that used unpacking and ended up keeping track of 3 variables
# b2 = 1
# b1 = 2
# i = 3
# evens = [2]

# while i < 4000000:
#     if i % 2 == 0:
#         evens.append(i)
#     b2 = b1
#     b1 = i
#     i = b1+b2

# print(sum(evens))



# rewriting with unpacking after some thought; could take out the list and just sum during iteration, but w.e.
b = 1
i = 2
evens = []

while i < 4000000:
    if i % 2 == 0:
        evens.append(i)
    i, b = i + b, i

print(sum(evens))