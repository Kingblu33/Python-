print("Hello World")  # 1. TASK: print "Hello World"
name = "Noelle"
print("Hello "+ name +"!") # with a +
print("Hello", name, "!" )	# with a comma
# 3. print "Hello 42!" with the number in a variable
name = 42
print("Hello",str(name), "!")	# with a comma
print("Hello"+ str(name) +"!")	# with a +	-- this one should give us an error!
# 4. print "I love to eat sushi and pizza." with the foods in variables
fave_food1 = "sushi"
fave_food2 = "pizza"
print( "I Love to eat {} and {}".format(fave_food1,fave_food2) ) # with .format()
print( f"My name is {fave_food1} and {fave_food2}" ) # with an f string


