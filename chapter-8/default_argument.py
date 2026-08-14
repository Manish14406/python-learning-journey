# def manish(name,ending="Thanks buddy"):
#     print("Heyyy give me your pen : "+name)
#     print(ending)

# manish("Manish")  # Takes down the default value
# manish("Havii","Thanks girl")

def func(name,ending="Thanks boy"):
        print("Hey give me your pen : ",name)
        print(ending)
        return "Done"
a = func("Manish")
print(a)
func("Havii","Good girl")
print(a)