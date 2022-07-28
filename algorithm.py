my_dict = {}
my_dict['1'] = 0
for i in range(2,1000001):
    my_dict[str(i)] = my_dict[str(i-1)] + 1
    if not i % 2:
        my_dict[str(i)] = min(my_dict[str(i)], my_dict[str(i//2)] + 1)
    if not i % 3:
        my_dict[str(i)] = min(my_dict[str(i)], my_dict[str(i//3)] + 1)

num = input()
print(my_dict[num])
