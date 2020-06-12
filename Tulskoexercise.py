#Exercise#18..take argv arguments and add 2 digits.
'''
import sys

a = int(sys.argv[1])
b = int(sys.argv[2])

print(a+b)

'''

#Exercise #19.. if else for odd numbers and elif for 1,2,3,4
'''
x = int(input("Enter a number"))

if x % 2 == 0:
    print("Even")
    if x > 5:
        print("Great")
    else:
        print("Not great")
else:
    print("Number is Odd")

if x == 1:
    print("One")

elif x == 2:
    print("Two")
elif x == 3:
    print("Two")
elif x == 4:
    print("Four")
'''

#Exercise 20..Use while loop and print Mahad boy boy boy boy 5 times
'''
i=1
while i<=5:
    j = 1
    print("Mahad ",end="")
    while j<=5:
        print("boy",end=" ")
        j+=1
    print()
    i+=1
'''
#Exercise 21..Use for loop and print a range and a list
'''
for i in range(10):
    print(i,end=" ")
print()
lst=[5,10.6,"Mahad"]
for i in lst:
    print(i,end=" ")
'''
#Exercise 22..Use while loop a vending machine with 10 candies and user asks for 15 after 10 show out of stock and exit.
'''
n = int(input("Number of candies you want"))
total = 10
i = 0
while i < total:
    print("Take candy")
    i = i+1
    n = n-1
print("We are out of Stock")

print("You did not get %d candie" % n)
print("You did not get candies",n)

'''


#Exercise 23..use for loop and print #### and # and ####
                                     ###      ##    ####
                                     ##       ###   ####
                                     #        ####  ####
'''
for i in range(4):
    for j in range(4-i):
        print("#",end="")
    print()
'''
#Exercise 24: [12,13,17,14,19] if num%5==0 not found printed.
'''
x=[12,13,17,15,19]
for i in x:
    if(i%5==0):
        print("Found")
        break
else:
    print("Not Found")
'''
#Exercise 25: code for prime numbers
'''
n=int(input("Number to check: "))

if(n==0 or n==1):
    print("Not prime")
else:

    for i in range(2,n):
        if n%i==0:
            print("Not prime")
            break
    else:
        print("Prime")

'''
#Exercise 26: Arrays, Create an integer array and then create a new one to store its squares. and print squares.
'''
import array as ar
arr=ar.array('i',[10,15,20])
arr2=ar.array(arr.typecode,[a*a for a in arr])
for i in arr2:
    print(i,end=" ")
'''
#Exercise 27: Create an array of size n, add n values and then search for element and its index too with k-=0 and index method.
'''
n=int(input("Size of array"))
import array as ar
arr = ar.array('i', [])

for i in range(n):
    num=int(input("Enter the number you want"))
    arr.append(num)

print(arr)

snum=int(input("Number you want to search"))

index = 0
for i in range(len(arr)):
    
    if arr[i] == snum:
        print("Found at %d index " % index)
        break
    index = index + 1

else:

    print("Not Found")
'''
#Exercise 28: Create a 2 dimentional Array
'''
from numpy import array

x= array([[5,7,9,11],[4,6,7,8]])
print(x)
'''
#Exercise 29: Initialize array using array, linspace, logspace, arange, zeros and ones.
'''
from numpy import *

x= linspace(5,15,11)
print(x)
y=logspace(5,15,11)
print(y)
z=arange(10,20,3)
print(z)
a=zeros(5,float)
print(a)

'''
#Exercise 30:copy array deep and shallow.
'''
from numpy import *
x=array([5,7,8])
x[1]=13
y=x.copy()
print(y)
z=x.view()
print(z)
'''

