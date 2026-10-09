#FOR LOOP PROBLEMS
#basic understanding
#1. print numbers from 1 to 10 in one line

# for i in range(1,11):
#    print(i)#1 2 3 4 5 6 7 8 9 10

# #2. print even numbers from 5 to 30 in one line

# for i in range(5,31):
#    if i%2==0:
#        print(i)#6 8 10 12 14 16 18 20 22 24 26 28 30

# #3. print odd numbers from 5 to 30 in one line

# for i in range(5,31):
#    if i%2!=0:
#        print(i)#5 7 9 11 13 15 17 19 21 23 25 27 29 

# #4. print numbers divisible by 5 from 1 to 30 in one line

# for i in range(1,31):
#    if i%5==0:
#        print(i)# 5 10 15 20 25 30

# #5. print numbers divisible by both 5 and 7 from 1 to 100 in one line

# for i in range(1,101):
#    if i%5==0 and i%7==0:
#        print(i,end=" ")# 35 70

# #6. sum of numbers from 10 to 25 

# sum=0
# for i in range(10,26):
#    sum+=i
# print(sum) #280
   
# #7. sum of numbers in any list

# num=[10,20,30,40,50]
# sum=0
# for i in num:
#     sum+=i
# print(sum)#150

#8. multiplication table of a number 

#n=int(input("enter num:"))
#for i in range(1,11):
 #  print(n*i)#2 4 6 8 10 12 14 16 18 20

#interview problems
#9. factorial 

# n=int(input())#5
# fact=1
# for i in range(1,n+1):
#    fact*=i
# print(fact)#120 

# #10. fibonacci 

# n=int(input())#7
# a,b,=0,1
# for i in range(n):
#    print(a,end=" ")
#    a,b=b,a+b#0 1 1 2 3 5 8 

# #11. reverse a string

# a="greeshma"
# b=a[::-1]
# print(b)# amhseerg

# # 12. count vowels in a string

# s=input()#pavani
# count=0
# for ch in s:
#    if ch in "aeiouAEIOU":
#       count+=1
# print(count)#3

# # 13. count z's and y's in a string

# s=input()#zoya is a lazy girl
# z=0
# y=0
# for ch in s:
#    if ch=='z':
#       z+=1
#    elif ch=='y':
#       y+=1
# print('z:',z)#1
# print('y:',y)#6

# # 14. check whether a number is prime number or not 

# n = int(input())#7
# count = 0

# for i in range(1, n + 1):
#     if n % i == 0:
#         count += 1

# if count == 2:
#     print("Prime")#prime
# else:
#     print("Not Prime")

# # WHILE LOOP PROBLEMS
# # basic understanding
# # print 1 to 10 with while loop

# i=0
# while i<10:
#    i=i+1
#    print(i)#1 2 3 4 5 6 7 8 9 10

# #print even numbers from 1 to 10

# i=2
# while i<=10:
#     i=i+2
#     print(i)2 4 6 8 10 12 14 16 18 20

# #print numbers divisible by both 5 and 7 from 1 to 500 

# i=1
# while i<=500:
#    if i%5==0 and i%7==0:
#        print(i)
#    i=i+1#35 70 105 140 175 210 245 280 315 350 385 420 455 490
        
# # interview problems
# # count digits

# n = int(input())#785465

# count = 0

# while n > 0:
#     count += 1
#     n //= 10

# print(count)#6

# # reverse a number

# n = int(input())#123456789

# rev = 0

# while n > 0:
#     digit = n % 10
#     rev = rev * 10 + digit
#     n //= 10

# print(rev)#987654321

# # palindrome number 

# n = int(input())#12321

# original = n
# rev = 0

# while n > 0:
#     digit = n % 10
#     rev = rev * 10 + digit
#     n //= 10

# if original == rev:
#     print("Palindrome")#palindrome
# else:
#     print("Not Palindrome")

# # palindrome string (without slicing, built in function)

# s = input()#level

# rev = ""

# for ch in s:
#     rev = ch + rev

# if s == rev:
#     print("Palindrome")#palindrome
# else:
#     print("Not Palindrome")

# # armstrong number

n = int(input())

original = n
digits = len(str(n))
sum = 0

while n > 0:
    digit = n % 10
    sum += digit ** digits
    n //= 10

if original == sum:
    print("Armstrong")
else:
    print("Not Armstrong")