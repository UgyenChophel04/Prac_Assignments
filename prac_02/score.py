import random


def determine_score_status(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


def main():
    user_score = float(input("Enter your score: "))
    user_result = determine_score_status(user_score)
    print("Your result is:", user_result)

    # Generate a random score
    random_score = random.randint(0, 100)
    random_result = determine_score_status(random_score)
    print("Random score:", random_score)
    print("Random result:", random_result)


if __name__ == "__main__":
    main()
