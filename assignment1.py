"""
Name: Gagandeep Kaur
Date started:10-12-2019
GitHub URL:https://github.com/JCUB-CP1404-SP23/a1-movies-to-watch-gagankarangill.git
"""

from operator import itemgetter

""""This function open a movies file and then read it.
and split it from ',' and append it to a empty list sorted_list.
In last, it returns the sorted_list
"""


def movies_file():
    in_file = open("movies.csv", "r")          # open the movies file #
    created_list = in_file.readlines()           # read all file lines
    sorted_movies = []                           # empty list
    for line in created_list:
        split_line = line.split(",")              # split the string from "," #
        split_line[1] = int(split_line[1])
        split_line[3] = split_line[3][0]
        sorted_movies.append(split_line)         # add movies into the empty list
        in_file.close()                         # close the file #
    return sorted_movies


# This function will sort the movies according to their year and then by title #
def get_sorted_movie_list(new_list):
    new_list.sort(key=itemgetter(1, 0))
    return new_list


# display_menu function ask for input and show a list of menu to list movies, add, watch and to quit #
def display_menu():
    print("L- List movies \n A- Add new movie \n W- Watch a movie \n Q- Quit")
    list = ["L", "A", "W", "Q"]                                 # List of choices #
    choice = input("Choose L, A, W, Q :\n").upper()
    while choice not in list:
        print("Invalid Menu Choice")
        choice = input("Choose L, A, W, Q :\n").upper()
    return choice


# watch movies function prints the sorted_movie_list with index and '*' with unwatched movies
def watch_movies(sorted_movies_list):
    for i in range(5):                              # to print index
        if 'u' in sorted_movies_list[i]:            # print * in unwatch movies
            print("{}.{:>3s} {} \t - {} ({})".format(i, "*", sorted_movies_list[i][0], sorted_movies_list[i][1],  sorted_movies_list[i][2],  sorted_movies_list[i][3]))
        else:                                       # print empty space in watched movies at the place of'*'
            print("{}.{:>3s} {} \t - {} ({})".format(i, " ", sorted_movies_list[i][0], sorted_movies_list[i][1],  sorted_movies_list[i][2],  sorted_movies_list[i][3]))


# this function calculate the watched movies by checking the condition if u in movies_list
def cal_watch_movies(created_movies_list):
    movies = 0
    for i in range(5):
        if 'u' in created_movies_list[i]:
            movies = movies+1
    return movies


# this function calculate the unwatched movies by checking the condition if u not in movies_list
def cal_unwatch_movies(created_movies_list):
    movies = 0
    for i in range(5):
        if 'u' not in created_movies_list[i]:
            movies = movies + 1
    return movies


# this function ask the user to input number for movie and then print the movie by checking it on movies list
def watch_to_unwatch(watch_movies):
    i = int(input("Please enter the number of movie to mark as watched:\n"))
    if i in watch_movies[i]:
        print(" watched this movie. Please choose another movie to watch")
    else:
        return watch_movies[i]


# adding_movies will take inputs for new movie
def adding_movies():
    title_of_movie = input("Please enter the title of movie :")            # ask for name of movie
    while not title_of_movie.isalpha():
        print("Invalid Input. Please enter valid value.")
        title_of_movie = input("Please enter the title of movie :")
    year_of_movie = input("Please enter the year for movie :")             # ask for year of movie
    while not year_of_movie.isdigit() or int(year_of_movie) <= 0:          # check the input
        print("Invalid Input.  Please enter valid value.")
        year_of_movie = input("Please enter the year for movie :")
    category_of_movie = input("Please enter the category of movie :")      # ask for category of movie
    while not category_of_movie.isalpha():
        print("Invalid Input.  Please enter valid value.")
        category_of_movie = input("Please enter the category of movie :")
    print("{} ({} from {}) added to movie list".format(title_of_movie, category_of_movie, year_of_movie))
    new_movie = ("{} , {} , {} , u".format(title_of_movie, year_of_movie, category_of_movie, ))
    return new_movie


def main():
    """This program will display the menu and then ask for input L to list movies, A to add movies, w to watch movie and Q to quit.
    It will display the sorted list according to their year and then by title and with '*' if it is unwatched
    """
    print("Movies To Watch 1.0 - by <Gagandeep Kaur>")

    new_list = get_sorted_movie_list(movies_file())               # gives sorted movie list
    m = cal_watch_movies(new_list)                                # calculate watched movie
    u = cal_unwatch_movies(new_list)                              # calculate unwatched movie
    added_list = new_list

    choice = display_menu()                                       # provide options to choose
    while choice != "Q":
        if choice == "L":                                         # shows menu option and print with watched and wumwatched movies
            watch_movies(new_list)
            print("Number of watched movies", m)                  # prints watched movie
            print("Number of unwatched movies", u)                # prints unwatched movie
            choice = display_menu()                               # again display the menu
        elif choice == "A":                            # add a new movie to a list by taking inputs
            aad = adding_movies()
            added_list.append(aad)                     # add a new movie to a list
            print(added_list)
            choice = display_menu()                   # again display the menu
            added_list = new_list
        elif choice == "W":                                  # prints a movie according to the index input
            proper_list = watch_to_unwatch(new_list)
            print(proper_list)
            print("you have watched the movie")
            choice = display_menu()
    print("Have a nice day:)")                   # print this message if user choose to quit


main()