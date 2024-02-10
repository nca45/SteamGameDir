"""
Helper functions for steam related functions
"""
import os
import vdf
import yaml

from .constants import STEAM_LOCATION

from thefuzz import fuzz

def find_steam_game_directory(game_name:str, fuzz_acceptance:int):
    """
    Attempts to find the game directory given a list of directories used by
    Steam to store games on
    """
    potential_candidates = []

    storage_directories = _get_steam_libraries()
    for storage in storage_directories:
        for game in os.listdir(storage):
            fuzz_amount = fuzz.WRatio(game.lower(), game_name.lower())
            if fuzz_amount >= fuzz_acceptance:
                potential_candidates.append(os.path.join(storage, game))
    return potential_candidates

def _get_steam_libraries():
    """
    returns a list of storage locations steam uses to install games
    """
    libraries = []
    steam_dir = STEAM_LOCATION
    libraryfolders_file = os.path.join(steam_dir, 'steamapps', 'libraryfolders.vdf')
    with open(libraryfolders_file, 'r') as f:
        libraryfolders = vdf.load(f)

    for index, data in libraryfolders['libraryfolders'].items():
        libraries.append(os.path.join(data['path'], 'steamapps', 'common'))

    return libraries