#Exercise 31: Use numpy to crate a 2 dimentional array, flatten it, create 3D, muliply 2 matrix
'''
from numpy import *
x=array([[4,5,6],[7,8,9]])
z=array([[1,2,3],[3,4,5],[5,6,7]])
print(x)
print(x.flatten())
print(x.ndim)
print(x)
y=x.reshape(3,2,1)
print(y)
print(matrix(x)*matrix(z))
'''
#Exercise 32: Create a function add_sub, take 2 values and return add and sub
'''
def add_sub(x,y):
    add =x + y
    sub=x-y
    return add,sub
x=15
y=10
a,b=add_sub(x,y)
print("add is {} and sub is {} ".format(a,b))
'''
#Exercise 33:  create a function, pass a value and list and print the ids in the update function and main
'''
def update(x):
    print(x,id(x))
y=update(15)
print(y,id(y))
'''
#Exercise 34: crate sum function that should display output on variable length arguments

'''
def sum(*args):
    result=0
    for i in args:
        result+=i
    return result

print(sum(5,7,9))
'''

#Exercise 35: crate a person with variable length kw argumets and print key value pair
'''
def person(**data):
    #print(name)
    print(data)

    for (i,j) in data.items():
        print(i,j)

person(name='Qamar',age=32,status='married',city='Hbd')
'''
#Exercise 36: update a value in function using gloabl and globals method.
'''
x=10
def update():

    globals()['x']=8
    print("Inside the function value of x is {}".format(x))

update()
print ("outside function value of x is {}".format(x))
'''
#Exercise 37: pass a list to function and return number of evens and odds.
'''
def evensAndOdds(x):
    even, odd = 0, 0
    evens, odds = [], []
    for i in x:
        if i%2 == 0:
            even += 1
            evens.append(i)
        else:
            odd += 1
            odds.append(i)
    print([i for i in evens])
    for i,val in enumerate(odds):
        print(i,val)

    return even, odd

x=[12,37,45,67,44,56,75,66]
e, o = evensAndOdds(x)

print("Evens: {} \nOdds:{}".format(e, o))
'''

#Exercise 37-1: pass a list user input ten times and return names having less than 6 characters.
'''

def lessThan6(x):
    total=0
    for i in x:
        if len(i)<6:
            total+=1
        else:
            pass
    return total


user = []
for i in range(5):
    x=input("Enter the name")
    user.append(x)


print("Total less than 6 are {}".format(lessThan6(user)))
'''
#Exercise 38: print fibbonoci number using for loop in fib function
'''
def fib(x):
    fiblist=[]
    first=0
    second=1
    fiblist.append(first)
    fiblist.append(second)
    if(x>1):
        for i in range(2,x):
            num=first+second
            fiblist.append(num)
            first,second=second,num
        return fiblist,num

def fib1(x):
    first=0
    second=1
    if(x>1):
        for i in range(2,x):
            num=first+second
            first,second=second,num
            if(num>x):
                break
        return first

x=int(input("How many fib seq you want: "))
y=int(input("Last fib number less than the number provided"))
l,num1=fib(x)
number=fib1(y)

print(l)
#print("{}th Fib is {} ".format(x,num1))
print("Number is",number)

'''

#Exercise 38-1: print fibbonoci number the last number less than our input, not the whole n fib.
#done above
#Exercise 39: print factorial function using for loop
'''
def fact(x):
    result=1

    if x>2:
        for i in range(2,x+1):
            result=result*i
    return result

x=int(input("Number you want factoril: "))
print("{}! ={} ".format(x,fact(x)))
'''

#Exercise 40: create a greet function and call it recursively and also
'''
import sys
def greet():
    print("Greeting")
    greet()


print(sys.getrecursionlimit())
greet()
'''
# ..print the recusrion limit after updating it to 2000. done
##Exercise 41: factoeial function using Recursion
'''
def fact(n):
    if n==1:
        return 1
    else:
        return n*fact(n-1)

print(fact(3))
'''
#Exercise 42: Implement a lambda function f for square and one for add fadd.
'''
def square(n):
    return n*n

n=int(input("Enter the number: "))
f=lambda n:n*n
print("n square is ",f(n))
'''
#Exercise 43-1: Use filter on list to get evens in the list using def and lambda.
'''
def evens(n):
    x=[]
    for i in n:
        if i%2==0:
            x.append(i)
    return x

x=[12,15,17,19,22,45,66]
print(list(filter(lambda x:x%2==0,x)))
'''
#Exercise 43-2: Use map on the above evens using def update and lamda.
'''
def evens(n):
    x = []
    for i in n:
        if i % 2 == 0:
            x.append(i)
    return x

x = [12, 15, 17, 19, 22, 45, 66]
y=list(filter(lambda x: x % 2 == 0, x))
print(y)
print(list(map(lambda a:a*a,y)))
'''
#Exercise 43-3: Extend the above double using reduce find sum whille use def sum and lambda.
'''
import functools
x = [12, 15, 17, 19, 22, 45, 66]
y=list(filter(lambda x: x % 2 == 0, x))
print(y)
print(list(map(lambda a:a*a,y)))
print(functools.reduce(lambda a,b:a+b,y))d
'''
#Exercise 44: using decorator smart_div, extend div where numerator is always big number.

