#1
def number_of_food_groups():
    return 5
print(number_of_food_groups())  # prints 5

#2
def number_of_military_branches():
    return 5
print(number_of_days_in_a_week_silicon_or_triangle_sides() + number_of_military_branches()) # error due to first words not being a variable

#3
def number_of_books_on_hold():
    return 5
    return 10
print(number_of_books_on_hold()) # only returns 5 function exits on the first return statement

#3
def number_of_books_on_hold():
    return 5
    return 10
print(number_of_books_on_hold())

#4
def number_of_fingers():
    return 5
    print(10)
print(number_of_fingers()) # only returns 5 as the print statement is after the return statement

#5
def number_of_great_lakes():
    print(5)
x = number_of_great_lakes()
print(x)      # the variable x was never assigned a value

#6
def add(b,c):
    print(b+c)
print(add(1,2) + add(2,3)) # Returns add(1,2)  and add(2,3) doesnt add the values

#7
def concatenate(b,c):
    return str(b)+str(c)
#  print(concatenate(2,5)) # fucntion would run due to indentionation otherwise it would return the string 25

#8
#def number_of_oceans_or_fingers_or_continents():#
# b = 100
    #print(b)
    #if b < 10:
#return 7
# print(number_of_oceans_or_fingers_or_continents())

#9
def number_of_days_in_a_week_silicon_or_triangle_sides(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3 #never gets to this return statement
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3)) # returns 7
print(number_of_days_in_a_week_silicon_or_triangle_sides(5,3)) #returns 14
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3) + number_of_days_in_a_week_silicon_or_triangle_sides(5,3)) #returns 21

#10
def addition(b,c):
    return b+c
    return 10 # never gets to this return statement
print(addition(3,5)) #returns 5 +3

#11
b = 500
print(b) # prints 500
def foobar():
    b = 300
    print(b) #prints 300

print(b) #prints 500
foobar() # calls on the function
print(b) #prints 500

#12
b = 500
print(b) #prints 500
def foobar():
    b = 300
    print(b) #prints 300
    return b #returns 300
print(b) #prints 500
foobar() #calls on function 
print(b) #prints 500


#13
b = 500
print(b) #prints 500
def foobar():
    b = 300
    print(b)
    return b #returns 300
print(b)
b=foobar() # calls on function assigns it the the variable b
print(b) # prints 300

#14
def foo():
    print(1) #prints 1 
    bar() #calls on the function bar
    print(2) #prints 2
def bar():
    print(3) #prints 3 
foo() #calls on the function foo 

#15
def foo():
    print(1) # prints 1 
    x = bar() #calls on the function bar and assigns the value to x
    print(x) # prints that assigned value
    return 10 # returns 10
def bar():
    print(3) # prints 3 
    return 5 #returns 5
y = foo() #call on function asssigns value to a variable y 
print(y) # prints that assigned value





































