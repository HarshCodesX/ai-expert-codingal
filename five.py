import time
from textblob import TextBlob
from colorama import init, Fore

# Initialize colorama
init(autoreset=True)

# In-memory movie dataset
MOVIES = [
    {
        "title": "Inception",
        "genres": ["Action", "Sci-Fi"],
        "overview": "A thief who steals corporate secrets through dream-sharing technology.",
        "rating": 8.8
    },
    {
        "title": "The Dark Knight",
        "genres": ["Action", "Drama"],
        "overview": "Batman faces the Joker, a criminal mastermind who wants chaos.",
        "rating": 9.0
    },
    {
        "title": "Forrest Gump",
        "genres": ["Drama", "Romance"],
        "overview": "The story of a man with a low IQ who lived an extraordinary life.",
        "rating": 8.8
    },
    {
        "title": "The Hangover",
        "genres": ["Comedy"],
        "overview": "Three friends wake up from a bachelor party with no memory of the night before.",
        "rating": 7.7
    },
    {
        "title": "Interstellar",
        "genres": ["Adventure", "Sci-Fi"],
        "overview": "A team travels through a wormhole in space to ensure humanity's survival.",
        "rating": 8.6
    }
]

# Get all unique genres
def get_genres():
    genres = set()
    for movie in MOVIES:
        genres.update(movie["genres"])
    return sorted(genres)

GENRES = get_genres()

# Small loading animation
def loading(msg="Processing"):
    print(Fore.YELLOW + msg, end="", flush=True)
    for _ in range(3):
        time.sleep(0.5)
        print(".", end="", flush=True)
    print()

# Recommend movies
def recommend_movies(genre, mood, min_rating=None, limit=5):
    mood_polarity = TextBlob(mood).sentiment.polarity
    recommendations = []

    for movie in MOVIES:
        if genre not in movie["genres"]:
            continue

        if min_rating and movie["rating"] < min_rating:
            continue

        overview_polarity = TextBlob(movie["overview"]).sentiment.polarity

        if mood_polarity > 0 and overview_polarity <= 0:
            continue
        if mood_polarity < 0 and overview_polarity >= 0:
            continue

        recommendations.append(
            (movie["title"], overview_polarity, movie["rating"])
        )

        if len(recommendations) == limit:
            break

    return recommendations

# Display results
def display_results(recs, name):
    print(Fore.CYAN + f"\nMovie recommendations for {name}:\n")
    for idx, (title, polarity, rating) in enumerate(recs, 1):
        sentiment = "Positive" if polarity > 0 else "Negative" if polarity < 0 else "Neutral"
        print(
            Fore.GREEN
            + f"{idx}. {title} | Rating: {rating} | Sentiment: {sentiment} ({polarity:.2f})"
        )

# Main flow
def start_assistant():
    print(Fore.BLUE + "Welcome to the AI Movie Recommendation Assistant\n")
    name = input(Fore.YELLOW + "What's your name? ").strip() or "User"
    print(Fore.GREEN + f"Hello {name}! Let's find a movie for you.\n")

    print(Fore.CYAN + "Available genres:")
    for idx, genre in enumerate(GENRES, 1):
        print(Fore.CYAN + f"{idx}. {genre}")

    while True:
        choice = input(Fore.YELLOW + "\nChoose a genre (number or name): ").strip()
        if choice.isdigit() and 1 <= int(choice) <= len(GENRES):
            genre = GENRES[int(choice) - 1]
            break
        elif choice.title() in GENRES:
            genre = choice.title()
            break
        else:
            print(Fore.RED + "Invalid genre. Try again.")

    mood = input(Fore.YELLOW + "\nHow are you feeling today? ").strip()
    loading("Analyzing your mood")

    mood_polarity = TextBlob(mood).sentiment.polarity
    mood_desc = "positive" if mood_polarity > 0 else "negative" if mood_polarity < 0 else "neutral"
    print(Fore.GREEN + f"Your mood seems {mood_desc} ({mood_polarity:.2f})\n")

    while True:
        rating_input = input(
            Fore.YELLOW + "Minimum IMDB rating (or type 'skip'): "
        ).strip().lower()

        if rating_input == "skip":
            min_rating = None
            break

        try:
            min_rating = float(rating_input)
            break
        except ValueError:
            print(Fore.RED + "Please enter a valid number or 'skip'.")

    loading("Finding movies")

    recs = recommend_movies(genre, mood, min_rating)

    if not recs:
        print(Fore.RED + "No suitable recommendations found.")
        return

    display_results(recs, name)

    print(Fore.GREEN + "\nEnjoy your movie time!")

# Entry point
if __name__ == "__main__":
    start_assistant()
