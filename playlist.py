#  ‘title’, ‘artist’, and ‘genre’
playlist = [
    { 
        "title": 'Panzer Division Marduk', 
        "artist": 'Marduk', 
        "genre": 'Black Metal'
    },
    { 
        "title": 'With Hearts Towards None', 
        "artist": 'Mgla', 
        "genre": 'Black Metal'
    },
    { 
        "title": 'Unforgiven I', 
        "artist": 'Metallica', 
        "genre": 'Metal'
    },
    { 
        "title": 'Living on a prayer', 
        "artist": 'Bon Jovi', 
        "genre": 'Rock'
    },
    { 
        "title": 'Angela of Death', 
        "artist": 'Slayer', 
        "genre": 'Thrash Metal'
    },
    { 
        "title": 'Your Treachery Will Die With You', 
        "artist": 'Dying Fetus', 
        "genre": 'Death Metal'
    }
]


def menu():
    print("")
    print("Please choose from one of the following")
    print("")
    print("1. View the playlist")
    print("2. Make a change to the playlist")
    print("3. Exit")
    print("")
    validate_menu()

def menu_change():
    print("")
    print("In order to make a change")
    print("")
    print("Please choose one of the following actions:")
    print("")
    print("1. Add a song")
    print("2. Remove a song")
    print("3. Edit a song")
    print("4. Return to main menu")
    print("")
    validate_change_menu()

def menu_view():
    print("")
    print("Which view would you like")
    print("")
    print("1. View the playlist")
    print("2. Search by a genre")
    print("3. Search by an artist")
    print("4. Return to main menu")
    print("")
    validate_view_menu()

def validate_menu():
    has_validated = False
    
    while not has_validated:
        try:
            user_choice = int(input("Enter your choice: "))
            
            if user_choice == 1:
                menu_view()
            elif user_choice == 2:
                menu_change()
            elif user_choice == 3:
                print("Thank you for using 'Music Playlist'")
                has_validated = True
            else:
                print("Invalid choice. Please try again.")
                validate_menu()
        except ValueError:
            print("Invalid choice. Please enter a number.")
            validate_menu()

def validate_change_menu():
    has_validated = False
    
    while not has_validated:
        try:
            user_choice = int(input("Enter your choice: "))
            
            if user_choice == 1:
                add_song()
            elif user_choice == 2:
                remove_song()
            elif user_choice == 3:
                edit_song()
            elif user_choice == 4:
                menu()
            else:
                print("Invalid choice. Please try again.")
                validate_change_menu()
        except ValueError:
            print("Invalid choice. Please enter a number.")
            validate_change_menu()

def validate_view_menu():
    has_validated = False
    
    while not has_validated:
        try:
            user_choice = int(input("Enter your choice: "))
            
            if user_choice == 1:
                view_playlist()
            elif user_choice == 2:
                search_by( 'genre' )
            elif user_choice == 3:
                search_by( 'artist' )
            elif user_choice == 4:
                menu()
            else:
                print("Invalid choice. Please try again.")
                validate_view_menu()
        except ValueError:
            print("Invalid choice. Please enter a number.")
            validate_view_menu()

def view_playlist():
    print("")
    print("Here is your playlist")
    print("")
    print("Title - Artist - Genre")
    for song in playlist:
        print(f"{song['title']} - {song['artist']} - {song['genre']}")
    menu_view()

def search_by ( type ):
    if type == 'artist':
        search_by = type
    elif type == 'genre':
        search_by = type
    else:
        menu()
        return 

    has_validated = False
    has_results = False
    index_val = 0
    song_array = {}

    print("")
    print(f"Enter a {search_by}: ")
    user_genre = input(">>> ").lower()
    print("")
    print(f"Your chosen {search_by} is {user_genre}")
    print("")
    for song in playlist:
        if user_genre == song[search_by].lower():

            song_array[ index_val ] = ( song['title'],  song['artist'],  song['genre'])
            index_val += 1
        else: 
            has_results = True
    if len(song_array) == 0:
        if search_by == 'artist':
            print(f"No songs found by this artist.")
        elif search_by == 'genre':
            print(f"No songs found in this genre.")
    else:
        print(f"Songs found in this {search_by}:")
        print("")
        print(" --- Title --- Artist --- Genre --- ")
        for song in song_array.values():
            print(f"{song[0]} - {song[1]} - {song[2]}")
    print("")
    print(f"Do you want to search for another {search_by} or go back to the main menu?")
    print("")
    print(f"1. Search another {search_by}")
    print("2. Return to main menu")
    print("3. Return to the viewing menu")
    print("")
    validate_search( type )

