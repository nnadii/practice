import random

# keep practicing python until you are perfect.


def add(a, b):
    return a + b


def square(c):
    return c * c


result = square(add(2, 3))
func = add(2, square(3))

sum = result + func
print(sum)

# module
for x in range(5):
    result = random.randint(1, 6)
    print(result)


try:
    a = 20
    b = 0
    print(a / b)
except ZeroDivisionError:
    # print("Oops, undefined")

    print("Code after handling exception")


# file handling
file = open("file.txt", "r")
content = file.read()
print(content)

# write to file
file = open("file.txt", "w")
file.write("Hello chime, let's take this serious")
file.close()

file = open("file.txt", "r")
content = file.read()
print(content)
file.close()

file = open("file.txt", "w")
file.write("Another line added now")
file.close()

list = [x ** 2 for x in range(10) if x ** 2 % 2 == 0]
print(list)

number = [4, 5, 6]
new_number = "Number:{0},{1},{2}".format(number[0], number[1], number[2])
print(new_number)

# print(":".join(["apple", "mango", "banana"]))
# print("Hello there".replace("there", "world"))

# def add_ten(x):
#     return x + 10


# def twice(func, arg):
#     return func(func(arg))


# print(twice(add_ten, 10))

# new_list = [2, 4, 6, 8, 10]
# print(list(map(lambda x: x ** 2, new_list)))

# filter_list = [1, 3, 4, 5, 67, 7, 8, 30, 41]
# print(list(filter(lambda x: x % 2 == 0, filter_list)))

# Generators
# def odd_numbers(x):
#     for counter in range(x):
#         if counter % 2 == 1:
#             yield counter


# print(list(odd_numbers(20)))

# def even_numbers():
#     counter = 0
#     while counter < 10:
#         yield counter
#         counter += 1


# for x in even_numbers():
#     print(x)

# classes
# class Student:
#     def __init__(self, name, contact):
#         self.name = name
#         self.contact = contact

#     def get_data(self):
#         print("info arriving")
#         self.name = input("Enter your name ")
#         self.contact = input("Enter your contact ")

#     def put_data(self):
#         print("This guy, " + self.name + "has the contact:" + self.contact)


# class First_Student(Student):
#     def __init__(self, age):
#         self.age = age

#     def student_age(self):
#         print(self.age)


# school_age = First_Student(20)
# school_age.student_age()
# school_age.get_data()
# school_age.put_data()

# # factorial


# def factorial(x):
#     if (x == 1):
#         return 1
#     else:
#         return x * (factorial(x - 1))


# print(factorial(5))

# set
# set_a = {1, 2, 3, 4, 5}
# set_b = {4, 5, 6, 7, 8}
# print(set_a & set_b)
