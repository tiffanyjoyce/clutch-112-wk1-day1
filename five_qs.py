# Question 1 - Write a function to print"Hello_USERNAME

def hi(un):
    # return "Hey " + un.title() + "!"
    print("Hey " + un.title() + "!")
    print(f'Hey {un.title()}!')
    return f'Hey {un.title()}!'
print(hi('Brendan'))


# Question 2 - Print first odd numbersbetween 1 and 100



# def odd_numbers():
#     for i in range(1,101,2):
#         print(i)

# odd_numbers()

def odd_numbers2():
        numbers = list(range(0, 101))
        print(numbers)
        for number in numbers:
            if number % 2 != 0:
                print(number)

# odd_numbers2()


# Question 3 - Write a function returns themax number in a given list

def max_num_in_list(a_list):
    big = 0
    for a in a_list:
         if a > big:
              big = a
    return big

print(max_num_in_list([2,3,5,8,9, 100, 67, 45, 2]))

# Question 4 - Write a function to return ifthe given year is a leap year a functionreturns the max number in a given list

def is_leap_year(a_year):
    if a_year % 4 == 0 and a_year % 100 != 0:
        print(f'{a_year} is a leap year')
    elif a_year % 400 == 0:
        print(f'{a_year} is a leap year')
    else:
        a_year = False
        print(f'{a_year}')


# # Question 4 1.b solution

# def is_leap(a_year):
#     if a_year % 4 == 0 and (a_year % 400 == 0 or a_year % 100 != 0):
#         print(True)
#     else:
#         print(False)

# is_leap_year(2019)

# Question 5 - Write a function to check ifall numbers in a list are consecutive

sl = [0, 1, 2, 3, 4]



def is_consecutive(a_list):
    i = 0
    status = True
    while i < len(a_list) - 1:
       if a_list[i] + 1 == a_list[i + 1]:
           i += 1
       else:
            status = False
            break
    print(status)

# hello Brandt!
