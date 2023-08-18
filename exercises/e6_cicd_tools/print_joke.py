import random

import pyjokes

reactions = [
    "Hilarious!",
    "Oh, the humanity!",
    "You've cracked the code!",
    "That's comedy gold!",
    "My sides are splitting!",
    "Mind = blown!",
    "Cue the laugh track!",
    "I'm dying of laughter!",
    "That's so bad, it's good!",
    "*Insert uncontrollable laughter here*",
]


def get_random_reaction():
    return reactions[random.randint(0, len(reactions) - 1)]
    pass  # Fill this one in


def print_random_joke_and_reaction():
    joke = pyjokes.get_joke()
    reaction = get_random_reaction(reactions)
    print(f"{joke}\n{reaction}")
    pass  # Fill this one in


if __name__ == "__main__":
    print_random_joke_and_reaction()
