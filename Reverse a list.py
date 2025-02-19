#Let's see the different ways to reverse a list in python

#Lets first define a list
my_list = [1,2,3,4,5]

#1. Using the reverse method
my_list = my_list.reverse()
my_list # This will reverse the list and save in same name

# If we want to save as new reversed list we can use other methods
#2. Using Slicing
my_list = [1,2,3,4,5]
reversed_list = my_list[::-1]
print(reversed_list)

#3. Using the reversed function
my_list = [1,2,3,4,5]
reversed_list = list(reversed(my_list))
print(reversed_list)

#4. Using Loop
my_list = [1,2,3,4,5]
reversed_list = []
for num in my_list:
    reversed_list.insert(0,num)
print(reversed_list)

#5. Using append method
my_list = [1,2,3,4,5]
reversed_list = []
for num in range(len(my_list)-1,-1,-1):
    reversed_list.append(my_list[num])
print(reversed_list)
    





