import random
from score import determine_score_status


def get_valid_score():
    while True:
        score = input("Enter a score (0-100 inclusive): ")
        if score.isdigit():
            score = int(score)
            if 0 <= score <= 100:
                return score
        print("Invalid score. Please enter a number between 0 and 100.")


def print_result(score):
    result = determine_score_status(score)
    print("Result:", result)


def show_stars(score):
    print("*" * score)


def main():
    score = get_valid_score()
    print("Initial score:", score)

    while True:
        print("\nMain Menu:")
        print("(G)et a valid score")
        print("(P)rint result")
        print("(S)how stars")
        print("(Q)uit")

        choice = input("Enter your choice: ").upper()

        if choice == 'G':
            score = get_valid_score()
            print("New score:", score)
        elif choice == 'P':
            print_result(score)
        elif choice == 'S':
            show_stars(score)
        elif choice == 'Q':
            print("Farewell!")
            break
        else:
            print("Invalid choice. Please choose from the menu options.")


if __name__ == "__main__":
    main()
