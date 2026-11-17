from ut import cmd

playlist: list[str] = ["Blinding Lights", "Bad Guy", "Shape of You"]
filler: list[str] = ["of", "a", "the"]
running: bool = True

def cap_song(song: str) -> str:
    words = song.split()
    final: str = ""

    for i in range(len(words)):
        if words[i] in filler:
            final = words[i] = " "

        else:
            final = final + words[i].capitalize() + " "

    return final.removesuffix(" ")


def queue(song: str) -> None:
    global playlist
    song = cap_song(song)
    playlist.append(song)

def ins_queue(song: str, pos: int) -> None:
    global playlist
    song = cap_song(song)
    playlist.insert(pos, song)

def remove_song(song: str) -> None:
    global playlist
    song = cap_song(song)

    if song in playlist:
        playlist.remove(song)

    else:
        print(f"{song} not in playlist")

def last_played() -> str:
    global playlist
    last = playlist.pop(0)
    playlist.insert(0, last)
    return last

def sort_alph(reverse: bool=False) -> list[str]:
    global playlist

    if reverse:
        return playlist.sort(reverse=True)

    return playlist.sort()

def check_playlist(song: str) -> None:
    song = cap_song(song)
    position: int = -1

    if song in playlist:
        position = playlist.index(song)
        print(f"{song} in playlist at position {position+1}")

    else:
        print(f"{song} not in playlist")


def main():
    print("Choose an option")
    print("1. Add a song")
    print("2. Insert a song")
    print("3. Remove a song")
    print("4. Check last played song")
    print("5. Sort playlist")
    print("6. Check where a song is in playlist")
    print("7. Quit\n")
    print("Playlist: ")
    print(*playlist, sep=", ")

    choice = input("-> ")
    print("")

    match choice:
        case "1":
            song = input("Enter the song name: ")
            queue(song)
            input("Added")
        case "2":
            song = input("Enter the song name to insert: ")
            try:
                pos = int(input("Enter the position: "))
            except:
                input("Position must be an int")

            ins_queue(song, pos)
            input("Added")
            
        case "3":
            song = input("Enter the song name to remove: ")
            remove_song(song)
            input("")

        case "4":
            print(f"The last played song was {last_played()}")
            input("")

        case "5":
            print("1. Sort alphabetically")
            print("2. Sort reverse-alphabetically")
            try:
                choice = int(input("Enter 1 or 2: "))
                if choice == 1:
                    sort_alph()
                elif choice == 2:
                    sort_alph(reverse=True)

                else:
                    print("Pick either 1 or 2")

            except:
                print("Input must be an int")
                input("")

        case "6":
            song = input("Enter the song name: ")
            check_playlist(song)
            input("")

        case "7":
            running = False

        case _:
            input("Enter a valid choice")

    cmd.cls()

while running:
    main()