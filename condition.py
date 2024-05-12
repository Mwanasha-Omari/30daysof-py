# input
# an array of numbers

#  process 
# iterate through the numbers to get all the numbers 
# if its divisible by both 3 and 5,3 or 5

# output
# if the number is divisible by both three and 5
# it should print out fizzbuzz
# if the number is divisible by 3 it should print out fizz
# if the number is divisible by 5 it should print out buzz




# 1. Write a program that iterates through numbers from 1 to a given limit (e.g., 100).
#  For each number: If the number is divisible by 3, print ""Fizz"".
#  If the number is divisible by 5, print ""Buzz"".
#  If the number is divisible by both 3 and 5, print ""FizzBuzz"".
# Otherwise, print the number itself.
def check_word(n):
    numbers=range(n)
    for number in numbers:
        if number%3==0:
            print(f"{number} fizz")
        elif number%5==0:
            print(f"{number} buzz")
        elif number %5==0 %3==0:
            print(f"{number} fizzbuzz")
        else :
            print(f"{number}")



# input
# number
#  process
#   checking if the number is less than one it should print 
# out the number is not a prime number  
# if the number is divisible by 3 and not divisible by two the
#  number is a prime number      
#  else the number should be invalid
# output
# prime number
# not a prime number
# nimber is not valid





#  " Write a program that takes a number as input and determines if it's prime.

def check_prime_number(numbers):
    for number in numbers:
        if number<1:
            print(f"{number} is not a prime number")

        elif number%2!=0 and number%3==0:
            print(f"{number} is a prime number")
        else:
            print(f"{number} is not valid")



# input
#    year            
#  process 
#  checking if the year is divisible by 4
# checking if the year is divisible by 400
# checking if the year is divisible by 100
       
# output
#  if the number is divisible by 100 400 and 4 
# print its a leap year  
# else it is not a leap year  
            


#  "Write a program that takes a year as input. Check if the year is a leap year based on the following rules:
#  A year is a leap year if it is divisible by 4 but not by 100.
#  However, if the year is divisible by 100, it must also be divisible by 400 to be considered a leap year."
def check_year(year):
    if year%4==0:
        if year%100==0:
            if year%400==0:
                print(f"{year} is a leap year")
            else:
                print(f"{year} is a leap year")
        else:
                    print(f"{year} is a leap year")
    else:
               print(f"{year} is not a leap year")



     # input
 #character
               
#  process
# iterating through the list of vowels checking if the character is a vowel or a consonant
# cecking if the character is in the vowels

# output     
# if the character is in the list of vowel print out 
# character is a vowel 
# else it should print out the character is a consonant
         
#  Write a program that takes a character as input. Check if the character is a vowel (a, e, i, o, u) and display "Vowel" or "Consonant" accordingly.
def vowel_or_consonant(char): 
     vowel=['a','e','i','o''u']
     for i in vowel  : 
       if vowel[i]==char :
        print(f"{char} is a vowel")  
       else:
            print(f"{char} is a consonant")  
   

# input
#   list of numbers          
#  process 
# sort the numbers in an ascending order

# output
# maximum and minimum number

# Write a program that takes an array of numbers as input and finds the minimum and maximum elements.
numbers=[1,2,3,4,5,6,8,9,]
sorted_numbers=numbers.sort()
print(numbers[0])   
print(numbers[-1])   




# input
# a list of numbers
#  process 
# adding each number in the list and getting the total
# output
# sum of the numbers in the list

# Write a program that takes an array of numbers as input and calculates the sum of all elements.
numbers=[1,2,3,4,5,6,8,9,]
count=0
for i in numbers :
     count+=i
     print(count)

# input
#   list of numbers and a number 

#  process 
#  checking if the number is in the array
# output
    #  the number exists in the array


# Write a program that takes an array and a number as input and checks if the number exists in the array.
numbers=[1,2,3,4,5,6,8,9,]
number=3
if number in numbers:
       print(f"{number} exists in numbers")