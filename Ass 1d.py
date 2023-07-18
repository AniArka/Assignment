x = int(input("enter starting range"))
y = int(input("enter closing range"))
prime_list = []
for i in range(x, y+1):
    if i > 1:
        for j in range(2, int(i / 2) + 1):
            if i % j == 0:
                break
        else:
            prime_list.append(i)
print(prime_list)