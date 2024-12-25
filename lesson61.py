#Write a program to perform the following operations: 1. Create a tuple with different datatypes 2. Create another tuple of integers 3. Create a new tuple by adding 9 to the previous tuple 4. Count the occurrences of an element in the tuple 5. Perform slicing on the tuple

tuple_1=(1,"student",21.6,True)
print(tuple_1)

tuple_2=(1,2,3,4,5)
print(tuple_2)

tuple_2=tuple_2+(9,)
print(tuple_2)

tuple_3=(10,20,10,30,70,10)
print(tuple_3.count(10))

tuple_4=(1,2,3,4,5,6,7)
print(tuple_4[1:4]) #slicing is done by using index position where [start index:end index+1]