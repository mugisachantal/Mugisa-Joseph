print("Hello, world!")




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




#my real world example 

celsius_readings = [22.5, 23.1, 21.9, 150.0, 24.0, -10.0, 22.8]

# [expression for item in iterable if condition]
fahrenheit_readings_filtered_lc = [
    (celsius * 9/5) + 32
    for celsius in celsius_readings
    if 0 <= celsius <= 100
]

print("Fahrenheit readings (list comprehension):", fahrenheit_readings_filtered_lc)


names=list(('jose','makos','oscar'))
print(len(names))