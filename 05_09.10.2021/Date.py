import time
date = input('Дата (День/Месяц/Год): ')
try:
  valid_date = time.strptime(date, '%d/%m/%Y')
  print('Верная дата')
except ValueError:
  print('Неверная дата')