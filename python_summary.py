# summary python


# ========================================================================
# birth_year = input("birth years: ")
# age = 2019 - int(birth_year)
# print(type(age))
# print(age)

# course = "python for beginner"
# # print(course[1])
# # print(course[-2])
# # print(course[0:3])
# # print(course[1:])
# # print(course[:4])
# # print(course[:])
# # print(course[1:-1])
# ====================================================================
# format string
# first = 'ayoub'
# last = 'smatti'
# message = first + '['+last + ']' + 'is a coder'
# msg = f'{first} [{last}] is coder '
# print(message)
# print(msg)

# =====================================================================
# method string
# course = "python for beginner"
# print(len(course))
# print(course.upper())
# print(course.lower())
# print(course.find('n'))
# print(course.replace('b','f'))
# print('p' in course)
# ======================================================================
# x = 10
# x = x +3
# x +=3
# print(x)
# x= 10 + 3*2
# print(x)
# =======================================================================
# z = 10 + 3 * 2 ** 2
# # f = (2+3) * 10 - 3
# # print(z)
# # print(f)
# #
# # x = 2.9
# # print(round(x))
# # x = -2.9
# # print(abs(x))
# ========================================================================

# import math
# print(math.ceil(2.9))
# print(math.floor(2.9))

# ========================================================================
# is_hot = False
# if is_hot:
#    print('the weather is hot')
# else:
#    print('is lovely day')
# print('enjoy your day')
# ========================================================================
# price = 1000000
# has_good_credit = True
# if has_good_credit:
#     down_payment = 0.1 * price
# else:
#     down_payment = 0.2 * price
# print(f"down payment is: {down_payment}")
# ========================================================================

# AND
# OR
# NOT

# ========================================================================
# is_good_credit =True
# is_criminal_record = False
# if is_good_credit and not is_criminal_record:
#     print("Eligible")
# ========================================================================
# Comparison operator
# < > <= >= != ==

# ========================================================================

# weight = int(input("weight: "))
# unit = input('(L)bs or (K)g: ')
# if unit.upper() == "L":
#     converted = weight * 0.45
#     print(f"You are {converted} kilos")
# else:
#     converted = weight / 0.45
#     print(f"You are {converted} pounds")

# ========================================================================

# i = 1
# while i <= 5:
#     print('*' * i)
#     i += 1
# print("Done")

# ========================================================================
# secret_number = 9
# guest_count = 0
# guest_limit = 3
# while guest_count < guest_limit:
#     guest = int(input('Guess: '))
#     guest_count += 1
#     if guest == secret_number:
#         print("You won!")
#         break
# else:
#     print("Sorry!")
# ========================================================================

# command = ""
# command_check = ""
# while True:
#     command = input("> ").lower()
#     if command == "start":
#         if command_check =="start":
#             print("The car already starting...")
#         else:
#             print("The Car is starting...")
#         command_check = command
#     elif command == "stop":
#         if command_check =="stop":
#             print("The car already stopped")
#         else:
#             print("The Car is Stopped")
#         command_check = command
#     elif command == "help":
#         print("""
# start -to start the car
# stop  -to stop the car
# quit  -to quit
#               """)
#     elif command == "quit":
#         break
#     else:
#         print("sorry i cant understand!")

# ========================================================================

# for item in 'python':
#     print(item)
#

# =========================================================================
price = [10,20,30]
for i in price:
    print(price[0]+price[1]+price[2])








