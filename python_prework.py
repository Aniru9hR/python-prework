# Question 1 :
#Write a function to print "hello_USERNAME!" USERNAME is the input of the function

def hello_name(user_name) : 
    print("Hello_",user_name)



hello_name(input("USERNAME "))



# Question 2 :
#Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing


def first_odds(): 
    numbers = list(range(1,101))
    odd_list = []    
    for x in numbers :
        if x%2 != 0 :  
            odd_list.append(x)
    print(odd_list)

first_odds()





#Question 3 :
#Please write a Python function, max_num_in_list to return the max number of a given list.


def max_num_in_list(a_list) : 
    print(max(a_list))


number =list(range(1,11))
max_num_in_list(number) 




#Question 4 :
#Write a function to return if the given year is a leap year. A leap year is divisible by 4, but not divisible by 100, unless it is also divisible by 400. The return should be boolean Type (true/false).


def is_leap_year(a_year) : 
    leap_year = False
    
    if a_year % 400== 0:
        leap_year = True
    elif (a_year % 4 ==0) and (a_year % 100 != 0) : 
        leap_year = True 
    return leap_year


year = int(input("Enter Year: "))
print(is_leap_year(year))




#Question 5 :
#Write a function to check to see if all numbers in list are consecutive numbers. For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers. The return should be boolean Type.


def is_consecutive(a_list) : 
    l=sorted(a_list)
    l1=list(range(min(a_list),max(a_list)+1))
    if l==l1 :
        return True
    else : 
        return False
    
print(is_consecutive([10,20,30,40,50]))  

