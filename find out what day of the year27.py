import datetime

date = input('Enter the date (DD MM YYYY): ')

day_name = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

day = datetime.datetime.strptime(date, '%d %m %Y').weekday()

print("Day is:", day_name[day])