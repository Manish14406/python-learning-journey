# # program to develop : that reads student data name,srn,marks in 3 sub and total marks percentage with suitable message

# name = input("Enter your name\n")
# srn = input("Enter your SRN\n")
# sub1 = int(input("Enter your mark in sub-1"))
# sub2 = int(input("Enter your mark in sub-2"))
# sub3 = int(input("Enter your mark in sub-3"))

# t_marks = sub1+sub2+sub3
# percentage = (t_marks/300) * 100

# print("Name : ",name)
# print("SRN : ",srn)
# print("Total : ",t_marks)
# print(f"Percentage : {percentage} %")

# ------------------------------------------------------------------------
# n = int(input("enter a number"))
# for i in range(n):
#     print(i)
# for i in range(-5,+6):
#     print(i)

# for i in range(0,n,2):
#     print(i)
# for i in range(1,n,2):
#     print(i)

# ---------------------------------------------------------------------------------

# “List1” is a list that contains the “N” different SRN of students read using a
# user defined function with the help of input(). SRN of “M” more students are
# to be appended or inserted into “List1” at the appropriate place and also
# return the index of the SRN entered by user

# list1 = []
# def read():
#     n = int(input("Enter the number of srn to insert"))
#     for i in range(0,n):
#         srn = input("Enter srn : ") 
#         list1.append(srn)
# read()
# f = input("are you interested in adding more srn's")
# if f == 'yes':
#     pos = int(input("Enter the position to insert : "))
#     s = input("Enter the srn : ")
#     list1.insert(pos,s)
# else:
#     pass

# print(list1)
# p = input("Enter the index of element to be printed : ")
# print("The index of srn enetered by user",p,'=',list1.index(p))

# --------------------------------------------------------------------------------

# “Tuple1” and “Tuple2” are two tuples that contain “N” different data type
# read using the user defined function “READ” with the help of input( ).
# Elements of “Tuple1” and “Tuple2”are to be read one at a time and the
# “larger” value among them should be put into “Tuple3”.

# the whole catch is 2 tuples with diff data types the max value of these tuples in the tuple 3 

# t1 = ()
# t2 = ()
# l1 = list(t1)
# l2 = list(t2)

# def read():
#     count = int(input("Enter the number of elements : "))
#     for i in range(count):
#         print("Enter elements of tuple 1 : ")
#         l1.append(int(input()))
#     for i in range(count):
#         print("Enter elements of tuple 2 : ")
#         l2.append(input())
# read()
# t1 = tuple(l1)
# t2 = tuple(l2)
# t3 = (max(t1),max(t2))
# print("The max of t1 and t2 are : ",t3)

# ------------------------------------------------------------------------------------------------------

# union and intersection

s1 = set()
s2 = set()
s3 = set()
def union():
    for i in s2:
        if i in s1:
            pass
        else:
            s1.add(i)
    print("Union : ",s1)

def inter():
    for i in s2:
        s3.add(i)
    else:
        pass
    print("intersection :",s3)



# n = int(input("Enter number of elements in s1\n"))
# for i in range(n):
#     s1.add(int(input()))
# m = int(input("Enter number of elements in s2"))    
# for i in range(m):
#     s2.add(int(input()))

# ch = int(input("1:union\n2:intersection"))
# if(ch==1):
#     union()
        
# elif (ch == 2):
#     inter()

# -----------------------------------------------------------------------------------------

# oops object oriented
# cls = blueprint, encapsulation of method and variables to ensure security
# object = instance of the cls
# constructer = it is a special method that is automaitically executed when object is created 
# display = used to display the value stored inside the object variable 


# class student:
#     def __init__(self,name,no):
#         self.name = name              #initialising of object variable
#         self.no = no

#     def display(self):
#         print("Name : ",self.name)
#         print("No : ",self.no)

# s1 = student("Manish",21)  #creating object variable
# s1.display()                  # calling display method

# ==============================

# class Car:
#     def __init__(self,name,year,price):
#         self.name = name
#         self.year = year
#         self.price = price
        
#     def display(self):
#        print(str(self.name),str(self.year),str(self.price))

# carobject = []

# n = int(input("Enter no of cars  : \n"))
# for i in range(n):
#     name = input("Enter name : ")
#     year = int(input("Enter year : "))
#     price = float(input("Enter price : "))
#     carobject.append(Car(name,year,price))

# print ("NAME  |   year   |   price   ")
# for obj in carobject:
#     obj.display()

# ------------------------------------------------------------------------------------------------

# 12. Airline Reservation System contains the attributes of passengers such as
# Name, PAN-No., Mobile-no, Email-id, Source, Destination, Seat-No and AirFare, Travel_date. A Class is required to be created for “Airlilne” with the
# above attributes and perform the following operations:
# a. Get the details of “Airline” object from user and store into Array of
# objects
# b. List details of all the passengers who travelled From “Bengaluru to
# # London”.
# # c. List details of all the passengers who travelled From “USA to China”
# # on 10th of Feb, 2020. 

