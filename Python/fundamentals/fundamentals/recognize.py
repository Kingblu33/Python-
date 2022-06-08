num1 = 42        #variable declaration, initialize number
num2 = 2.3       # variable declartion, initializing number
boolean = True    # variable declartion, boolean
string = 'Hello World' #declartionof a string
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives']  #list Declaration
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': 'False'} #Dictionary declaration
fruit = ('blueberry', 'strawberry', 'banana') # declaration of a tuple
print(type(fruit)) 
print(pizza_toppings[1]) # access second value in the array toppins
pizza_toppings.append('Mushrooms') # adds the word mushrooms to the end of the pizza toppings list
print(person['name']) # Access 
person['name'] = 'George' #changes the value of name to geroge
person['eye_color'] = 'blue' #assigns the word blue to eye color
print(fruit[2]) #access and prints the third value in fruit
  
if num1 > 45:    # if statement condition , checking if the value stored in num1 is gr
    print("It's greater")  #action that happens if the if statement is true
else: # else  if statement
     print("It's lower") #action that happens if the if statement is true      

if len(string) < 5:   # if statement condition ,. checking if the length of the string is less than 5
    print("It's a short word!") # action if that statement is true
elif len(string) > 15: # if statemnet condition checking if the string lenght is greater than 15
    print("It's a long word!") # action if the statement is true
else:
    print("Just right!") # if the statement isnt true do this

for x in range(5):  #for loop start
    print(x)    # for loop stop
for x in range(2,5): #for loop start
    print(x) #for loop stop
for x in range(2,10,3): # for loop start
    print(x)   #for loop stop
x = 0
while(x < 5): #while loop start
    print(x)
    x += 1  #while loop stops and inecrement

pizza_toppings.pop() # deletes the last element in tis array
pizza_toppings.pop(1) # deletes the element at this array

print(person) # prints the value stored in person
person.pop('eye_color') #deletes the value stored in eye color
print(person) #prints new value stored in person

for topping in pizza_toppings: # for loop , start
    if topping == 'Pepperoni': # if statment
        continue # continue
    print('After 1st if statement') #prints this onto the terminal if condition is met
    if topping == 'Olives': # if statement
        break    #for loop stops

def print_hello_ten_times():  # declaration of a function
    for num in range(10):  # for loop
        print('Hello') # prints hello if condition is true

print_hello_ten_times()  #calls on the function

def print_hello_x_times(x): #deckaration of a function
    for num in range(x): # for loop
        print('Hello') # prints hello if condition is true
 
print_hello_x_times(4)  # call on the function

def print_hello_x_or_ten_times(x = 10): # declartion of a function
    for num in range(x): # for loop
        print('Hello') # printshello if conditons is true

print_hello_x_or_ten_times() # calls on the function
print_hello_x_or_ten_times(4) # calls on the function


"""
Bonus section
"""

# print(num3)     
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])  
# print(pizza_toppings[7]) 
#   print(boolean)
# fruit.append('raspberry') 
# fruit.pop(1) 