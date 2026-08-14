
# # Exceptional handling

# while True:
#     try:
#         e = int(input("Enter number 1 : "))
#         l = int(input("Enter number 2 : "))
#         print(e/l)
#     except ValueError:
#         print("Please dont perform value error")
#     except ZeroDivisionError:
#         print("Dont divide by 0")
#     except Exception as e:
#         print("Their is an unkown error",e)
    
# Throwing an error  // custome error  (used by developers interact)
# n = int(input("Enter number 1 : "))
# m = int(input("Enter number 2 : "))
# if(m == 0):
#     raise ValueError("Dont use 0 as secand number !")
# print(n/m)

# else factor in error / it only occurs when their is no error in try block

try:
    89/90
except Exception as e:
    print("Dont divide by zero buddy !")
else:
    print("Heloo my beautiful girl haa myy one and only beautiful girl havi")

# In exceptions finally is always executed 
finally:
    print("I am always executed no matter what happens !")