# class ARS:
#     def __init__(self,Name,src,des,date):
#         self.name = Name
#         self.src = src
#         self.des = des
#         self.date = date
#     def display(self):
#         print(self.name,"\t",self.src,"\t",self.des,"\t",self.date)

# l = []

# n = int(input("No of passenger\n"))

# for i in range(n):
#     Name = input("Eneter name : ")
#     src = input("source       : ")
#     des = input("destination  : ")
#     date = input("date        : ")
#     l.append(ARS(Name,src,des,date))

# for obj in l:
#     obj.display()

# print("people named manish and the date 10/10/1000\n")
# for obj in l:
#     if (obj.name.lower() == "manish"  and obj.date == "10/10/1000"):
#         obj.display()


# +============================================================================

# Adding student data into file
# infile = open("Std.txt", 'a+')

# flag = input("Do you want to update the file (Y/N): ")

# if flag.upper() == 'Y':
#     n = int(input("Enter how many students: "))
#     for i in range(n):
#         srn, name, sem, sec, avg_mark = input(
#             "Enter SRN Name Semester Section AvgMarks:\n").split()
        
#         infile.write(srn + " " + name + " " + sem + " " + sec + " " + avg_mark + "\n")

# infile.close()


# # Extracting required students
# print("\nStudents of 4th Semester A Section with Avg >= 75:\n")

# outfile = open("Std.txt", 'r')
# mylines = []

# for line in outfile:
#     mylines.append(line.split())   # split each line into list: [srn, name, sem, sec, avg]

# for element in mylines:
#     srn = element[0]
#     name = element[1]
#     sem = element[2]
#     sec = element[3]
#     avgmark = int(element[4])

#     if sem == "4" and sec.upper() == "A" and avgmark >= 75:
#         print(element)

# outfile.close()


# import numpy

# def READ_DATA(R, C, matrix):
#     for i in range(R):
#         for j in range(C):
#             matrix[i][j] = int(input())


# m = int(input("\nEnter the row size M: "))
# n = int(input("Enter the column size N: "))

# matrix = numpy.ndarray(shape=(m, n), dtype=int)

# print("\nSize:", matrix.size)
# print("Shape:", matrix.shape)
# print("Dimensions:", matrix.ndim)

# print("\nEnter %d elements of %dx%d matrix:" % (m * n, m, n))
# READ_DATA(m, n, matrix)

# print("\nMatrix is:")
# print(matrix)

# print("\nDiagonal Elements:")
# dia = matrix.diagonal()
# print(dia)

# r = int(input("\nEnter row index to display: "))
# print(matrix[r])

# c = int(input("Enter column index to display: "))
# print(matrix[:, c])


# name = input("Enter yout name : ")
# sub1 = int(input("Enter the marks in sub 1 : "))
# sub2 = int(input("Enter the marks in sub 2 : "))
# sub3 = int(input("Enter the marks in sub 3 : "))

# t_marks = sub1+sub2+sub3
# percentage = ((t_marks)/300)*100

# print(f"Name        : {name}")
# print(f"Total marks : {t_marks}")
# print(f"Percentage  : ",percentage)


# n = int(input("Enter a number \n"))

# temp = n 
# sum = 0

# digits = len(str(n))

# while temp>0 :
#     digit = temp% 10
#     sum = sum + (digit ** digits)
#     temp = temp // 10

# if(sum == n):
#     print("Armstrong")
# else :
#     print("Noooo ! not a armstrong")

# list = []

# def read():
#     n = int(input("Enter number of students : \n"))
#     for i in range(n):
#         srn = input(("Enter SRN : "))
#         list.append(srn)
# read()
# flag = input("Whether you want to enter some more srn's Y/N")
# if(flag == "Y"):
#     pos = int(input("Enter the position to insert SRN : "))
#     s   = input("Enter srn : ")
#     list.insert(pos,s)
# print(list)
# p = input("Enter the index of srn to return  : ")
# print("The index of Srn is ",list.index(p))


# t1 = () 
# t2 = () 
# t3 = () 
# L1 = list(t1)
# L2 = list(t2)

# def read():
#     n = int(input("Enter the quantity : "))
#     for i in range(n):
#         dt = input("Enter elements in tuple 1 ")
#         L1.append(dt)
#     for i in range(n):
#         dts = input("Enter elements in tuple 2 ")
#         L2.append(dts)
# read()

# tuple1 = tuple(L1)
# tuple2 = tuple(L2)

# t3 = (max(tuple1),max(tuple2))
# print(t3)

