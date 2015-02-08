#!/usr/bin/python -tt

def get_phone_numbers(record):
    name, email, *phone_numbers = record
    return phone_numbers

user_record_1 = ('Ian', 'ian@test.com', '789-222-3434', '212-444-8181')
user_record_2 = ('Hope', 'hope@test.com', '808-321-0437')

print("Ian's phones:", get_phone_numbers(user_record_1))
print("Hope's phones:", get_phone_numbers(user_record_2))

