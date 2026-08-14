# marks = {
#     "Manish": 199,
#     "havii": 636,
# }
# # print(marks,type(marks))
# print(marks["Manish"])

# Manish={
#     "manish":"creater",
#     "Money": "options",
#     "Aim": "option model",
#     "List": [12,45]

# }
# print(Manish["List"])

marks = {
    "Manish": "Havi",
    "Bablu": "rudie"
}

print(marks.items())
print(marks.keys())
marks.update({"Bablu":"RUDIE"})
# print(marks["Manish2"]) GIVES ER
print(marks.get("Manish2")) # prints none

m = [["harry","manish"],8,76,0.6]
print(m)

marks.popitem()
print(marks)
print(marks.values())

# to make a empty dic

d={}


