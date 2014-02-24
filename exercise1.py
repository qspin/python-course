__author__ = 'kristof'

def valid_user_input(obj):
    try:
        return float(obj)
    except ValueError:
        print("Not a valid number")
        return None

limit_down = input('Please enter the down limit: ')
while not valid_user_input(limit_down):
    limit_down = input('Please enter the down limit: ')
limit_up = input('Please enter the upper limit: ')
while not valid_user_input(limit_up):
    limit_up = input('Please enter the upper limit: ')
value = float(input('Please enter a number: '))
while not valid_user_input(value):
    value = float(input('Please enter a number: '))

print("Value is {0} then down limit".format("smaller" if value < limit_down else "bigger"))
print("Value is {0} then upper limit".format("smaller" if value < limit_up else "bigger"))



