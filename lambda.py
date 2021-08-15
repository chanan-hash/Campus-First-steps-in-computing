import functools

print((lambda x,y: x+y) (2,5))

new_add = lambda x,y : x + y
print(new_add(3,4))

print((lambda y, x: x in y) ([1, 5, 6, 9], 9))
print()

shopping_list = [200, 120, 330, 50]
print(functools.reduce( lambda x, y: x + y , shopping_list))
print()

print("first lambda")

shop_list = [2,4,3,5,6,7]
print(functools.reduce(lambda x,y: x+y,shop_list))

print()
print("second lambda")

my_list = [0,1,2,3,4,5,6,7]
print(list(filter(lambda x : x % 2 ==0,my_list)))

print()
list_of_tuples = [(2,2),(3,4),(4,1),(1,3)]
print(sorted(list_of_tuples,key= lambda x :x[1]))

print()
print("third lambda")
clac_sqrt_list = [lambda x : x**2, lambda x: x**3, lambda x: x**4]
for func in clac_sqrt_list:
    print(func(3))