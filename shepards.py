#Author: Daniel Oram

#Code club Manurewa intermediate

#This line stores all the words typed from keyboard when you press enter

myString = raw_input()

#lets make a function that checks that our string is more than 8 characters long

#to define a function we must use the special keyword 'def'

#this states that our code inside of it is part of the function
# defined above it

#Here is an example function

def myFunction():
	print("This function prints our string " + "\"" + myString + "\" " + "to the console!")


#Notice that we indented the print() statement with a tab (or 4 spaces)
# below our line of code that defined myFunction

#We can think of this as putting the print() statement 'inside'
# of our function

#All lines of code that are indented by 4 spaces or a tab can be thought of this way

#code that is indented cannot be executed unless the function
# it is inside of is called

myFunction()

#What if we want to indent code a second or a third time?

#We can have code blocks within codeblocks by applying the
# same indenting rule above

#for example

def mySecondFunction():
	def myInnerFunction():
		print("This function is within another function")

	myInnerFunction()


#Here we call the inner function within our second function but we didn't call our second function itself!

mySecondFunction()