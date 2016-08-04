#Code club Manurewa intermediate


#This line stores all the words typed from keyboard when you press enter

myString = raw_input()

#Lets print out myString so that we can see proof of our awesome typing skills!

#Try typing myString between the brackets of print() below

print(myString)


#With our string we want to make sure that the first letter of each word is a capital letter

#Try editing myString by calling .title() at the end of myString below - This Will Capitalise Every Word In Our String

myCapitalString = myString.title()

print("My Capitalised String looks like \"" + myCapitalString + "\"!")

#Now we want to reverse myString so that it looks backwards!

#Try reversing myString by putting .join(reversed(myCapitalString)) after the empty string below - it will look like this -> ''.join(reversed(myCapitalString))

myBackwardsString = ''.join(reversed(myCapitalString))

#Lets see how we did!

print("My backwards string = " + "\"" + myBackwardsString + "\"")

#Whoa that looks weird!

#Lets reverse our string back so that it looks like normal!

#Can you do that just like we did before?

myForwardString = ''.join(reversed(myBackwardsString)) #remember to use myBackwardsString instead of myCapitalString !

print("My forward string = " + "\"" + myForwardString + "\"")

#Ok phew! we should be back to normal

#Lets try reverse our string again but this time we want to reverse the word order! NOT the letter order!

#To do this we need to find a way to split our string up into the individual words

#Try adding .split() to the end of myForwardString kind of like we did before

myListOfWords = myForwardString.split()	#replace the [...] with something that looks like line 27!

#Now lets reverse our List so that the words are in reverse order!

myBackwardsListOfWords = reversed(myListOfWords)

#Before we can print it out we must convert our list of words back into a string!

#Our string was split into several different strings and now we need to join them back together

#HINT: we want to use the .join() function that we used earlier but this time we just want to put our list of words inside the brackets and 
# NOT reversed(myBackwardsListOfWords) inside of the brackets!

myJoinedString = ' '.join(myBackwardsListOfWords) # replace the [...] with the right variable!

print("My joined string = " + "\"" + myJoinedString + "\"")

#Hmmm our list is now in reverse.. but it's hard to read! 

#Go back and fix our issue by adding a space between the '' above. That will add a space character between every word in our list when it joins it together!



#Nice job! You've finished blueberry.py







