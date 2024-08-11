import pandas as pd
import csv
from datetime import datetime
from index import get_date, get_genre, get_movie_rating, get_movie_name
import matplotlib.pyplot as plt


class CSV:
    CSV_File = "Movies_Rating.csv"

    @classmethod
    def initialize_csv(cls):
        try:
            pd.read_csv(cls.CSV_File)
        except FileNotFoundError:
            df = pd.DataFrame(columns=['Date', 'Movie_Name', 'Genre', 'Rating'])
            df.to_csv(cls.CSV_File, index=False)

    @classmethod
    def add_entry(cls, date, movie_name, genre, rating):
        new_entry = {
            "Date": date,
            "Movie_Name": movie_name,
            "Genre": genre,
            "Rating": rating
        }
        with open(cls.CSV_File, 'a', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=['Date', 'Movie_Name', 'Genre', 'Rating'])
            writer.writerow(new_entry)
        print("Entry Added!!")

    @classmethod
    def get_movie_range(cls, start_date, end_date):
        df = pd.read_csv(cls.CSV_File)
        df['Date'] = pd.to_datetime(df['Date'],format="%d-%m-%Y")  # formatting the dates in the dataset into that format
        start_date = datetime.strptime(start_date, "%d-%m-%Y")
        end_date = datetime.strptime(end_date, "%d-%m-%Y")

        filtered_df = df.loc[(df['Date'] >= start_date) & (df['Date'] <= end_date)]

        if filtered_df.empty:
            print("No entries found, between this range")
            return None
        else:
            print(f"You watching between {start_date.strftime('%d-%m-%Y')} and {end_date.strftime('%d-%m-%Y')}")
            print(filtered_df.to_string(index=False))

            print("\nYour Watch History:")
            total_movies = filtered_df['Movie_Name'].count()
            print("Total Viewed Movies is/are: ", total_movies)
            avg_rating = filtered_df['Rating'].mean()
            print(f"Average Rating is: {avg_rating:.2f}")
            return filtered_df


def add():
    CSV.initialize_csv()
    date = get_date("Enter the Date when you watched the movie in (dd-mm-yyyy): ", allow_default=True)
    movie_name = get_movie_name()
    genre = get_genre()
    rating = get_movie_rating()
    CSV.add_entry(date, movie_name, genre, rating)


def plot_range(df):
    if df is not None:
        df.set_index("Movie_Name", inplace=True)

        plt.figure(figsize=(10, 5))

        df['Rating'].plot(kind='bar', color='red')

        plt.legend()
        plt.xlabel("Movies")
        plt.ylabel("Rating")
        plt.title("Your Watch List")
        plt.grid(True)
        plt.tight_layout()
        plt.show()
    else:
        print("No Data available to plot")


def main():
    while True:
        print("\nWelcome to your Movie Watch List:")
        print("1. Add a movie")
        print("2. View your Watch List")
        print("3. Exit")
        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            add()
        elif choice == '2':
            start_date = get_date("Enter the Start Date in format dd-mm-yyyy: ")
            end_date = get_date("Enter the End Date in format dd-mm-yyyy: ")
            CSV.get_movie_range(start_date, end_date)
            if input("Do you want a visual representation of the movies? (y/n): ").lower() == 'y':
                plot_range(CSV.get_movie_range(start_date, end_date))

        elif choice == '3':
            print("Thank you for visiting...")
            break


if __name__ == "__main__":
    main()
