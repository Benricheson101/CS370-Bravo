list = []

list2 = ["dog", "cat", "bird"]

for i in range(len(list2)):
    list.append(0)

print(list)

for i in range(len(list2)):
    list[i] = list2[i]

print(list)

