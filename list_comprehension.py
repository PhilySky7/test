# new_list = []

# for num in integer:
#     if num % 2 == 0:
#         new_list.append(num)

# print(new_list)

integer = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
new_list = [num for num in integer if num % 2 == 0]
print(list(new_list))


new_tuple = tuple(map(lambda x: x**2, new_list))
print(new_tuple)

# keys = ["a", "b", "c"]
# values = [1, 2, 3]
#
# key_value = {k: v for k, v in zip(keys, values)}
# print(key_value)