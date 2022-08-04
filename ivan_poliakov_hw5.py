'''Задача 1. 10 баллов'''

print('TASK 1:')
password = input('fill your password \n')
password_repeat = input('please, repeat your password \n')
if password == password_repeat:
    print('welcome')
else:
    print('please, try again')


'''Задача 2. 5 баллов'''

print('TASK 2:')
data = ['bear', 'milk', 'eg', 'eg', 'eg', 'eg']
eg = 'eg'
while eg in data:
    data.remove(eg)
print(data)


'''Задача 3. 10 баллов'''

print('TASK 3:')
numbers = input('print numbers')
numbers = numbers.split(", ")
for i in numbers:
    i = int(i)
    while i % 2 == 0:
        print("all numbers are even")
        break
    else:
        print('NO')
        break


'''Задача 4. 25 баллов'''

print('TASK 4:')
metods: list = dir(set)
new_methods: list = []
for i in metods:
    for j in i:
        if j.isalpha():
            new_methods.append(i)
            break
        else:
            break
print(new_methods)

''' Задача 5. 15 баллов'''

# https://realpython.com/quizzes/python-lists-tuples/results/?t=eyJjIjo2LCJuIjoxMSwicSI6Nywic2lnIjoibGIkVUh4NSoldjN1ZHxyQyVncjs3Z3Y1TTZ1QXF3TFRFbnVEeXp-PyIsInQiOjQwMiwidiI6M30=&s=1
# https://realpython.com/quizzes/python-sets/results/?t=eyJjIjo5LCJuIjoxMCwicSI6MTEsInNpZyI6ImUhcC1-OGdAZzskWTVFTko7YEtfYWVHUy1kQGRGaXAwU3AtPl83LUQiLCJ0IjoxMDQsInYiOjN9&s=1

'''Задача 6. 5 баллов'''

print('TASK 6:')
set_method: set = {"1", "2", "3"}
set1: set = {'a'}
set2: set = {'1', 'b', 'c'}
set3: set = {'2', 'c', '1'}
#add
set_method.add('4')
print('add: ', set_method)
#update
set_method.update(set1)
print('update: ', set_method)
#remove
set_method.remove('a')
print('remove: ', set_method)
#discard
set_method.discard('4')
print('discard: ', set_method)
#pop
set_method.pop()
print('pop: ', set_method)
#union
print('union: ', set_method.union(set2, set3))
#intersection
set_method.intersection(set2, set3)
print('intersection: ', set_method)
#difference
print('difference: ', set_method.difference(set2, set3))
#isdisjoint
set_method.isdisjoint(set2)
print('isdisjoint: ', set_method)
#issubset
set_method.issubset(set2)
print('issubset: ', set_method)
#clear
set_method.clear()
print('clear: ', set_method)


'''Задача 7. 25 баллов'''

print('TASK 7:')
frozenset_1 = frozenset('Hello')
counter = 0
for l in frozenset_1:
    counter = counter+1
print(counter)
