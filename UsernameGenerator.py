import random

adjectives = ["Brave", "Swift", "Fancy", "Bright", "Cool", "Crazy", "Sharp", "Sweet", 
              "Giggling", "Hilarious", "Quirky", "Silly", "Witty", "Spunky", "Zany", 
              "Analytical", "Insightful", "Intelligent", "Predictive", "Innovative", 
              "Structured", "BigData", "Statistical", "Quantitative", "Algorithmic", 
              "Iron", "Silver", "Golden", "Super", "Mega", "Hyper", "Ultra", "Epic",
              "OldSchool", "Retro", "Vintage", "Star", "Cosmic", "Galactic"]

nouns = ["Lion", "Eagle", "Panda", "Shark", "Falcon", "Tiger", "Bear", "Wolf", 
         "Jester", "Prankster", "Clown", "Noodle", "Pickle", "Banana", "Doughnut", 
         "Statistic", "Algorithm", "Dataset", "Model", "Query", "Spreadsheet", 
         "Datapoint", "Array", "Matrix", "Function",
         "Gamer", "Nerd", "Geek", "Droid", "Jedi", "Sith", "Trooper", "Mutant",
         "Ranger", "Knight", "Wizard", "Elf", "Dwarf", "Orc", "Goblin", "Dragon"]

digits = list(range(0, 100))

def generate_username():
    adj = random.choice(adjectives)
    noun = random.choice(nouns)
    digit = random.choice(digits)
    username = f"{adj}{noun}{digit}"
    return username

def main():
    num_usernames = int(input("How many usernames do you want to generate? "))
    for _ in range(num_usernames):
        print(generate_username())

if __name__ == "__main__":
    main()