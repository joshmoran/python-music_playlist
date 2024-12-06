# Music Playlist App

## This is an assignment for 'JustIT' within their technical training for Python
- Please see 'Project Brief.pdf' for full project details that this script must meet 
- Overview
- [x] 1. Understanding python dictionaries 
- [x] 2. Setting up a playlist
- [x] 3. Adding songs to the playlist
- [x] 4. Viewing the playlist
- [x] 5. Updating song information
- [x] 6. Deleting a song from the playlist 

# Overview and Error Handling 
## On startup
### Overview 
- The user is greeted and welcomed
- The user is told what they can do with this script 
  - view, search, add, remove, or edit songs 
- From here to the main menu 

## Main Menu 
### Overview 
- Three options for the user to enter
  1. View and Search 
  2. Make a change
  3. Exit the script

### Error Handling 
- If the user does not click a valid number (1, 2 or 3), the input is repeated until they enter a valid number
- Based on their action depends on which screen they are navigated to 
  1. View and Search = Search Sub Menu
  2. Make a change = Change Sub Menu 
  3. Exit the script = The user is thanked and the script is exited and return back to the command line

## Search Sub Menu 
### Overview 
- The user has 4 options
  1. View the playlist 
  2. Search by genre
  3. Search by artist
  4. Return to the main menu 

### Error Handling 
- If the user does not click a valid number (1, 2, 3 or 4), the input is repeated until they enter a valid number
- Based on their action depends on which screen they are navigated to 
  1. View the playlist = Function: View the playlist
  2. Search by genre = Function: Search By Genre
  3. Search by artist = Function: Search By Artist
  4. Return to the main menu = Returns back to the main menu 

## Change Sub Menu 
### Overview 
- The user has 4 options
  1. Add a song 
  2. Remove a song
  3. Edit a song
  4. Return to the main menu 

### Error Handling 
- If the user does not click a valid number (1, 2, 3 or 4), the input is repeated until they enter a valid number
- Based on their action depends on which screen they are navigated to 
  1. Add a song = Function: Add a song
  2. Remove a song = Function: Remove a song
  3. Edit a song = Function: Edit a song 
  4. Return to the main menu = Returns back to the main menu 
   
## Functions 
### View the Playlist 
#### Overview 
- Headers are printed and then the playlist is printed out to the user
- Once completed it returns the user back to the main menu 

### Search By Genre
#### Overview 
- An input is shown asking the user to enter a genre they want to search for 
- Once complete and results are returned, a new menu is shown
  1. Search for another Genre
  2. Return to the main menu 
  3. Return to the view menu 

#### Error Handling
- Depending on their being:
  - Result/s = They are shown to the user 
  - If no results = a message saying 'no songs have been found'
- Once complete and the menu is shown, they go to the following functions 
  1. Search for another Genre = Function: Search by Genre
  2. Return to the main menu = Function: Main Menu 
  3. Return to the view menu = Function: Search Sub Menu
- During the new menu, only a valid number (1, 2 or 3) will be accepted, otherwise it re-asks for the users input 

### Search By Artist
#### Overview 
- An input is shown asking the user to enter a artist they want to search for 
- Once complete and results are returned, a new menu is shown
  1. Search for another artist
  2. Return to the main menu 
  3. Return to the view menu 

#### Error Handling
- Depending on their being:
  - Result/s = They are shown to the user 
  - If no results = a message saying 'no songs have been found'
- Once complete and the menu is shown, they go to the following functions 
  1. Search for another artist = Function: Search by artist
  2. Return to the main menu = Function: Main Menu 
  3. Return to the view menu = Function: Search Sub Menu
- During the new menu, only a valid number (1, 2 or 3) will be accepted, otherwise it re-asks for the users input 

### Add a song
#### Overview 
- Allow the user to add a song to the playlist 
- Once selected, the user is notified that 3 things are required
  1. Title 
  2. Artist 
  3. Genre 
- Once these details are added, the user is shown what they have types and they are used if they are correct
  - Yes or No
- Once correct details are added and they say 'Yes', the user is returned to the Change Sub Menu

#### Error Handling
- Each input ( Title, Artist, Genre ) are done one by one, 
- Checks if the input is empty, if it is then repeat the input 
  - Message - 'The artist cannot be empty' 
- Once these three elements are submitted the user is asked if they are correct
  - Y for yes, N for n
  - If yes, 
    - The new entry is added to the playlist 
    - A message shows it has been completed successfully
    - The user is returned to the Change Sub Menu 
  - If no, 
    - The user completed the initial three inputs (title, artist, genre)
  
### Remove a song
#### Overview 
- On start, the user is asked for how they want to search for an entry
  - Title 
  - Artist
  - Genre
- The user select one and asked what they want to search for 
  
#### Error Handling
- The title, artist, genre are indexed (1,2 or 3), the user must enter a valid number or it will repeat and re-ask the user
- Using one of the three (title, artist, genre) options the user must enter their search requirements
  - If empty, the question/search query is repeated until it is not empty 
- Based on the results, they are modified 
  - If 1 Entry is found
    - The user is asked to confirm: Y for Yes, N for no
      - If Yes
        - The entry is removed from the playlist 
        - A new menu is showed
            1. Delete another song = Function: Remove a song 
            2. Go to the change menu = Function: Change Sub Menu 
            3. Go to the main menu = Function: Main Menu 
        - User must enter a valid number or the menu will be repeated until a valid number is picked
      - If No,
        - The user will re-enter there search query and go through the process 
  - If more than 1 entry is found, 
    - The results are printed out tot he user and the user has to select the index value (at the start of each entry)
    - Additionally, they can choose to cancel and return to the main menu
  - Checking 

### Edit a song 
#### Overview 
- On start, each entry of the playlist is shown with an index value 
- User must select an entry and confirm it is correct
- Once an entry has been selected, the user is asked which part of the entry they want to chang:
  1. Title
  2. Artist
  3. Genre
- AFter selecting the title, artist or genre 
- User types the new value
- 
#### Error Handling

- When picking a song:
  - if the number selected is greater than the number of items in the playlist, the user is re-asked for their input 
  - If the input is empty, the user is re-asked for their input 
- Once picked a song, the user is shown their selection and asked if this is correct
  - If Yes, then the user moves on to pick the title, artist or genre 
  - If No, the user starts at the start of editing a song function
  - Input must be each 'y' or 'n'
  - If empty, the user is re-asked for their input
- When picking which part of the entry they want to change (title, artist or genre), each one has a index value (1, 2 or 3)
  - User must select a valid number (1, 2 or 3), if not the menu is re-shown and their input will be re-asked for 
- 