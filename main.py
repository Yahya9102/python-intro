

# dagens övning
def check_age(name):
     
    age = 20

    if age >= 18:
        return f"Hej {name}, du är myndig"
    else:
        return f"Hej {name}, du är inte myndig"



user_name = input("Ange ditt namn: ")
result = check_age(user_name)


print(result)
     







# Skapa en funktion som tar en en parameter "string" 
# Deklarera er ålder som variabel som gör en if check om ni är myndiga eller ej
# Kallar på den funktionan och tar in en användarinput från consollen och matar in den i funktion
# och sen ska det prints tex "Hej Yahya du är myndig/inte myndig"







name = input("Ange ditt namn: ")

name = name.strip()

print(f"Hej {name}! Kul att du är här.")



# Function that greets a user by name
def greet_user(name):
     if len(name) == 0:
          return "Du måste ange ett namn"
     else:
          return "Hej, " + name
     

names = ["Yahya", "Rasmus", "Martin", "Robert", "Shweta"]

#for name in names:
 #    print(greet_user(name))







# While loop
count = 0

while count < 5:
     #print("Count är: ", count) 
     count += 1






# Numberiskt for loop
numbers = [10,20,30,40,50]



# For loop used to iterate over a range of numbers based on the length of the list
#for i in range(len(numbers)):
     #print(i)







# for loop
names = ["Yahya", "Rasmus", "Martin", "Robert", "Shweta"]


# For loop used normally for iterating over a list
#for name  in names:
     #print(name)







# if else else if statement
temp = 33

if temp > 18:
     print("")
elif temp < 10: # else if
     print("kallt")
else:      
    print("vet ej")



# function that returns a value
def add(a, b):
     return a + b

# Call the function and store the result in a variable
result = add(5,5)
#print(result)









# function that takes in a param name and prints a greeting
#def greeting(name):
#     print("Hej: " + name)


#username = "Yahya"
#Call the function with the argument username
#greeting(username)



# Dictionaries in Python (AKA Objects in other languages)
person = {
    "name": "Yahya",
    "age": 33,
    "Is_student": False
}


# Variables in Python
number = 5
numberFloat = 3.3
text = "Yahya"
is_student = True


#Lists in Python
numbersList = [10,20,30,40,50,33.3]
name = ["Yahya, Rasmus, Martin, Robert, Shweta"]
mixedList = [10, "Yahya", 33.3, True]




# Checking the type of variables using the function type()
#print(type(text))
#print(type(number))
#print(type(numberFloat))
#print(type(is_student))
#print(type(numbersList))
#print(type(name))
#print(type(mixedList))
#print(type(person))




