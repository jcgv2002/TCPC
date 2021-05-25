MENU_PROMPT = "\nEnter 'a' to add a movie, 'l' to see your movies, 'f' to find a movie by title, or 'q' to quit: "
movies = []


#   - adding movies
def add_movies():
    title = input("Enter the movie title: ")
    director = input("Enter the movie director: ")
    year = input("Enter the movie release year: ")

    movies.append({
        'title': title,
        'director': director,
        'year': year
    })


#   - listing movies
def list_movies():
    for movie in movies:
        print_movies(movie)


#   - printing movies
def print_movies(movie):
    print(f"Title: {movie['title']}")
    print(f"Director: {movie['director']}")
    print(f"Release year: {movie['year']}")


#   - finding movies
def find_movies():
    user_title = input("Enter the movie title: ")
    
    for movie in movies:
        title = movie['title']
        if title == user_title:
            print(f"You are lucky!. {user_title} is available")
            print_movies(movie)
            break
    else:
            print(f"Sorry!, {user_title} is not available yet")


user_options ={
    'a': add_movies,
    'l': list_movies,
    'f': find_movies
}

#   - user menu
def user_menu():
    selection = input(MENU_PROMPT)
    while selection != 'q':
        if selection in user_options:
            user_options[selection]()
        else:
            print('Unknown command. Please try again.')

        selection = input(MENU_PROMPT)


# Remember to run the user menu function at the end!
user_menu()