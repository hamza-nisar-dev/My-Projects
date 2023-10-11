import datetime
msg="2022-04-04"
birth_date = datetime.datetime.strptime(msg, '%Y-%m-%d')
print(birth_date)