import re
import random
from colorama import Fore, init

# Initialize colorama
init(autoreset=True)

# Travel data
TRAVEL_OPTIONS = {
    "beaches": ["Bali", "Maldives", "Phuket"],
    "mountains": ["Swiss Alps", "Rocky Mountains", "Himalayas"],
    "cities": ["Tokyo", "Paris", "New York"]
}

JOKES = [
    "Why don't programmers like nature? Too many bugs!",
    "Why did the computer go to the doctor? Because it caught a virus!",
    "Why do travelers always feel warm? Because of all their hot spots!"
]

# Normalize user input
def clean_input(text: str) -> str:
    return re.sub(r"\s+", " ", text.strip().lower())

# Recommend a travel destination
def suggest_destination():
    while True:
        print(Fore.CYAN + "TravelBot: What do you prefer? Beaches, mountains, or cities?")
        choice = clean_input(input(Fore.YELLOW + "You: "))

        if choice not in TRAVEL_OPTIONS:
            print(Fore.RED + "TravelBot: I don't recognize that option.")
            return

        place = random.choice(TRAVEL_OPTIONS[choice])
        print(Fore.GREEN + f"TravelBot: You could visit {place}.")
        feedback = clean_input(input(Fore.YELLOW + "TravelBot: Does that work for you? (yes/no): "))

        if feedback == "yes":
            print(Fore.GREEN + f"TravelBot: Great choice! Have a wonderful trip to {place}.")
            return
        elif feedback == "no":
            print(Fore.CYAN + "TravelBot: No problem, let's try again.")
        else:
            print(Fore.RED + "TravelBot: I'll take that as a no and suggest again.")

# Provide packing advice
def give_packing_tips():
    destination = clean_input(input(Fore.YELLOW + "TravelBot: Where are you heading? "))
    days = input(Fore.YELLOW + "TravelBot: Trip duration (in days)? ")

    print(Fore.GREEN + f"\nTravelBot: Packing advice for {days} days in {destination}:")
    print(Fore.GREEN + "- Choose clothes that can be mixed and matched.")
    print(Fore.GREEN + "- Carry essential chargers and adapters.")
    print(Fore.GREEN + "- Always check the weather before packing.\n")

# Tell a joke
def share_joke():
    print(Fore.YELLOW + f"TravelBot: {random.choice(JOKES)}")

# Help menu
def display_help():
    print(Fore.MAGENTA + "\nAvailable options:")
    print(Fore.GREEN + "- Ask for travel suggestions (say 'recommend')")
    print(Fore.GREEN + "- Get packing advice (say 'packing')")
    print(Fore.GREEN + "- Hear a joke (say 'joke')")
    print(Fore.CYAN + "Type 'exit' or 'bye' to leave the chat.\n")

# Main interaction loop
def start_chat():
    print(Fore.CYAN + "TravelBot: Hello! I'm here to help with your travel plans.")
    user_name = input(Fore.YELLOW + "Your name: ").strip() or "Traveler"
    print(Fore.GREEN + f"TravelBot: Nice to meet you, {user_name}.")

    display_help()

    while True:
        user_input = clean_input(input(Fore.YELLOW + f"{user_name}: "))

        if "recommend" in user_input or "suggest" in user_input:
            suggest_destination()
        elif "pack" in user_input:
            give_packing_tips()
        elif "joke" in user_input or "funny" in user_input:
            share_joke()
        elif "help" in user_input:
            display_help()
        elif "exit" in user_input or "bye" in user_input:
            print(Fore.CYAN + "TravelBot: Thanks for chatting. Safe travels!")
            break
        else:
            print(Fore.RED + "TravelBot: I'm not sure I understood that.")

if __name__ == "__main__":
    start_chat()
