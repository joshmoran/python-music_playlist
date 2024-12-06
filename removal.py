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

create =  {'title': 'With Hearts Towards None', 'artist': 'Mgla', 'genre': 'Black Metal'}


# create =  {'title': 'With Hearts Towards None', 'artist': 'Mgla', 'genre': 'Black Metal'}
index_el = 0
for song in playlist:
    
    for key, value in song.items():
        if value == 'Angela of Death':
            print("matches:")
            playlist[index_el]['title'] =  'sonething something' 

            print(f"{key} - {value}")

    index_el += 1
    # if song['title'] == 'Angel of Death':
    #     song.update['title']



# playlist.append(create)

# del playlist[1]

print(playlist)

