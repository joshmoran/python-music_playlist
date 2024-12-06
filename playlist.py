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

def init():
    print("")
    print("Hello and welcome to your 'music playlist'")
    print("You can view, search, add, remove, or edit songs in your playlist")
    menu()


def menu():
    print("")
    print("Please choose from one of the following")
    print("")
    print("1. View and search")
    print("2. Make a change ")
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
                exit()
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
                change_song( 'remove' )
            elif user_choice == 3:
                change_song( 'edit' )
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

def validate_changes( ):
    validated = False

    while not validated:
        user_choice = input(">>> ")

        match user_choice:
            case "1":
                validated = True
                add_song()
            case "2":
                validated = True
                remove_song()
            case "3":
                validated = True
                change_song( 'edit' )
            case "4":
                validated = True
                menu()
            case _:
                print("Invalid choice. Please try again.")
                validate_changes()

def add_song():
    print("")
    print("Adding a song to the playlist")
    print("")
    print("In order to add an entry to the playlist, we will need 3 things")
    print("1. Title of the song")
    print("2. Artist of the song")
    print("3. Genre of the song")
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
    print("Y. Yes")
    print("N. No")
    while not user_happy:
        print("")
        user_choice = input(">>> ").lower()

        match user_choice:
            case "y":
                user_happy = True
                submit_song(final_title, final_artist, final_genre)
            case "n":
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

def change_song( page ):
    global playlist
    index_no = 1
    print("")
    if page == 'remove':
        print("So, we are:")
        print("Removing a song from the playlist")
        print("")
        print("Please choose one of the following:")
        print("1. Title")
        print("2. Artist")
        print("3. Genre")
        print("")
        validate_change( page )
    elif page == 'edit':
        print("So, we are:")
        print("Editing a song in the playlist")
        print("")
        print("Before we can edit a song, which entry do you want to change? ")
        print("")
        print(f"Index - Title - Artist - Genre")
        for song in playlist:
            print(f"{index_no}: {song['title']} - {song['artist']} - {song['genre']}")
            index_no = index_no + 1 
        print("")
        print("Which song do you want to edit?")
        print("")
        validate_change_song()

def validate_change_song():
    global playlist 

    try:
        user_input = int( input(">>> ") )
        if user_input <= len(playlist):
            print("")
            selected_song = playlist[int(user_input) - 1]
            print(f"You have chosen: {selected_song['title']} - {selected_song['artist']} - {selected_song['genre']}")
            print("")
            print("Is this correct?")
            print("")
            print("Y: Yes")
            print("N: No")
            validate_edit( selected_song )
        else:
            print("")
            print("Invalid choice. Please enter a valid index.")
            validate_change_song()
    except ValueError:
        print("")

def validate_edit( selected_song = '' ):
    validated = False 

    while not validated:
        print("")
        user_choice = input(">>> ").lower()
        print(f"The user selected {user_choice}")
        match user_choice:
            case "y":
                validated = True
                print("")
                print("Okay we will edit this song entry")
                print("")
                print("Okay, which part do you want to change? ")
                print("")
                print("1. Title")
                print("2. Artist")
                print("3. Genre")
                print("")
                validate_change( 'edit', selected_song )
            case "n":
                print("You selected no")
                print("")
                print("Lets try this again")
                validated = True
                change_song( 'edit' )
            case _:
                print("Invalid choice. Please try again.")
                validate_edit( selected_song )
        

def make_edit_song( item, song, user_choice ):
    global playlist 

    found = False
    index_el = 0

    for key, value in song.items():
        if key == item:
            key_to_change = value
    for entry in playlist:
        for key, value in entry.items():
            if value == key_to_change:
                print("")
                playlist[index_el][item] =  user_choice
                print(f"Successfully changed the {item} to {user_choice}")
                found = True
                after_change( 'edit' )
        index_el += 1

    if found == False:
        print(f"No songs found with the name of {user_input}")
        after_change(page )

def validate_make_edit( field, song ):
    validated = False 

    while not validated:
        print(f"Please enter the new {field}")
        user_choice = input(">>> ")
        print("")
        print(f"The user selected {user_choice}")
        if user_choice == '':
            print("The new {field} must not be empty")
            validated = True
            validate_make_edit( field, song )
        else:
            make_edit_song( field, song, user_choice )

