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

#exercise4
try:
    if(5>0):
        print("its a postive number")
except:
    
            