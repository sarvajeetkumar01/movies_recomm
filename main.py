import json
import random
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
MOVIES_FILE = BASE_DIR / "data" / "movies.json"


def load_movies():
    """Load movie categories and movie names from JSON."""
    with open(MOVIES_FILE, "r", encoding="utf-8") as file:
        return json.load(file)


def display_movies(category, movies):
    """Display five randomly selected movies."""
    selected_movies = random.sample(movies[category], 5)

    print("\n" + "=" * 55)
    print(f"       5 RECOMMENDED {category.upper()} MOVIES")
    print("=" * 55)

    for number, movie in enumerate(selected_movies, start=1):
        print(f"{number}. {movie}")

    print("=" * 55)


def main():
    movies = load_movies()

    print("\n" + "=" * 55)
    print("       WELCOME TO MOVIE RECOMMENDATION SYSTEM")
    print("=" * 55)

    while True:
        print("\nWhich category of movies do you want to watch?")
        print("1. Action")
        print("2. Romance")
        print("3. Drama")
        print("4. Horror")
        print("5. Exit")

        choice = input("\nEnter your choice (1-5): ").strip()

        categories = {
            "1": "action",
            "2": "romance",
            "3": "drama",
            "4": "horror"
        }

        if choice in categories:
            category = categories[choice]
            display_movies(category, movies)

            again = input("\nWould you like another 5 recommendations? (y/n): ").strip().lower()
            if again != "y":
                print("\nThanks for using Movie Recommendation System! 🎬")
                break

        elif choice == "5":
            print("\nThanks for using Movie Recommendation System! 🎬")
            break

        else:
            print("\nInvalid choice. Please enter a number from 1 to 5.")


if __name__ == "__main__":
    main()
