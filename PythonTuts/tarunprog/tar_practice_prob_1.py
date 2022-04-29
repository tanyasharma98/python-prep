current_year = 2021


def age_enter(age):
    print(f"you age is input age {age}")
    age = current_year - age
    print(f"Year of birth {age} and you become 100 year old in year {age + 100}")
    return age


def year_enter(year):
    current_age = current_year - int(year)
    print(f"Your current age is {current_age} in year {current_year}")
    after_year = int(input_age) + 100
    print(f"you will become 100 year old in year {after_year}")
    return year


def particular_yr(year, bornyear):
    if year > bornyear or year < input_age:
        age = year - bornyear
        print(f"your are {age} year old in {year}")
    else:
        print("Looks like you are")


try:
    input_age = int(input("Enter your age or your year of birth"))
    # if len(str(input_age)) == 4 and 1900 < input_age <= current_year:
    if 0 < input_age <= 150:
        birth_year = age_enter(input_age)
    elif 1900 < input_age <= current_year:
        birth_year = year_enter(input_age)

    else:
        print("Look like you are God kid")
        raise ValueError("Enter valid number")
except Exception as e:
    print(e)

else:
    nxt = input("Do ypu want to check yor age in particular year\nPress y :- yes\nPress N :- No")
    if nxt.capitalize() == "Y":
        year_enter = int(input("Enter year to check your age in particular year"))
        particular_yr(year_enter, birth_year)
    else:
        print("Live long")
