
'''  print("Hillow World!!")
name = input("enter your name:")
age = input("enter your age:")

print("Helllo " + name + "! you are " +age+ "!")

num1 = input("enter a number:")
num2 = input("enter another number:")
result = int(num1) + int(num2)     #can use float for decimals
print(result)
'''
from itertools import filterfalse

''' color = input("enter a color: ")
plural_name = input("enter a plural noun: ")
celebrity = input("enter a celebrity: ")

print("Roses are "+ color)
print(plural_name + " are blue")
print("I love "+ celebrity)
'''

''' Lucky_numbers = [4,2,7,1,87,32,6]
friends =["kavin", "karen", "Jim", "Joy"]
friends.append("ray")  #append add new name at the end of name list
friends.insert(1,"Ravi")  #add at specific index position
friends.sort()  #sort list by alphabetical order and numbers in ascending order
Lucky_numbers.sort()
print(Lucky_numbers)
print(friends.index("Jim")) #shows the index position of that string
print(friends.count("ray")) #counts the number of repeat
print(friends)
print(friends[3])
print(friends[1:3]) #prints upto 1-2 index position

friends2 = friends.copy()  #copy the lists from exiting one and make it another
My_numbers = Lucky_numbers.copy()
print(friends2)
print(My_numbers)
'''

###Tuple####
'''
# coordinates = [(4,5), (2,3), (4,1)]
coordinates = (3,2)

print(coordinates[1])
print(coordinates[0])
'''

###Function###
'''
def say_hi(name, age):   #this functiom can print as many indented code can write and need to call function to print it
    print("hello "+ name+ ", you are "+ age)


say_hi("Tom", "30")
say_hi("Mav", "76")
say_hi("Jim", "42")
'''

###Function###
'''
def cube(num):
    return num*num*num

result = cube(5)
print(result)
'''

####If_statements###
'''
is_male = False
is_tall = False

if is_male and is_tall:       ##AND condition true if both true
    print("you are a male or tall or both")
elif is_male and not(is_tall):
    print("you are not tall but are male")
elif not(is_male) and is_tall:
    print("you are not a male but are tall")
else:
    print("you are not a male")
#------------------------------------------------#
is_male = True
is_tall = False

if is_male or is_tall:      ### OR condition  both need not to be true ###
    print("you are a male or tall or both")
else:
    print("you are not a male")
'''

####If_Statements & Comparisions #####
'''
def max_num(num1, num2, num3):       #can use operators like ==,!=,>=,<=...
    if num1>= num2 and num1>= num3:
        return num1
    elif num2>= num1 and num2>= num3:
        return num2
    else:
        return num3

print(max_num(56,7,8))
'''

###Building a calculator ####
'''
num1 = float(input("enter first number: "))
op = input("enter the operator: ")
num2 = float(input("enter second number: "))

if op == "+":
    print(num1+num2)
elif op == "-":
    print(num1-num2)
elif op == "*":
    print(num1*num2)
elif op == "/":
    print(num1/num2)
else:
    print("Invalid operator")
'''

#### Dictionaries #####
'''
monthConversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December"
}

print(monthConversions.get("Dec","Not a valid month name!"))
'''

### While_Loop #####
'''
i = 1
while i <= 96:
    print(i)
    i+=1

print("This end of the loop")
'''

### Building_Guessing_Game ###
'''
secret_word = "Hey_Babes"
guess = ""
guess_count = 0
guess_limit = 5
out_of_guesses = False

while guess != secret_word and not(out_of_guesses):
    if guess_count < guess_limit:
        guess = input("Enter guess: ")
        guess_count += 1
    else:
        out_of_guesses = True


if out_of_guesses:
    print("out_of_guesses, You lose!")
else:
    print("You win!")
'''

#### For Loop ###
'''
for Alphabets in "HELLO Mr.Ray":
    print(Alphabets)

Fruits = ["Apple", "Oranges","Mangoes","Banana"]
for name in Fruits:
    print(name)
'''

