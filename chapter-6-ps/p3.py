inpt = input("Type a comment\n")

s ="Make a lot of money"
v ="Buy now"
d ="Subscribe this"
k ="Click this"

if((s in inpt) or (v in inpt) or (d in inpt) or (k in inpt) ):
    print("Spam comment detected")
else:
    print("No comments detected")