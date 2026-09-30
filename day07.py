# # Set Methods 
# #add 
s = set()
s.add(1)
s.add(1.6)
s.add(2+3j)
s.add(True)
s.add(None)
#s.add([1,2,3])#error
s.add((4,5,6))
#s.add({7,8,9})#error
#s.add({10:'a', 11:'b', 12:'c'})#error
s.add('rakesh')
s.add(range(13,16))
print(s)#{range(13, 16), 1, 1.6, (2+3j), None, 'rakesh', (4, 5, 6)}

# #update
s = set()
# #s.update(1)#error
# #s.update(1.6)#error
# #s.update(2+3j)#error
# #s.update(True)#error
# #s.update(None)#error
s.update([1,2,3])
s.update((4,5,6))
s.update({7,8,9})
s.update({10:'a', 11:'b', 12:'c'})
s.update('rakesh')
s.update(range(13,16))
print(s)#{1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 'r', 's', 'h', 'a', 'e', 'k'}

# #pop
s = {1,4,3,2,5,6,7,9}
print(s)#{1, 2, 3, 4, 5, 6, 7, 9}
a = s.pop() 
print(a, s)#1 {2, 3, 4, 5, 6, 7, 9}
b = s.pop() 
print(b, s)#2 {3, 4, 5, 6, 7, 9}
#c = s.pop(3)#error
#print(c, s)

# #remove
s = {4,3,2,5,8}
a = s.remove(8)
print(a, s)#None {2, 3, 4, 5}
b = s.remove(9)
print(b, s)

# # discard
# s = {4,3,2,5,8}
# a = s.discard(8)
# print(a, s)#None {2,3,4,5}
# b = s.discard(9)
# print(b, s)#None {2,3,4,5}

# # clear
#s = {4,3,5,2,1}
#a = s.clear()
#print(a, s)#None set()

# # union, intersection, differece, symmetric_difference
# s = {1,2,3,4}
# l = [3,4,5,6]
# t = (3,4,5,6)
# s2 = {3,4,5,6}
# d = {3:'c', 4:'d', 5:'e', 6:'f'}
# r = range(3,7)
# w = '3456'
# print('Union:', s.union(l))#Union: {1, 2, 3, 4, 5, 6}
# print('Intersection:', s.intersection(t))#Intersection: {3, 4}
# print('Difference:', s.difference(s2))#Difference: {1, 2}
# print('Symmetric Difference:', s.symmetric_difference(d))#Symmetric Difference: {1, 2, 5, 6}
# print('Union:', s.union(w))#Union: {'3', 1, 2, 3, 4, '6', '5', '4'}
# print('Union:', s.union(r))#Union: {1, 2, 3, 4, 5, 6}


# # Dict Methods 
d = {}
#d.update(5)#error
#d.update(5.4)#error
#d.update(4+5j)#error
#d.update(True)#error
#d.update(None) #error
#d.update([1,2,3])#error
#d.update((4,5,6))#error
#d.update({7,8,9})#error
#d.update('rak')#error
#d.update(range(10, 14))#error
# d.update({10:'j', 11:'k', 12:'l'})
# print(d)#{10: 'j', 11: 'k', 12: 'l'}
# d.update([ [1,'a'], (2,'b'), 'ab' ])
# print(d)#{10: 'j', 11: 'k', 12: 'l', 1: 'a', 2: 'b', 'a': 'b'}
# d.update(( 'ra', 'ke', 'sh' ))
# print(d)#{10: 'j', 11: 'k', 12: 'l', 1: 'a', 2: 'b', 'a': 'b', 'r': 'a', 'k': 'e', 's': 'h'}
# d.update({ (3,'c'), (4,'d') })
# print(d)#{10: 'j', 11: 'k', 12: 'l', 1: 'a', 2: 'b', 'a': 'b', 'r': 'a', 'k': 'e', 's': 'h', 3: 'c', 4: 'd'}

# # #pop 
# d = {3:'c', 2:'b', 1:'a', 4:'d'}
# x = d.pop(2)
# print(x)#b
# #y = d.pop(100)
# #print(y)#error
# z = d.pop(100, -1)
# print(z)#-1

# #popitem
# d = {3:'c', 2:'b', 1:'a', 4:'d'}
# x = d.popitem()
# print(x, d) #(4, 'd') {3: 'c', 2: 'b', 1: 'a'}
# y = d.popitem()
# print(y, d)#(1, 'a') {3: 'c', 2: 'b'}

# #clear
# d = {3:'c', 2:'b', 1:'a', 4:'d'} 
# d.clear() 
# print(d)#{}

# #get 
# d = {3:'c', 2:'b', 1:'a', 4:'d'}
# x = d.get(2)
# print(x, d)#b {3: 'c', 2: 'b', 1: 'a', 4: 'd'}
# y = d.get(100)
# print(y, d)#None {3: 'c', 2: 'b', 1: 'a', 4: 'd'}
# z = d.get(100, -1)
# print(z, d)#-1 {3: 'c', 2: 'b', 1: 'a', 4: 'd'}

# #setdefault
# d = {3:'c', 2:'b', 1:'a', 4:'d'}
# x = d.setdefault(2, 90)
# print(x, d)#b {3: 'c', 2: 'b', 1: 'a', 4: 'd'}
# y = d.setdefault(100)
# print(y, d)#None {3: 'c', 2: 'b', 1: 'a', 4: 'd', 100: None}
# z = d.setdefault(90, -1)
# print(z, d)#-1 {3: 'c', 2: 'b', 1: 'a', 4: 'd', 100: None, 90: -1}
# m = d.setdefault(90, -2)
# print(m, d)#-1 {3: 'c', 2: 'b', 1: 'a', 4: 'd', 100: None, 90: -1}


# #keys, values, items
# d = {3:'c', 2:'b', 1:'a', 4:'d'}
# dk = d.keys()#dict_keys([3, 2, 1, 4]) <class 'dict_keys'
# print(dk, type(dk))
# dv = d.values()#dict_values(['c', 'b', 'a', 'd']) <class 'dict_values'
# print(dv, type(dv))
# di = d.items()# dict_items([(3, 'c'), (2, 'b'), (1, 'a'), (4, 'd')]) <class 'dict_items'
# print(di, type(di))







