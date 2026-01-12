import colorama
from colorama import Fore, Style
from textblob import TextBlob

# Initialize colorama
colorama.init()

print(f"{Fore.CYAN}Welcome to Sentiment Spy{Style.RESET_ALL}")

# Ask for user's name
user_name = input(f"{Fore.MAGENTA}Please enter your name: {Style.RESET_ALL}").strip()
if not user_name:
    user_name = "User"

# Store conversation history
conversation_history = []

print(f"\n{Fore.CYAN}Hello, {user_name}!{Style.RESET_ALL}")
print(
    f"Type a sentence and I will analyze its sentiment.\n"
    f"Commands: {Fore.YELLOW}reset{Fore.CYAN}, "
    f"{Fore.YELLOW}history{Fore.CYAN}, "
    f"{Fore.YELLOW}exit{Fore.CYAN}\n"
    f"{Style.RESET_ALL}"
)

while True:
    user_input = input(f"{Fore.GREEN}> {Style.RESET_ALL}").strip()

    if not user_input:
        print(f"{Fore.RED}Please enter some text or a valid command.{Style.RESET_ALL}")
        continue

    # Exit command
    if user_input.lower() == "exit":
        print(f"{Fore.BLUE}Exiting Sentiment Spy. Goodbye, {user_name}!{Style.RESET_ALL}")
        break

    # Reset history
    elif user_input.lower() == "reset":
        conversation_history.clear()
        print(f"{Fore.CYAN}Conversation history cleared.{Style.RESET_ALL}")
        continue

    # Show history
    elif user_input.lower() == "history":
        if not conversation_history:
            print(f"{Fore.YELLOW}No conversation history yet.{Style.RESET_ALL}")
        else:
            print(f"{Fore.CYAN}Conversation History:{Style.RESET_ALL}")
            for idx, (text, polarity, sentiment_type) in enumerate(conversation_history, start=1):
                if sentiment_type == "Positive":
                    color = Fore.GREEN
                elif sentiment_type == "Negative":
                    color = Fore.RED
                else:
                    color = Fore.YELLOW

                print(
                    f"{idx}. {color}{text} "
                    f"(Polarity: {polarity:.2f}, {sentiment_type}){Style.RESET_ALL}"
                )
        continue

    # Sentiment analysis
    polarity = TextBlob(user_input).sentiment.polarity

    if polarity > 0.25:
        sentiment_type = "Positive"
        color = Fore.GREEN
    elif polarity < -0.25:
        sentiment_type = "Negative"
        color = Fore.RED
    else:
        sentiment_type = "Neutral"
        color = Fore.YELLOW

    # Store result
    conversation_history.append((user_input, polarity, sentiment_type))

    print(
        f"{color}{sentiment_type} sentiment detected "
        f"(Polarity: {polarity:.2f}){Style.RESET_ALL}"
    )
