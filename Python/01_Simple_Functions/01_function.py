def income(hour, per_hour):
    if hour > 8:
        return 'Too much!'
    else:
        return 'You have enough time to rest'

print(income(9,9))



"""
This code defines a function that assesses daily working hours and returns a corresponding message.
The last line, print(income(9,9)) , is to test the function.
"""