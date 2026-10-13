from ut import cmd


playlist = ["Style", "yes", "Location", "Moves like jagger"]
playlist.append("POP OUT")
playlist.append("Arcade")



def show_playlist():

    if len(playlist) == 0:
        print("Your playlist is empty!")
        print("")

    else:

        for i in range(len(playlist)):
            print(f"{i+1} - {playlist[i]}")

        print("")



def help():
    print("q -> Quits program")
    print("h -> Displays help")
    print("a -> Adds a song to the playlist")
    print("r -> Removes a song from the playlist")
    print("c -> Clears the playlist")

    wait = input("\n")


running = True
while running:

    cmd.cls()
    show_playlist()

    key = input("What do you want to do? (h for help): ")
    cmd.cls()
    key = key.lower()

    match key:

        case "q":
            running = False

        case "h" | "help":
            help()

        case "a":
            song = input("Enter a song to add: ")
            playlist.append(song)

        case "r":
            song = input("Enter a song to remove: ")
            try:
                playlist.remove(song)

            except:
                print("Song not found in playlist")
                input("")

        case "c":
            choice = input("Are you sure you want to clear your playlist?: ")
            if choice in ["y", "yes", "ye", "yea"]:
                playlist.clear()

            else:
                pass

        case _:
            print("Enter a valid key")