import os
import random
import sys


####################
# Player Definition
####################
class Player:
    def __init__(self):
        self.name = ''
        self.background = ''
        self.skills = {'Networking': 3, 'Problem-Solving': 3, 'Resilience': 3, 'Time Management': 3}
        self.energy = 100
        self.reputation = 50
        self.completed_challenges = 0
        self.current_position = 'center'
        self.level = 1
        self.goal_achieved = False

player = Player()

####################
# Game Constants
####################
DESCRIPTION = 'description'
INFO = 'info'
CHALLENGE = 'challenge'
HINT = 'hint'
SOLUTION = 'solution'
SOLVED = 'solved'
DIRECTIONS = ['up', 'down', 'left', 'right', 'forward', 'back']

map_solved = {
    'top': False,
    'north': False,
    'center': False,
    'east': False,
    'west': False,
    'south': False,
}

career_map = {
    'top': {
        DESCRIPTION: "You find yourself in a bustling career fair filled with recruiters.",
        INFO: "A recruiter challenges you to summarize your career goals in 30 seconds.",
        CHALLENGE: "Write your 'elevator pitch' in 10 words or less.",
        HINT: "Think about what you want to achieve in your career.",
        SOLUTION: lambda answer: len(answer.split()) <= 10,
        SOLVED: False,
    },
    'north': {
        DESCRIPTION: "You enter a quiet library filled with students preparing for interviews.",
        INFO: "A friend hands you a mock coding challenge.",
        CHALLENGE: "Solve this: What is 2^3 * 3?",
        HINT: "Remember the order of operations: exponents before multiplication.",
        SOLUTION: lambda answer: answer == "24",
        SOLVED: False,
    },
    'center': {
        DESCRIPTION: "You stand at the center, surrounded by different paths to success.",
        INFO: "Each wall leads to a unique opportunity, but before you can explore, you need a CV to showcase your skills.",
        CHALLENGE: "To proceed, create a CV. Enter the three most important sections in a CV.",
        HINT: "Common CV sections include education, experience, and skills.",
        SOLUTION: lambda answer: all(section in answer.lower() for section in ['education', 'experience', 'skills']),
        SOLVED: False,
    },
    'east': {
        DESCRIPTION: "You find yourself at a company networking event.",
        INFO: "A senior manager asks: 'What makes you unique?'",
        CHALLENGE: "Describe a strength you bring to the workplace.",
        HINT: "Think about what makes you stand out professionally.",
        SOLUTION: lambda answer: len(answer.split()) > 3,
        SOLVED: False,
    },
    'west': {
        DESCRIPTION: "You're in a virtual assessment center for a prestigious firm.",
        INFO: "A time-based scenario tests your decision-making skills.",
        CHALLENGE: "Choose one: (1) Prioritize speed (2) Ensure accuracy (3) Balance both.",
        HINT: "There is no wrong answer; it's about your priorities.",
        SOLUTION: lambda answer: answer in ["1", "2", "3"],
        SOLVED: False,
    },
    'south': {
        DESCRIPTION: "You approach a peer support group for first-generation students.",
        INFO: "Someone shares a personal challenge they faced during their journey.",
        CHALLENGE: "Share a time you overcame an obstacle in life.",
        HINT: "Focus on a specific moment that highlights your resilience.",
        SOLUTION: lambda answer: len(answer.split()) > 5,
        SOLVED: False,
    },
}

####################
# Game Functions
####################
def clear_screen():
    os.system('clear')

def print_location():
    """Print the player's current location description."""
    location = player.current_position
    print('\n' + ('#' * (4 + len(location))))
    print(f'# {location.upper()} #')
    print('#' * (4 + len(location)))
    print(career_map[location][DESCRIPTION])

def prompt():
    """Prompt the player for action."""
    print("\nWhat would you like to do?")
    print("1. Move to a different location")
    print("2. Inspect the current location")
    print("3. Check your stats")
    print("4. Quit the game")
    choice = input("> ").strip()

    if choice == "1":
        move_player()
    elif choice == "2":
        examine()
    elif choice == "3":
        check_stats()
    elif choice == "4":
        print("Thanks for playing! Goodbye!")
        sys.exit()
    else:
        print("Invalid choice. Please try again.")

def move_player():
    """Move the player to a new location."""
    print("Where would you like to move? (forward/back/left/right/up/down)")
    direction = input("> ").lower()
    if direction not in DIRECTIONS:
        print("Invalid direction. Please choose forward, back, left, right, up, or down.")
        return
    player.current_position = random.choice(list(career_map.keys()))  # Simulate movement
    print(f"You move {direction} and arrive at a new location.")
    print_location()

def examine():
    """Inspect the current location and attempt challenges."""
    location = player.current_position
    if career_map[location][SOLVED]:
        print("You've already solved the challenge here.")
        return

    print(career_map[location][INFO])
    print("Do you want a hint? (yes/no)")
    if input("> ").strip().lower() == "yes":
        print(f"HINT: {career_map[location][HINT]}")

    print(career_map[location][CHALLENGE])
    answer = input("> ").strip()
    if career_map[location][SOLUTION](answer):
        print("Correct! You've completed the challenge.")
        career_map[location][SOLVED] = True
        player.completed_challenges += 1
        level_up()
        check_goal()
    else:
        print("Incorrect. Try again later.")

def level_up():
    """Increase the player's level after completing enough challenges."""
    if player.completed_challenges % 3 == 0:  # Level up every 3 challenges
        player.level += 1
        print(f"\n🎉 Congratulations! You've advanced to Level {player.level}!")
        player.energy += 20  # Restore some energy
        player.reputation += 10

def check_goal():
    """Check if the player has achieved the game goal."""
    if player.level >= 3:  # Winning condition
        print("\n🎉 Congratulations! You've unlocked your dream job and completed the game! 🎉")
        sys.exit()

def check_stats():
    """Display the player's stats."""
    print("\nPlayer Stats:")
    print(f"Name: {player.name}")
    print(f"Energy: {player.energy}")
    print(f"Reputation: {player.reputation}")
    print(f"Completed Challenges: {player.completed_challenges}")
    print(f"Level: {player.level}")
    print(f"Skills: {player.skills}")

def start_game():
    """Initialize the game."""
    clear_screen()
    print("🎮 Welcome to CareerQuest: Unlocking Opportunities! 🎮")
    player.name = input("Enter your name: ").strip()
    print(f"Hello, {player.name}! Your journey begins.")
    print_location()
    while True:
        prompt()

####################
# Game Start
####################
if __name__ == "__main__":
    start_game()
