#Arithmetic 

# + : 
a = 45 + 4.5
b = True + False 
c = 4+5j + 6+7j
#d = None + 5 
e = [1,2,3] + [4,5,6]
f = (1,2,3) + (4,5,6)
g = "gree"+"shma"
#h = range(1,4) + range(4,7)
#i = {1,2,3} + {4,5,5}
#j = {1:'a', 2:'b'} + {3:'c', 4:'d'}
#k = [1,2,3] + (1,2,3)
#l = [1,2,3] + 'rak'
print(a)#49.5
print(b)#1
print(c)#(10+12j)
#print(d)#error
print(e)#[1,2,3,4,5,6]
print(f)#(1,2,3,4,5,6)
print(g)#greeshma
#print(h)#error
#print(i)#error
#print(j)#error
#print(k)#error
#print(l)#error

# - : 
a = 45 - 5.5
b = 4+5j - 3+2j 
c = True - False 
#d = [1,2,3] - [2,3]
#e = (1,2,3) - (2,3)
f = {1,2,3,4} - {2,1}
#g = {1:'a', 2:'b', 3:'c'} - {2:'b', 3:'c'}
print(a)#39.5
print(b)#(1+7j)
print(c)#1
#print(d)#error
#print(e)#error
print(f)#{3,4}
#print(g)#error

# #* : 
a = 4 * 5.4
b = True * False 
c = (4+5j) * (3+2j)
#d = [1,2,3] * (2,3)
e = [1,2,3] * 3 
#f = [1,2,3] * 3.0
g = (1,2,3) * 3 
h = 'greeshma' * 3 
#i = {1,2,3} * 3 
#j = {1:'a', 2:'b', 3:'c'} * 3
k = [1,2,3]
l = range(1,2,3)
m = (4,5,6)
print(a)#21.6
print(b)#0
print(c)#(2+23j)
#print(d)
print(e)#[1,2,3,1,2,3,1,2,3]
#print(f)#error
print(g)#(1,2,3,1,2,3,1,2,3)
print(h)#greeshmagreeshmagreeshma
#print(i)#error
#print(j)#error
print(*k)#1 2 3
print(*l)#1
print(*m)#4 5 6

# # ** : power 
a = 5 ** 2 
b = 3 ** 2.3
c = (3+4j) ** (1+2j)
print(a)#25
print(b)#12.513502532843182
print(c)#(-0.41981317556195746-0.6604516942073324j)

# # / :
a = 5 / 2     
print(a)#2.5

# # // : 
a = 5 // 2     
print(a) #2
a = 5.5 // 2   
print(a)#2.0

# # % : 
a = 5 % 2 
print(a)#1


# # #Relational Operators 
print(5 == 6.5)#False
print(1 == True)#True
print(2 == None)#False
print(4+5j == 4+6j)#False
print(5 > 6.5)#False
print(1 > True)#Flase
#print(2 > None)#error
#print(4+5j > 3+2j)#error
print([1,2,3] == [1,2,4])#False
print([1,2,3] > [1,3,4])#False
print((1,2,3) > (1,3,4))#Flase
print({1,2,3} > {1,2}) #True
#print({1:2, 2:3} > {3:4, 4:5})
print({1:2, 2:3} == {1:2, 2:3})#True
print([1,2,3] == (1,2,3))#False
#print([1,2,3] > (1,2,3)) #error 

# # #True or False
print(bool(0))    #False
print(bool(4.5))  #True
print(bool(''))   #False
print(bool('r'))  #True
print(bool([]))   #False
print(bool([1]))  #True
print(bool(None)) #False

# print()
# print()
# # #Logical Operators
print( 4 and 0 and 6 )   #0
print( 4 and 1 and 6 )   #6
print( 4 or 0 or 6)      #4
print(0 or '' or [])     #[]
#mixed
print(4 or 0 and 6)      #4
# #not reverse the bool value
print(not False) #True
print(not True)  #False

# #Assignment operators
a = 10 
a += 20
a -= 10
a *= 2 
a **= 2
a /= 2 
a //= 3
a %= 3
print(a)#2.0

# #Identity Operators 
a = 34 
b = 34 
print(a is b) #True
a = 3+4j 
b = 3+4j 
print(a is b) #True
a = [1,2,3]
b = [1,2,3]
print(a is b) #False
a = 'rakesh'
b = 'rakesh'
print(a is b) #True
a = range(1,4)
b = range(1,4)
print(a is b) #False
a = (1,2,3)
b = (1,2,3)
print(a is b) #True
a = {1,2,3}
b = {1,2,3}
print(a is b) #False
print()
print()

# #Membership 
a = [1,2,3,4]
b = {1,2,3,4}
c = 'rakesh'
d = (1,2,3,4)
e = {1:'a', 2:'b', 3:'c'}
f = range(1,4)
print(5 in a)#False
print(3 in b)#True
print('r' in c)#True
print(4 in d)#True
print('b' in e)#False
print(3 in e)#True
print(4 in f)#False

# #Walrus operator
#print(a = 4)
print(a := 4)#4
print(a)#4

# #ternary operator 
a = 5 if 10 > 20 else 6 
print(a)
a = [1,2,3] if 5 < 10 else (1,2,3)
print(a)
