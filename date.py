#program to find out the difference between two dates
from datetime import date

f_date = date(int(input("Enter year in yyyy format \n")), int(input("Enter month in mm format\n")), int(input("Enter date in dd format\n")))
l_date = date(int(input("Enter year in yyyy format \n")), int(input("Enter month in mm format\n")), int(input("Enter date in dd format\n")))
diff = l_date - f_date
print("Difference between dates is" + str(diff.days) + " days.")
