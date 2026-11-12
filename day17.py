# def add(x, y):         
#     return x + y 
# print(add(10,20))#30       
# print(type(add)) #<class 'function'>      

# a = lambda x,y : x + y   
# print(a(10,20)) #30       
# print(type(a))  #<class 'function'>      

#b = lambda (x,y) : x + y 
#print(b(10,20)) 

#c = lambda x,y : return x + y 
#print(c(10,20))

# lambda function to return the sum of two numbers

add=lambda x,y:x+y#30
print(add(10,20))

# lambda function to return the square of a number

squ=lambda x:x**2
print(squ(5))#25

# lambda function to return the second element of a sequence

second=lambda x:x[1]
print(second([10,20,30,40]))#20



# #tricky
# a = lambda x : print(x+10), print(200), print(300)
# print(a)   # 30 200 300 
# print(type(a)) #(<function <lambda> at 0x000002069AE88FE0>, None, None) #<class 'tuple'>
            
# # #map 
# a = [1,2,3,4,5,6]
# m = map(lambda x : x**2, a) 
# print(m) #<map object at 0x000002666C04B9A0>
# print(type(m))#<class 'map'>
# l = list(m)   #[1,4,9,16,25,36]  
# print(l)

# # #filter 
# a = [1,2,3,4,5,6]
# f = filter(lambda x : x % 2 == 0, a)
# print(f)
# print(type(f))#<class 'filter'>
# l = list(f)#[2,4,6]
# print(l)

# # #reduce 
# import functools 
# l = [1,2,3,4,5]
# r = functools.reduce(lambda x,y : x+y, l) 
# print(r)     #15    
# print(type(r))  #<class 'int'> 



























































