a = int(input("Enter a number between 1 to 10:"))

match a:
    case 7:
        print("You won a pen")
    case 2:
        print("You won a chocolate")
    case 5:
        print("You won a 50rupees voucher")
    case _:
        print("Better luck next time")
