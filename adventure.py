"""A small command-line choose-your-own-adventure game."""


def choose(prompt, options):
    """Display numbered options and return the selected option number."""
    while True:
        print(prompt)
        for number, option in enumerate(options, start=1):
            print(f"  {number}. {option}")

        choice = input("> ").strip()
        if choice.isdigit() and 1 <= int(choice) <= len(options):
            return int(choice)

        print("Please choose one of the numbered options.\n")


def main():
    print("THE LANTERN OF STARFALL")
    print("You wake at the edge of a moonlit forest with a mysterious lantern in hand.")
    print("Your goal is to reach the old tower before the lantern burns out.\n")

    choice = choose(
        "You stand before two paths. Where do you go?",
        ["Follow the mossy trail into the forest", "Cross the old stone bridge"],
    )

    if choice == 1:
        choice = choose(
            "The forest trail leads to a quiet clearing. A fox watches you from a fallen tree.",
            [
                "Offer the fox a piece of your bread",
                "Chase the fox away and search the tree",
                "Ignore the clearing and walk into the dark woods",
            ],
        )
        if choice == 1:
            print("\nThe fox bows and reveals a hidden path to the tower.\n")
        elif choice == 2:
            print("\nThe tree collapses beneath you. The forest keeps its secrets. You lose!")
            return
        else:
            print("\nThe lantern flickers out in the dark woods. You lose!")
            return
    else:
        choice = choose(
            "The bridge groans under your feet. Halfway across, you spot a locked iron gate.",
            [
                "Use the lantern's flame to warm the lock",
                "Turn back and search beneath the bridge",
                "Run across the bridge before it gives way",
            ],
        )
        if choice == 1:
            print("\nThe lock glows gold and clicks open. Beyond it, a path climbs toward the tower.\n")
        elif choice == 2:
            print("\nA sudden current sweeps you into the river. You lose!")
            return
        else:
            print("\nThe bridge collapses just as you reach the far side. You lose!")
            return

    choice = choose(
        "At the tower door, three symbols are carved into the stone.",
        ["Press the sun symbol", "Press the moon symbol", "Press the star symbol"],
    )

    if choice == 3:
        print("\nThe star symbol shines brightly. The tower opens, and the lantern becomes a crown of light.")
        print("You found the Lantern of Starfall. You win!")
    else:
        print("\nThe symbol flashes red, and the tower sends you back into the night. You lose!")


if __name__ == "__main__":
    main()
