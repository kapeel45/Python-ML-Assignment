# Addresss of a and b is same because both are pointing to same object in memory. In python, small integers are cached and reused, so when you assign the value 10 to both a and b, they both reference the same integer object in memory.

a = 10
b = 10

print("a Type is ::", type(a))
print("a Address is ::", id(a))

print("b Type is ::", type(b))
print("b Address is ::", id(b))

print(id(a), id(b))   # same id
print("Check Addresses :: ",a is b)         # True
print("Check Value :: ", a == b)         # True

# While, list is mutable object, so when you create two separate lists with the same value, they are stored in different memory locations.
a = [10]
b = [10]

print("a Type is ::", type(a))
print("a Address is ::", id(a))

print("b Type is ::", type(b))
print("b Address is ::", id(b))

print(id(a), id(b))   # often different
print("Check Addresses :: ",a is b)         # often False
print("Check Value :: ", a == b)         # True