'''

def smart_div(func):
    def inner(a,b):
        if a<b:
            a,b=b,a
        return func(a,b)
    return inner

@smart_div
def div(a,b):
    return a/b

print(div(2,5))

'''

#Exercise45:  Write module add,sub, div and use it in aother file.
'''
from TestSystem import add
print(add(5,6))
'''
#Exercise 46: use __name__ and put it in if statement, print only if you are in main.
'''
if __name__=='__main__':
    print("In main")
else:
    print("Not in main")
'''
#Exercise 47: file 1 is demo where func1 and func 2 have print statemens. Add file is another file that has sum and sub
#..method now from file 1 print fun1, fun2 and sum method only.

#Exercise 49: Create a class with name Computer and define a method config and print this method in main.
#Exercise 50: extend computer class by def init and add ram and cpu in init and print in config method.
#Exercise 51:class person has name and age defined in init method no write a compare method in class to compare the age of c1 and c2.
#Exercise 52:def a class car  and def mil and comp as instance variable and wheel as class variable, now change variables.
#Exercise 53:def a class student and pass m1,m2,m3 in init and calulcat the averga of each student now print school name as class method and
#...info as a static method.
#Exercise 54: craete a class Student with attribute name and roll nuber.Now an inner class laptop with cpu and RAM and show method for
# both classes should should show info.
#Exercise 55: Create a class A with 2 methods feature1, feature2 now a child class B with 2 additional feature 3,4 and access them all.
#Exercise 56:Craete a class A with feature 1 and feature 2, now class B extend A and C extend A,B. how init behave when Method Resolitoon order behaves how.
#Exercise 58: Duck typing Polymorphism: Create a class Laptop and pass ide object of class Pycharm and Editor and call execute method with ide object from pycharm and Myeditor.
#Exercise 59:Operator overloading: m1,m2 are 2 attributs of class Student. Now do S3=s2+s1 by operaor overloading of __add__. override the gt to get s1 wins and
#override __str__to get s1 in tuple instead of address.
#Exercise 60: class A has show method class B extends class A and has the same method now call the method using object of these class B.
#Exercise 60 Craeate an abstract class Computer and abstract method process and implememt it in laptop and print it from another method.
#Exercise 61: Iternator: Create a class  and def __iter__ and __Next__ to print top 10 vals.
#Exercise 62: Gnerator: print square of top 10 using yield in def TopTenSquare method.
#Exercise 63: exception: divide by zero and p as integer put in try and print exception in except.
#Exercise 64:Theading: Create two classes Hello and Hi print 5 times in parallel tjreads and print bye once the t1,t2 joins back.
#Exercise 65: File Handling. open a file and read it and write it in other file.
# #Exercise 66: comments done
# #Exercise 68:Linear Search. Define a method search and pass a list and number and found with index or not found.
# #Exercise 69: Binary Search: def a binay search method and find number using lower, mide and upper.
# #Exercise 70:Bubble sort: define a sort method that takes a list as an input.
#Exercise 71:Selection sort
#Exercise 72: SQL: mysql.connector, fetch data from student table and mydb is database name
#Exercise 74: Zip method: Create 2 tuples with name and comps, now zip them and print the zipped in list or a,b format.
#Exercise75:  Create 2 sockets,serve and clinet and send a packet from server and clinet and print it.
#Exercide 76: Anaconda:



