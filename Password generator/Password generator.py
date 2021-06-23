#Password generator
import random

def generate_password():
    first_upper = random.randint(65, 90)
    second_upper = random.randint(65, 90)
    first_lower = random.randint(97, 122)
    second_lower = random.randint(97, 122)
    number_one = random.randint(48, 57)
    number_two = random.randint(48, 57)
    symbol_one = random.randint(43, 47)
    symbol_two = random.randint(43, 47)

    password_characters_list = [chr(first_upper), chr(second_upper), chr(first_lower), chr(second_lower) ,chr(number_one) ,
                               chr(number_two), chr(symbol_one),chr(symbol_two)]


    random.shuffle(password_characters_list)
    final_password = ""
    for l in password_characters_list:
        final_password += l


    return final_password

print(generate_password())