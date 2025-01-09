import datetime
birthdate = "14-05-1991"
day,month,year = map(int, birthdate.split("-"))
today = datetime.date.today()
age = today.year - year - ((today.month, today.day) < (month, day))
print("Your age is",age,"years.")

