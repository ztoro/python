# IMMUTABLE

# INT, FLOAT, COMPLEX
print("######INT, FLOAT, COMPLEX######")
my_num = 42.42  # FLOAT
print(id(my_num))
my_num += 5
print(id(my_num))
# Két különböző változó, nem lehet megváltoztatni az értékét!

# BOOLEAN
print("######BOOLEAN######")
my_bool = True
print(id(my_bool))
my_bool = False
print(id(my_bool))

# A BOOLEAN az az INT alosztálya, ugyanúgy nem változtatható!
# Lásd:
bool

# STRING
print("######STRING######")
my_string = "hello world!"
print(my_string)

print("######MUTABLE######")

# TUPLE
print("######TUPLE######")
my_tuple = (True, "This was successful!")

# MUTABLE

# LIST
print("######LIST######")
my_list = ["Tibi", "Gábor"]
my_list.append("Zoli")
print(my_list)
my_list.remove("Zoli")
print(my_list)

print(my_list[0])
# DICTIONARY
print("######DICTIONARY######")
my_dict = {"name": "Tibi", "favourite_colour": "blue"}
# print(my_dict["name"])
# print(my_dict["favourite_colour"])

my_dicts = [{"name": "Tibi",
             "favourite_colour": "blue",
             "occupation": "DevOps Engineer"
             },
            {"name": "Gabor",
             "favourite_colour": "green"}]
for item in my_dicts:
    try:
        print(item["name"])
        print(item["favourite_colour"])
        if "occupation" in item:
            print(item["occupation"])
            if item["occupation"] == "DevOps Engineer":
                print("His occupation is DevOps engineer!")
        else:
            item["occupation"] = "Senior DevOps Engineer"
            print(item["occupation"])
    except KeyError:
        print("cannot find key!")
print(my_dicts)

del my_dict["favourite_colour"] # Deleting a key/value from a dict
print(my_dict)


# SET
print("######SET######")
my_set = {"Tibi", "Gábor"}
my_set.add("Zoli")
print(my_set)
for item in my_set:
    print(item)
print(my_set)
