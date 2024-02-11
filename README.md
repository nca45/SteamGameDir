# SteamGameDir
Tired of going through Steam to browse your game's local directory?

Hopefully this simple cli will help you out lmao

This cli searches through the partitions Steam uses to install games on and attempts to open the game's local directory

## Installation

Clone the repo

Navigate to `./SteamGameDir/`

Navigate to `src/constants.py` and modify the variable to match your Steam install location.

```python
STEAM_LOCATION = <Your steam installation path>
```

Go back up to `./SteamGameDir/` and Use the package manager pip to install

```bash
pip install .
```

## Usage

Open a game's local Steam directory
```bash
SteamGameDir Cyberpunk2077

```

Search for a game directory and tune the match 'fuzziness' to be more strict or more forgiving:
```bash
SteamGameDir Baldur's Gate 3 --fuzz 100
```
a fuzz of `100` will only search for an exact match (case insensitive), while a fuzz of `0` will return all installed games (don't do that)

If there are multiple matches, the cli will prompt you to pick a game directory:

```bash
> SteamGameDir Jackbox
Multiple candidates found:
1. C:\Program Files (x86)\Steam\steamapps\common\The Jackbox Party Pack 3
2. C:\Program Files (x86)\Steam\steamapps\common\The Jackbox Party Pack 4
3. C:\Program Files (x86)\Steam\steamapps\common\The Jackbox Party Pack 5
Select the desired game by typing in the desired index: 3

```