# class Car:
#     def __init__(self,Company_name,model,color,M_year,price):
#         self.Company_name = Company_name
#         self.model = model
#         self.color = color
#         self.M_year = M_year
#         self.price = price
#     def display(self):
#         print(self.Company_name,"\t",self.model,"\t",self.color,"\t",self.M_year,"\t",self.price)

# car_object = []
# n = int(input("Enter number of cars : "))
# for i in range(n):
#     Company_name = input("Enter car Company name : ")
#     model = input("Enter car model               : ")
#     color = input("Enter car color        : ")
#     M_year= input("Enter car Manufacturing year : ")
#     price = input("Enter car price        : ")
#     car_object.append(Car(Company_name,model,color,M_year,price))
# print("Company name  |  Model   |   Color   |   M_year   |    Price    |")
# for obj in car_object:
#     obj.display()

# class ARS:
#     def __init__(self,Name,PAN_no,Mobile_no,Email_id,Src,Des,Date):
#         self.Name = Name
#         self.PAN_No = PAN_no
#         self.Mobile_no = Mobile_no
#         self.Email_id = Email_id
#         self.src = Src
#         self.Des = Des
#         self.Date = Date
#     def display(self):
#         print(self.Name,self.PAN_No,self.Mobile_no,self.Email_id,self.src,self.Des,self.Date)

# l = []
# n = int(input("Enter how many details you want to enter : "))
# for i in range(n):
#     Name = input("Enter you name           : ")
#     PAN_no = input("Enter you pan          : ")
#     Mobile_no = input("Enter you mobile_no : ")
#     Email_id = input("Enter you email-id   : ")
#     src = input("Enter you src             : ")
#     Des = input("Enter you Des             : ")
#     Date = input("Enter date : ")
#     l.append(ARS(Name,PAN_no,Mobile_no,Email_id,src,Des,Date))

# print("List of people travelling from bangalore to london")
# for obj in l:
#     if(obj.src == "Bangalore" and obj.Des == "London"):
#         obj.display()

# print("List of people who traveled from USA to china on 10/02/2020 ")
# for obj in l:
#     if( obj.src == "USA"  and obj.Des == "China" and obj.Date == "10/02/2020"):
#         obj.display()

# def Read_input(R,C,matrix):
#     for i in range(R):
#         for j in range(C):
#             matrix[i][j] = int(input())

# import numpy

# m = int(input("Enter Row size : "))           
# n = int(input("Enter Clm size : "))     

# matrix = numpy.ndarray(shape=(m,n),dtype=int)

# print("Matrix size : ",matrix.size)
# print("Matrix shape : ",matrix.shape)
# print("Matrix dimention : ",matrix.ndim)

# print("Enter elements ")
# Read_input(m,n,matrix)

# print("MATRIX : ")
# print(matrix)

# print("The diagonal elements : ")
# dia = matrix.diagonal()
# print(dia)

# r = int(input("Enter row number to print : "))
# print(matrix[r])
# c = int(input("Enter row number to print : "))
# print(matrix[:,c])

# infile = open("std.txt","a+")

# flag = input("Do you want to update file or not Y/N")

# if(flag == "Y"):
#     n = int(input("Enter how many entries"))
#     for i in range(n):
#         srn,name,sem,sec,avg = input("Enter srn name sem sec avg ").split()
#         infile.write(srn + " " + name + " "+ sem + " " + sec + " " + avg + "\n")
# infile.close()

# outfile = open("std.txt","r+")

# print("The 4th sem students with 75 above")
# for line in outfile:
#     data = line.split()

#     srn = data[0]
#     name = data[1]
#     sem = data[2]
#     sec = data[3]
#     avg = float(data[4])
#     if(sem == "4th"  and avg >= 75):
#         print(data)


# s = set(1,2,3)
# print(s)

# class related program 

# class Student:
#     def __init__(self,name,cls):
#         self.name = name
#         self.cls = cls
#     def display(self):
#         print(f"Name : {self.name}\nClass : {self.cls}")

# s_object = []
# n = int(input("Enter no of students:\n"))
# for i in range(n):
#     name = input("Name  :")
#     cls =  input("Class :")
#     s_object.append(Student(name,cls))
# for obj in s_object:
#     obj.display()


# infile = open("text.file","a+")

# flag = input("Yes or No")
# if(flag == "Yes"):
#     n = int(input("Enter no of student details\n"))
#     for i in range(n):
#         name,branch,roll,sem = input().split()
#         infile.write(name + " " + branch + " " + roll + " " + sem + " " +"\n" )
# infile.close()

# l = []

# outfile = open("text.file","r+")



# for line in outfile:
#     data = line.split()
#     name = data[0]
#     branch = data[1]
#     roll = data[2]
#     sem = data[3]
#     print(data)
#     if(sem == "4"):
#         print(f"{"senior"}")

# outfile.close()

# print(2*"hi")