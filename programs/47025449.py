def get_input():

    Name = input("Enter a name: ")
    Hours = float(input("Enter hours worked: "))
    Rate = float(input("Enter hourly rate: "))
    return Name, Hours, Rate

def calc_pay(Hours, Rate):

    if Hours > 40:
        print((40 * Rate) + (Hours - 40) * (Rate * 1.5))
    else: 
        print(Hours * Rate)

Name, Hours, Rate = get_input()
calc_pay(Hours, Rate)