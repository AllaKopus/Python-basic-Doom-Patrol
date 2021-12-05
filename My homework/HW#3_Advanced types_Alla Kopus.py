import functools

# 1
int_a = 55
print(id(int_a))
# 9790720
str_b = 'cursor'
print(id(str_b))
# 140055551340272
set_c = {1, 2, 3}
print(id(set_c))
# 140055551306432
lst_d = [1, 2, 3]
print(id(lst_d))
# 140055552212672
dict_e = {'a': 1, 'b': 2, 'c': 3}
print(id(dict_e))
# 140055552164480

# 2
lst_d.extend([4, 5])
print(id(lst_d))
# 140055552212672

# 3
print(type(int_a))
# <class 'int'>
print(type(str_b))
# <class 'str'>
print(type(set_c))
# <class 'set'>
print(type(lst_d))
# <class 'list'>
print(type(dict_e))
# <class 'dict'>

# 4
print(isinstance(int_a, int))
# True
print(isinstance(str_b, str))
# True
print(isinstance(set_c, set))
# True
print(isinstance(lst_d, list))
# True
print(isinstance(dict_e, dict))
# True

# 5
print("Anna has {} apples and {} peaches.".format(3, 6))
# Anna has 3 apples and 6 peaches.

# 6
print("Anna has {0} apples and {1} peaches.".format(3, 6))
# Anna has 3 apples and 6 peaches.

# 7
print("Anna has {three} apples and {six} peaches.".format(three=3, six=6))
# Anna has 3 apples and 6 peaches.

# 8
print("Anna has {0:5} apples and {1:3} peaches.".format(3, 6))
# Anna has     3 apples and   6 peaches.

# 9
app = 3
pch = 6
print(f"Anna has {app} apples and {pch} peaches.")
# Anna has 3 apples and 6 peaches.

# 10
print("Anna has %d apples and %d peaches." % (app, pch))
# Anna has 3 apples and 6 peaches.

# 11
anna_dict={'three': app, 'six': pch}
print("Anna has %(three)d apples and %(six)d peaches." % anna_dict)
# Anna has 3 apples and 6 peaches.

# 12
lst = []
for num in range(10):
    if num % 2 == 1:
        lst.append(num ** 2)
    else:
        lst.append(num ** 4)
print(lst)
# [0, 1, 16, 9, 256, 25, 1296, 49, 4096, 81]
lst_comp = [num ** 2 if num % 2==1 else num ** 4 for num in range (10)]
print(lst_comp)
# [0, 1, 16, 9, 256, 25, 1296, 49, 4096, 81]

# 13
# list_comprehension = [num // 2 if num % 2 == 0 else num * 10 for num in range(10)]
lst = []
for num in range (10):
    if num % 2 == 0:
        lst.append(num // 2)
    else:
        lst.append(num * 10)
print(lst)
# [0, 10, 1, 30, 2, 50, 3, 70, 4, 90]

# 14
# d = {}
# for num in range(1, 11):
#     if num % 2 == 1:
#         d[num] = num ** 2
# print(d)
dict_comp = {num: num ** 2 for num in range(1, 11) if num % 2 == 1}
print(dict_comp)
# {1: 1, 3: 9, 5: 25, 7: 49, 9: 81}

# 15
# d = {}
# for num in range(1, 11):
#     if num % 2 == 1:
#         d[num] = num ** 2
#     else:
#         d[num] = num // 0.5
# print(d)
dict_comp = {d: d ** 2 if d % 2 == 1 else d // 0.5 for d in range(1, 11)}
print(dict_comp)
# {1: 1, 2: 4.0, 3: 9, 4: 8.0, 5: 25, 6: 12.0, 7: 49, 8: 16.0, 9: 81, 10: 20.0}

# 16
# dict_comprehension = {x: x**3 for x in range(10) if x**3 % 4 == 0}
x = {}
for num in range (10):
    if num % 4 == 0:
        x[num] = num ** 3
print(x)
# {0: 0, 4: 64, 8: 512}

# 17
# dict_comprehension = {x: x**3 if x**3 % 4 == 0 else x for x in range(10)}
x = {}
for num in range (10):
    if num % 4 == 0:
        x[num] = num ** 3
    else:
        x[num] = num
print(x)
# {0: 0, 1: 1, 2: 2, 3: 3, 4: 64, 5: 5, 6: 6, 7: 7, 8: 512, 9: 9}

# 18
# def foo(x, y):
#     if x < y:
#         return x
#     else:
#         return y
foo = lambda x, y: x if x < y else y
print(foo)
#<function <lambda> at 0x7f7d71e7c0d0>

# 19
# foo = lambda x, y, z: z if y < x and x > z else y
def foo(x, y, z):
    if y < x and x > z:
        return z
    else:
        return y
print(foo)
#<function foo at 0x7f88925eb160>

# 20
lst_to_sort = [5, 18, 1, 24, 33, 15, 13, 55]
print(sorted(lst_to_sort))
#[1, 5, 13, 15, 18, 24, 33, 55]

# 21
print(sorted(lst_to_sort, reverse=True))
#[55, 33, 24, 18, 15, 13, 5, 1]

# 22
print(list(map(lambda x: x *2, lst_to_sort)))
# [10, 36, 2, 48, 66, 30, 26, 110]

# 23
list_A = [2, 3, 4]
list_B = [5, 6, 7]
list_C = []
list_C = (list_A[0]**list_B[0], list_A[1]**list_B[1], list_A[2]**list_B[2])
print(list_C)
# (32, 729, 16384)

# 24
lst_sum = functools.reduce(lambda a, b: a + b, lst_to_sort)
print(lst_sum)
# 164

# 25
print(list(filter(lambda x: (x % 2 == 1), lst_to_sort)))
# [5, 1, 33, 15, 13, 55]

# 26
print(list(filter(lambda x: x < 0, range(-10, 10))))
# [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1]

# 27
list_1 = [1,2,3,5,7,9]
list_2 = [2,3,5,6,7,8]
print(list(filter(lambda x: x in list_1, list_2)))
# [2, 3, 5, 7]