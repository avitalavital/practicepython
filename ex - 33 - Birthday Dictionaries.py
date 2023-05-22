birthday_dictionary = {
    "avital": "11.12.1999",
    "natalie": "15.9.2002",
    "kfir": "14.3.1998",
    "hila": "19.7.2000"
}

print("Welcome to the birthday dictionary. We know the birthdays of:" + (str(birthday_dictionary.keys())))
NAME = input("Who's birthday do you want to look up?")
print(NAME + "'s" + " birthday is " + birthday_dictionary[NAME])
