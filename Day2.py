"""
As you can see, the code is broken.
Create the missing functions, use default arguments.
Sometimes you have to use 'return' and sometimes you dont.
Start by creating the functions
"""

# \/\/\/\/\/\/\  DO NOT TOUCH AREA  \/\/\/\\/\ #

def is_on_list(days,day):
    if day in days:
      return True
    else:
      return False

def get_x(days,day):
    return days[day]

def add_x(days,day):
    return days.append(day)

def remove_x(days,day):
    return days.remove(day)


days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

print("Is Wed on 'days' list?", is_on_list(days, "Wed"))

print("The fourth item in 'days' is:", get_x(days, 3))

print("done!")
add_x(days, "Sat")
print(days)

remove_x(days, "Mon")
print(days)
#debug#

# /\/\/\/\/\/\/\ END DO NOT TOUCH AREA /\/\/\/\/\/\/\ #




