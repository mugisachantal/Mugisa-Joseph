



def ListManipulaytion():
    # 1.Creating a list of 5 items (names of people) and write  outputing the 2nd item.
    names = ["Alice", "Bob", "Charlie", "David", "Eve"]
    print("Second Item: "+names[1])
    # 2.Changing the value of the first item to a new value
    names[0] = "Frank"
    print(names)
    # 3.Adding a sixth item to the list
    names.append("Grace")
    print(names)
    # 4.Adding “Bathel” as the 3rd item in your list
    names.insert(2, "Bathel")
    print(names)
    # 5.Removing the 4th item from the list
    del names[3]
    print(names)
    # 6.Using negative indexing to print the last item in your list
    print(names[-1])
    # 7.Creating a new list with 7 items and using a range of indexes to print the 3rd, 4th and 5th items.
    my_list = [10, 20, 30, 40, 50, 60, 70]
    print(my_list[2:5])
    # 8.Creating a list of countries and make a copy of it.
    countries = ["USA", "Canada", "Mexico", "Brazil", "Argentina"]
    countries_copy = countries.copy()
    print(countries_copy)
    # 9. looping through the list of countries
    countries = ["USA", "Canada", "Mexico", "Brazil", "Argentina"]
    for country in countries:
        print(country)
    # 10.Creatinga list of animal names and sort them in both descending and ascending order.
    animals = ["Lion", "Zebra", "Elephant", "Giraffe", "Antelope", "Bear"]

    # Ascending order
    animals.sort()
    print("Ascending order:", animals)

    # Descending order
    animals.sort(reverse=True)
    print("Descending order:", animals)
    # 11. Outputing only animal names with the letter ‘a’ in them
    for animal in animals:
        if 'a' in animal.lower(): # .lower() to check for both 'a' and 'A'
            print(animal)
            
    # 12.Creating two lists, one containing first names and the other second names and Joining the two lists.
    first_names = ["John", "Jane", "Peter"]
    second_names = ["Doe", "Smith", "Jones"]

    full_names = first_names + second_names
    print(full_names)



def tuppleManipulation():
    # 1. Outputting your favorite phone brand
    x = ("samsung", "iphone", "tecno", "redmi")
    favorite_brand = x[0] # Assuming "samsung" is the favorite
    print("My favorite phone brand is: " + favorite_brand)

    # 2. Using negative indexing to print the 2nd last item
    x = ("samsung", "iphone", "tecno", "redmi")
    print("The 2nd last item is: " + x[-2])

    # 3. Updating "iphone" to "itel"
    phones = ["samsung", "iphone", "tecno", "redmi"] 
    phones[1] = "itel"
    print(phones)

    # 4. Adding "Huawei" to your tuple 
    x = ("samsung", "iphone", "tecno", "redmi")
    x_list = list(x)
    x_list.append("Huawei")
    x = tuple(x_list)
    print(x)

    # 5. Looping through the tuple
    x = ("samsung", "iphone", "tecno", "redmi")
    for brand in x:
        print(brand)

    # 6. Removing/deleting the first item in your tuple 
    x = ("samsung", "iphone", "tecno", "redmi")
    x_list = list(x)
    del x_list[0]
    x = tuple(x_list)
    print(x)

    # 7. Creating a tuple of cities in Uganda using the tuple() constructor
    cities_in_uganda = tuple(["Kampala", "Entebbe", "Jinja", "Mbarara", "Gulu"])
    print(cities_in_uganda)

    # 8. Unpacking tuple
    x = ("samsung", "iphone", "tecno", "redmi")
    (brand1, brand2, brand3, brand4) = x
    print("Brand 1:", brand1)
    print("Brand 2:", brand2)
    print("Brand 3:", brand3)
    print("Brand 4:", brand4)

    # 9. Using a range of indexes to print the 2nd, 3rd and 4th cities
    cities_in_uganda = ("Kampala", "Entebbe", "Jinja", "Mbarara", "Gulu")
    print(cities_in_uganda[1:4])

    # 10. Joining two tuples (first names and second names)
    first_names = ("Alice", "Bob", "Charlie")
    second_names = ("thor", "son", "kevinn")
    full_names = first_names + second_names
    print(full_names)

    # 11. Creating a tuple of colors and multiplying it by 3
    colors = ("red", "green", "blue")
    multiplied_colors = colors * 3
    print(multiplied_colors)

    # 12. Returning the number of times 8 appears in this tuple
    my_tuple = (1, 8, 3, 8, 5, 8, 9)
    count_of_8 = my_tuple.count(8)
    print("The number 8 appears", count_of_8, "times.")
    
    
    

def setManipulation():
    # 1. Creating a set of 3 of  favorite beverages using the set() constructor
    favorite_beverages = set(("coffee", "tea", "water"))
    print(favorite_beverages)

    # 2. Adding 2 more items to the beverages set
    favorite_beverages.add("juice")
    favorite_beverages.add("soda")
    print(favorite_beverages)

    # 3. Checking if "microwave" is present in the set
    mySet = {"oven", "kettle", "microwave", "refrigerator"}
    if "microwave" in mySet:
        print("Microwave is present in the set.")
    else:
        print("Microwave is not present in the set.")

    # 4. Removing "kettle" from the set
    mySet = {"oven", "kettle", "microwave", "refrigerator"}
    mySet.remove("kettle")
    print(mySet)

    # 5. Looping through the set
    mySet = {"oven", "kettle", "microwave", "refrigerator"}
    for item in mySet:
        print(item)

    # 6. Adding elements from a list to elements in a set
    my_set = {"apple", "banana", "cherry", "date"}
    my_list = ["grape", "kiwi"]
    my_set.update(my_list)
    print(my_set)

    # 7. Joining two sets (ages and first names)
    ages = {25, 30, 22}
    first_names = {"john", "jesse", "lee"}
    combined_set = ages.union(first_names)
    print(combined_set)


def stringManipulation():
    # 1. Declaring two variables (integer and string) and concatenating them
    my_integer = 10
    my_string = "Hello"
    concatenated_string = my_string + str(my_integer)
    print(concatenated_string)

    # 2. Outputting the string without spaces at the beginning, in the middle and at the end
    txt = "     Hello,       Uganda!       "
    output_string = txt.replace(" ", "").replace(",", "").strip()
    print(output_string)

    # 3. Converting the value of 'txt' to uppercase
    txt = "     Hello,       Uganda!       "
    uppercase_txt = txt.upper()
    print(uppercase_txt)

    # 4. Replacing character 'U' with 'V' in the string
    txt = "     Hello,       Uganda!       "
    replaced_txt = txt.replace("U", "V")
    print(replaced_txt)

    # 5. Returning a range of characters in the 2nd, 3rd and 4th position
    y = "I am proudly Ugandan"
    range_of_characters = y[1:4]
    print(range_of_characters)

    # 6. Correcting the given code
    x = "All \"Data Scientists\" are cool!"
    print(x)
    
    
def dictionaryManupilation():
    # 1. Printing the value of the shoe size from the dictionary
    Shoes = {
        "brand" : "Nick",
        "color" : "black",
        "size" : 40
    }
    print(Shoes["size"])   


#ListManipulaytion()
#tuppleManipulation()
#stringManipulation()
dictionaryManupilation()
