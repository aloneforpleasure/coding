from random import randint
rand_list = list()
sorted_list = [0]
for i in range(11):
    rint = randint(0, 100)
    while rint in rand_list:
        rint = randint(0, 100)
    rand_list.append(rint)
    pos = 0
    while True:
        while pos != len(sorted_list):
            if rint > sorted_list[pos]:
                break
            else:
                pos += 1
        sorted_list.insert(pos, rint)
        break
sorted_list.remove(0)
print(f"Genereted list: {rand_list}")
print(f"Reversed list: {sorted_list}")

