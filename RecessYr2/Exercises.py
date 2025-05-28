#excercise1 function 
def product_of_three(a,b,c):
    print(a*b*c)
product_of_three(8,9,10)

#excercise2 function return
def returnAnswer(a,b):
    return a/b
result=returnAnswer(9,3.5)
print(result)

    
#exercise3  lamdas
my_list = [1, 2, 3, 4, 5]
sum_of_list = list(map(lambda x: x*x, my_list))
print(sum_of_list)

#exercise4 Realworld example

 

celsius_readings = [22.5, 23.1, 21.9, 150.0, 24.0, -10.0, 22.8]

# expression for item in iterable if condition
fahrenheit_readings_filtered_lc = [
    (celsius * 9/5) + 32
    for celsius in celsius_readings
    if 0 <= celsius <= 100
]

print("Fahrenheit readings (list comprehension):", fahrenheit_readings_filtered_lc)


names=list(('jose','makos','oscar'))
print(len(names))
