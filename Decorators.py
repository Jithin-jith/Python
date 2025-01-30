#Decorators are functions that wrap other functions and enhance its behaviour.
#They are examples of Higher order functions
#They have their own syntax, using "@".

#Let's create a wrapper function to wrap another function
def be_polite(func): # The main wrapper function
    def wrapper(): 
        print("Hello. Nice to meet you!")
        print(func())
        print("See you! Take care")
    return wrapper # Returns the sub function
    
def greet(): #the function to be wrapped
    return "How are you?"

polite = be_polite(func=greet) #save the returuned function into a variable
polite() #run the function

#Now let's create the Decorator using the synta "@"

@be_polite # The syntax used to mention the wrapper function
def scold(): #The function that needs to be wrapped
    return "I HATE YOU"  #The return value

scold()  #Run th function. No need to save the return and then execute the function