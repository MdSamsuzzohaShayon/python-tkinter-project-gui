# A tuple consists of a number of values separated by commas
# Tuples are immutable:
# but they can contain mutable objects:
# https://docs.python.org/3/tutorial/datastructures.html#tuples-and-sequences

t = 123, 456, 'hello'
print("This is tuples: ", t)
print("First Tuples: ", t[0])

# TUPLES CAN BE NESTED
nestedTuples = 1, 2, 3, (4, 5, 6, ("One", "two", "three"))
print("Nested tuples 👉 ", nestedTuples)

multiObj = ([1, 2, 3], [3, 2, 1])
print("Multiple object 👉 ", multiObj)

print("▶️▶️▶️▶️▶️▶️")
fruits = ("Apple", "Banana", 'Guava', "papaya", "pineapple", "cherry")

i = 0
while i < len(fruits):
    print("Looping 👉 ", fruits[i])
    i += 1

# UNPACKING TUPLES
# (Apple, Banana, Guava) = fruits
# print("Apple 👉 ",Apple)
print("Assign the rest of the values as a list called red ▶️")
# Assign the rest of the values as a list called "red"
(Banana, Guava, *red) = fruits
print(red)
print('▶️ ▶️ ▶️ ▶ ️▶ ️')
# To join two or more tuples you can use the + operator:

join_tuples = fruits + t
print("Join 👉 ", join_tuples)
mul_tuples = fruits * 2
print("multiply 👉 ", mul_tuples)
