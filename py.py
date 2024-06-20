import re

phone = input('Введите номер телефона: ')

if re.match(r'\+7\(\d{3}\)\d{3}-\d{2}-\d{2}', phone.replace(' ', '')):
    print(1)
print(0)