def edit_by( type, page ):
    global playlist
    found_items = []
    validated = False

    if page == 'remove':
        print(f"Please enter the name of the {type} to remove")
    elif page == 'edit':
            print(f"Please enter the name of the {type} to edit")
    print("")
    user_input = input(">>> ").lower()
    print("")
    index_val = 0

    for song in playlist:
        if user_input in song[type].lower() :
            found_items.append(song)
            index_val += 1

    if len(found_items) == 0:
        print(f"No songs found with the name of {user_input}")
        after_change( page )
    elif len(found_items) == 1:
        print(f"Okay, we have found 1 entry matching the {type} and name of {user_input}")
        print("")

        print(f"{found_items[0]['title']} - {found_items[0]['artist']} - {found_items[0]['genre']}")

        print("")
        print("Is this correct?, please confirm:")
        print("")
        print("Y. Yes")
        print("N. No")
        print("")
        confirmed = False
        while not confirmed:
            confirm_delete = input(">>> ").lower()

            match confirm_delete:
                case "y":
                    try:
                        confirmed = True
                        index_val = 0
                        print("this should be running")
                        index_val = 0
                        for song in playlist:

                            if found_items[0] == song:
                                print( page )
                                if page == 'edit':
                                    print("To change a song")
                                elif page == 'remove':
                                    print(f"So we have dropped {found_items[0]}")
                                    del playlist[ index_val ] 
                            index_val += 1 

                                
                    except:
                        print("An error has occurred, could not remove the song")
                    finally:
                        after_change( page )
                case "n":
                    confirmed = True
                    print("")
                    print("Okay, we will go through again")
                    print("")
                    print(f"What is the name of the {type} you want to remove?")
                    print("")
                    validate_change( 'remove' )
                case _: 
                    print("Invalid choice. Please try again.")
    else:   
        confirm_change( found_items, page)

def confirm_change( array, page ):
    index_val = 1

    print(f"Okay we have found songs to {page}")
    print("")
    print("Here are the songs:")
    for item in array:
        print(f"{index_val}: {item['title']} - {item['artist']} - {item['genre']}")
        index_val += 1 
    if page == 'edit':
        print(f"{index_val}: Cancel Editing and Return to the Main Menu ")
    elif page =='remove':
        print(f"{index_val}: Cancel Delete and Return to the Main Menu ")
    print("")
    validate_batch( array, page )


def validate_batch( array, page ):
    global playlist 

    validated = False

    print("Please enter a number to continue ")
    while not validated:
        try:
            user_choice = int( input(">>> ") )
            
            if user_choice == len(array) + 1:
                print("")
                print("Okay, we will go back to the main menu")
                print("")
                menu()
            elif user_choice  in range(1, len(array) + 1 ):
                validated = True
                confirm_batch( array[user_choice - 1 ], page )
            else: 
                print("Invalid choice. Please enter a number between 1 and", ( len(array) + 1 ))
                print("")
                validate_batch( array, page )
        except ValueError:
            print("It must be an integer")

def confirm_batch( to_delete, page ):
    global playlist

    index_val = 0 

    if page == 'remove':
        for song in playlist:
            if song['title'] == to_delete['title'] or song['artist'] == to_delete['artist'] or song['genre'] == to_delete['genre']:
                del playlist[index_val]
                print(f"Song '{to_delete['title']}' by '{to_delete['artist']}' removed successfully.")
            index_val += 1
    after_change( page )

def after_change( page):
    print("")
    print("Here are your options: ")
    print("")
    if page == 'remove':
        print("1. Delete another song")
    elif page == 'edit':
        print("1. Edit another song")
    print("2. Go to change menu")
    print("3. Go to main menu")
    print("")
    while True:
        user_choice = input(">>> ").lower()

        match user_choice:
            case "1":
                print("")
                if page == 'remove':
                    print("Okay, we will delete the song")
                elif page == 'edit':
                    print("Okay, we will edit the song")
                print("")
                change_song( page )
            case "2":
                print("")
                print("Okay, we will go to the change menu")
                print("")
                menu_change()
            case "3":
                print("")
                print("Okay, we will go back to the main menu")
                print("")
                menu()
            case _:
                print("Invalid choice. Please try again.")
                after_change( page )
            
def validate_change( page, item = '' ): 
    validated = False
    while not validated:
        user_choice = input(">>> ")

        match user_choice:
            case "1":
                validated = True
                print("")
                if page == 'edit' :
                    print("You have chosen to edit the title")
                    print("")
                    validate_make_edit( 'title', item )
                elif page == 'remove':
                    edit_by( 'title', page )
            case "2":
                validated = True
                print("")
                if page == 'edit':
                    print("")
                    print("You have chosen to edit the artist")
                    print("")
                    validate_make_edit( 'artist', item )
                elif page == 'remove':
                    edit_by( 'artist', page )
            case "3":
                validated = True
                print("")
                # if array ==
                if page == 'edit':
                    print("")
                    print("You have chosen to edit the genre")
                    print("")
                    validate_make_edit( 'genre', item )
                elif page == 'remove':
                    edit_by( 'genre', page )
            case _:
                print("Invalid choice. Please try again.")
                validate_change( page )



init()