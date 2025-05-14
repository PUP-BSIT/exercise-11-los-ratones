import random
import pyfiglet

def movie():
    banner = pyfiglet.figlet_format("Movie Rater")
    print(banner)

    name = input("What's your name?: ")
    movie = input("What's your favorite movie?: ")

    if movie.strip() == "":
        print("Good bye")
    else:
        response = random.choice([
            f"{name}, this movie is absolute cinema!",
            f"{name}, this movie is trash"
        ])
        print(response)

