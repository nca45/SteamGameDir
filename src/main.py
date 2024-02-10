import argparse

from .steam_config_util import find_steam_game_directory
from .util import open_steam_directory

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument('game_name',
                        type=str,
                        nargs='+',
                        help="The name of the steam game installed on Steam"
                        )
    parser.add_argument('--fuzz', 
                        '-f', 
                        type=int, 
                        required=False, 
                        default=90,
                        help="""Fuzz factor to match game_name argument with the directory's actual name.
                        Increase fuzz to make matching more strict. Too high may cause the program to require an exact match.
                        Decrease fuzz to make matching more lenient. Too low may cause the program to return multiple candidates to choose from.
                        Default is at 90.
                        """)

    args = parser.parse_args()
    game_name = " ".join(args.game_name)
    candidates = find_steam_game_directory(game_name, args.fuzz)
    open_steam_directory(candidates)

if __name__ == "__main__":
    main()