def validate_search( type ):
    validated = False

    while not validated:
        user_choice = input(">>> ")

        match user_choice:
            case "1":
                validated = True
                search_by( type )
            case "2":
                validated = True
                menu()
            case "3":
                validated = True
                menu_view()
            case _:
                print("Invalid choice. Please try again.")
                validate_search ( type )


def add_song():
    print("")
    print("Adding a song to the playlist")
    print("")
    print("In order to add an entry to the playlist, we will need 3 things")
    print("1. Title of the song")
    print("2. Artist of the song")
    print("3. Genre of the song")
    print("")
    validate_add_song()

def validate_add_song():
    no_of_entries = 3
    currently_on = 1

    final_title = ''
    final_artist = ''
    final_genre = ''

    user_happy = False

    while currently_on <= no_of_entries:
         
        validated = False

        while not validated:
            current_title = ''
            match currently_on:
                case 1:
                    current_title = 'title'
                case 2:
                    current_title = 'artist'
                case 3:
                    current_title = 'genre'
        
            try: 
                print("")
                print(f"Enter the {current_title}: ")
                user_input = input(">>> ")
                if len(user_input) > 0:
                    validated = True
                    match currently_on:
                        case 1:
                            final_title = user_input
                        case 2:
                            final_artist = user_input
                        case 3:
                            final_genre = user_input
                    currently_on += 1
                else:
                    print(f"The {current_title} cannot be empty.")
            except ValueError:
                print(f"Invalid input. Please enter a non-empty string.")
    print("")
    print("Okay you have chosen: ")
    print(f"Title: {final_title}")
    print(f"Artist: {final_artist}")
    print(f"Genre: {final_genre}")
    print("")
    print("Is this correct?")
    print("")
    print("1. Yes")
    print("2. No")
    print("")
    while not user_happy:
        print("")
        user_choice = input(">>> ")

        match user_choice:
            case "1":
                user_happy = True
                submit_song(final_title, final_artist, final_genre)
            case "2":
                user_happy = True
                print("")
                print("Okay, we will go through again")
                print("")
                validate_add_song()
            case _:
                print("Invalid choice. Please try again.")


   

def submit_song( title, artist, genre):

    try:
        playlist.append( { "title": title, "artist": artist, "genre": genre } )
        print("Song added successfully.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
    menu_change()

def remove_song():
    print("")
    print("Removing a song from the playlist")
    print("")
    print("In order to remove an entry from the playlist, we will need search it either of 3 things")
    print("1. Title of the song")
    print("2. Artist of the song")
    print("3. Genre of the song")
    print("")
    validate_remove()

def remove_by( type ):
    global playlist

    print("")
    print(f"Please enter the name of the {type}to remove")
    print("")
    user_input = input(">>> ").lower()
    
    for song in playlist:
        if user_input == song[type].lower():
            playlist.remove(song)
            print(f"Song '{song[type]}' has been removed from the playlist.")
            validated = True
        else:
            print("")
            print(f"We found no {type} with the name of {user_input}")
            print("")
            print("Lets try that again")
            remove_by( type )

def validate_remove(): 
    validated = False
    while not validated:
        user_choice = input(">>> ")

        match user_choice:
            case "1":
                validated = True
                remove_by( 'title ')
            case "2":
                validated = True
                remove_by( 'artist' )
            case "3":
                validated = True
                remove_by( 'genre' )
            case _:
                print("Invalid choice. Please try again.")
                validate_remove()

def edit_song():
    print("Edit Song")



remove_song()
# menu_view() 