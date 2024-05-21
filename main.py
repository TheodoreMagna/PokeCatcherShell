#-------------------------
# Imports
#-------------------------
import subprocess
from random import randint

#-------------------------
# Config
#-------------------------
shiny_rate = 1  # (in %)
catch_rate = 50 # (in %)
team_size = 6   # (in nb of pokemons)

#-------------------------
# Check if Krabby is installed
#-------------------------
try:
    result = subprocess.run(['krabby', 'list'], stdout=subprocess.PIPE)
    pokemons = str(result.stdout).split("'")[1].split("\\n")
    pokemons.pop()
except:
    print("Error: Krabby not found")
    print("Install Krabby (https://github.com/yannjor/krabby) with : cargo install krabby")
    exit()

#-------------------------
# Pokemon Class
#-------------------------
class Pokemon():
    def __init__(self, name, shiny=False, level=1):
        self.name = name
        self.shiny = shiny
        self.level = level
    
    def __str__(self):
        return self.name

    def catch(self, team):
        if (randint(1, 100) >= catch_rate):
            print("You caught a " + self.name + " !")
            team.append(self)
        else:
            print("You failed to catch the " + self.name + " :/")
        input("Press Enter to continue...")

    def remove_from_team(self, team):
        if (self in team):
            team.remove(self)

    def show(self):
        args_list = ['krabby', 'name', self.name]
        if (self.shiny):
            args_list.append("-s")
            print("Shiny !")
        subprocess.run(args_list)

#-------------------------
# Tools
#-------------------------
def clear_terminal():
    subprocess.run("clear")

def show_team(team):
    clear_terminal()
    print("=============================================================")
    print("=============================================================")
    print("Your team:")
    for poke in team:
        poke.show()
    print("=============================================================")
    print("=============================================================")
    input("Press Enter to continue...")

#-------------------------
# Game Loop
#-------------------------
def get_action(pokemon, team):
    clear_terminal()
    pokemon.show()
    temp = input("List of actions:\n- 1: Catch\n- 2: Continue\n- 3: Show Team\n- 4: Exit\n")
    match temp:
        case ("1"):
            pokemon.catch(team)
            return
        case ("2"):
            return
        case ("3"):
            show_team(team)
        case ("4"):
            exit()
        case _:
            print("Invalid action")
    get_action(pokemon, team)

#-------------------------
# Main
#-------------------------
def main():
    team = []

    while (len(team) < team_size):
        nb = randint(0, len(pokemons) - 1)
        pokemon = Pokemon(pokemons[nb])

        if (randint(1, 100) > 100 - shiny_rate):
            pokemon.shiny = True

        get_action(pokemon, team)

    show_team()
    print("You have a full team !")

if __name__ == "__main__":
    main()