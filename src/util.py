"""
Helper functions for opening steam directories
"""
import os

def open_steam_directory(candidates:list):
    if not candidates:
        print(f"Couldn't find the game directory... Try lowering the fuzz setting or check for typos")
        return
    elif len(candidates) == 1:
        chosen_directory = candidates[0]
    else:
        print("Multiple candidates found:")
        for i, candidate in enumerate(candidates, start=1):
            print(f"{i}. {candidate}")

        loop =  True
        while loop:
            choice = input("Select the desired game by typing in the desired index: ")
            try:
                chosen_directory = candidates[int(choice)-1]
                loop = False
            except:
                print("Invalid choice, please try again")
        
    print(f"Opening {chosen_directory}...")
    os.startfile(chosen_directory)