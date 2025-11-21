# the functions which can use in every datatypes is called as utility functions
# like id(),type(),print(),input(),len() etc

# functions on string
a = "hello world"
print(a.capitalize())
print(a.upper())
print(a.lower())
print(a.count("o"))
print(a.find("world"))
print(a.replace("world", "there"))
print(a.split(" "))

# functions on list
my_list = [1, 2, 3, 4, 5]
my_list.append(6)
print(my_list)
my_list.remove(3)
print(my_list)
my_list.reverse()
print(my_list)
my_list.sort()
print(my_list)
print(len(my_list))
print(max(my_list))
print(min(my_list))
print(sum(my_list))
print(my_list.index(4))
print(my_list.count(2))
my_list.insert(2, 10)

# functions on dictionary
my_dict = {"a": 1, "b": 2, "c": 3}
print(my_dict.keys())
print(my_dict.values())
print(my_dict.items())
my_dict.update({"d": 4})
print(my_dict)
my_dict.pop("b")
print(my_dict)
print(len(my_dict))
print(my_dict.get("a"))
my_dict.clear()
print(my_dict)

# functions on set
my_set = {1, 2, 3, 4, 5}
my_set.add(6)
print(my_set)
my_set.remove(3)
print(my_set)
my_set.clear()    
print(my_set)
print(len(my_set))
print(4 in my_set)
another_set = {4, 5, 6, 7, 8}
print(my_set.union(another_set))
print(my_set.intersection(another_set))
print(my_set.difference(another_set))
print(my_set.symmetric_difference(another_set))
print(my_set.issubset(another_set))
print(my_set.issuperset(another_set))
print(my_set.isdisjoint(another_set))

# functions on tuple
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple.count(2))
print(my_tuple.index(4))
print(len(my_tuple))
print(max(my_tuple))
print(min(my_tuple))
print(sum(my_tuple))
print(3 in my_tuple)
print(my_tuple[2])
print(my_tuple[1:4])
print(my_tuple[::-1])
new_tuple = my_tuple + (6, 7, 8)
print(new_tuple)
repeated_tuple = my_tuple * 2
print(repeated_tuple)
for item in my_tuple:
    print(item)