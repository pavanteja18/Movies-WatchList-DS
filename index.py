from datetime import datetime


def get_date(val, allow_default=False):
    date_str = input(val)
    if allow_default and not date_str:
        return datetime.today().strftime('%d-%m-%Y')

    try:
        valid_date = datetime.strptime(date_str, '%d-%m-%Y')
        return valid_date.strftime('%d-%m-%Y')
    except ValueError:
        print("Not a valid date. Enter date in format dd-mm-yyyy.")
        return get_date(val, allow_default)


# print(get_date("Enter the date in dd-mm-yyyy -> "))

def get_movie_name():
    name = input("Enter movie's name: ")
    return name


# print(get_movie_name())

def get_genre():
    movie_genre = input("Enter movie's main genre: ")
    return movie_genre


# print(get_genre())

def get_movie_rating():
    try:
        movie_rating = float(input("Enter movie's rating (0-5): "))
        if movie_rating < 0 or movie_rating > 5:
            raise ValueError("Invalid movie's rating must be in the range 0 to 5.")
        return movie_rating
    except ValueError as e:
        print("Invalid Entry. Value must be in the range 0 to 5.")
        return get_movie_rating()


# print(get_movie_rating())
