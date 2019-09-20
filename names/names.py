import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()
# Original Method: runtime is slow
# duplicates = []
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)


# Iterative - runtime is approx 1.84, still pretty slow
# duplicates = []
# storage = []

# for name_1 in names_1:
#     storage.append(name_1)

# for name_2 in names_2:
#     if name_2 in storage:
#         duplicates.append(name_2)


# Dictionary - runtime is approx 0.010, pretty fast
duplicates = []
storage = {}

for name_1 in names_1:
    storage[name_1] = name_1

for name_2 in names_2:
    if name_2 in storage:
        duplicates.append(name_2)


end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")