#### Exponent Function ###
'''
def raise_to_power(base_num, pow_num):
    result = 1
    for index in range(pow_num):
        result = result * base_num
    return result
print(raise_to_power(7,2))
'''

### 2D Lists & Nested Loops ###
'''
num_grid = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [0]
]
print(num_grid[0][0])
print(num_grid[0][1])
print(num_grid[1][0])
print("-----------------")
#using for loop
for row in num_grid:
    for col in row:
        print(col)
'''

#### Building a Translator ### translate vowel letters (aeiou) into @ if upperCase and * if lowerCase.
'''
def translation(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "aeiou":
            if letter.isupper():
                translation = translation + "@"
            else:
                translation = translation + "*"
        else:
            translation = translation + letter
    return translation
print(translation(input("Enter a phrase: ")))
'''

#### Try & Except ### when enter invalid input it handles the system to break and not to through error
'''
try:
    #value = 8/0
    number = int(input("Enter a number: "))
    print(number)
except ZeroDivisionError as err:
    print(err)
except ValueError:
    print("invalid input")
'''

#### READING FILES ### read files from outside stored either in same folder or different one#####
'''
Company_file = open("MyText.txt", "r")  # opened a file in read mode 'r'
print(Company_file.readable())  #use readable to check readable or not since using r to read, boolean true or f# alse
#print(Company_file.readlines()[0])  #use to read each line and move curser to next line
print(Company_file.read())      #use to read actual file

Company_file.close()            #need to close the file once it opens
'''
###Using for loop ##
'''
Company_file = open("MyText.txt","r")
for people in Company_file.readlines():
    print(people)
Company_file.close()
'''
#### Writing & append to file ###
'''
Company_file = open("MyText.txt","a") # using 'w' instead 'a' will overwrite with new and remove all previous
Company_file.write("\nShyam = Human Resources, ($7k)")
Company_file.close()
'''

### Using 'w' to create new file and write in something
'''
#Company_file = open("MyText2.txt","w")    #can create all kind of files
#Company_file = open("MyText3.txt","w")
Company_file = open("index.html","w")
Company_file.write("<p>Hello this is my new HTML file created using 'w'</p>")
Company_file.close()
'''

#### Modules & Pip ###
## sudo apt pip install python3-docx #  to install on Linux external Modules
# can use it to import functions from other files and use it here
'''
import tool

print(tool.beatles)
'''

#### Classes & Objects ####
'''
from student import student

student1 = student("Sam","Art", 3.0, False, "Volleyball")
student2 = student("Jim","IT", 2.4, True, "Soccer")
student3 = student("Ali","Business", 3.3, False, "Cricket")
print(student2.gpa)
print(student1.interest)
print(student3.name)
'''

#### Guessing Game ###
'''
from Question_bank import Question_bank

question_prompts = [ "What is the color of Sky?\n(a) Red \n(b) Blue \n(c) Yellow\n\n:>",
                     "What is the color of Leaf?\n(a) Green \n(b) Black \n(c) White\n\n:>",
                     "What is the best food for protein?\n(a) Chips \n(b) Water \n(c) Chicken\n\n:>"]

questions = [
    Question_bank(question_prompts[0],"b"),
    Question_bank(question_prompts[1], "a"),
    Question_bank(question_prompts[2], "c"),
]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score +=1
    print("you have got "+ str(score)+ "/" + str(len(questions)) + " correct")

run_test(questions)
'''

###### Object Function ####
'''
from Student import Student

student1 = Student("Shyam","Art",3.4)
student2 = Student("Jim","Business",3.8)

print(student2.on_honor_roll())
print(student1.on_honor_roll())
'''

### Inheritance #####

from Chef import Chef
from AmericanChef import AmericanChef

MyChef = Chef()
MyChef.make_special_dish()

MyAmericanChef = AmericanChef()
MyAmericanChef.make_special_dish()

