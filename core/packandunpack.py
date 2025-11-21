def func(*args, **kwargs): 
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)

func(1, 2, 3, name="Alice", age=30)
# here the *args packs all positional arguments into a tuple so it's another name is tuple paacking or single packing
# and **kwargs packs all keyword arguments into a dictionary

# Unpacking example
numbers = [4, 5, 6]
def add(a, b, c):
    return a + b + c
result = add(*numbers)  # Unpacking the list into individual arguments
print("Sum:", result)