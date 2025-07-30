import random

def get_user_info():
    questions = [
        ("name", "What is your name? "),
        ("age", "How old are you? "),
        ("color", "What is your favorite color? "),
        ("food", "What is your favorite food? "),
        ("city", "Which city do you live in? "),
        ("shs", "Which SHS did you attend? "),
        ("team", "What is your favorite soccer team? ")
    ]

    random.shuffle(questions)
    answers = {}

    for key, question in questions:
        answers[key] = input(question)

    return answers

def display_summary(info):
    print("\n--- Summary ---")
    print(f"Hello, {info['name']}!")
    print(f"You are {info['age']} years old, love the color {info['color']}, and enjoy eating {info['food']}.")
    print(f"Life must be awesome in {info['city']}!")
    print("----------------\n")

def save_summary(info, rating):
    filename = f"{info['name']}.txt"
    try:
        with open(filename, 'w') as file:
            file.write("Personal Assistant Summary\n")
            file.write("==========================\n")
            for key, value in info.items():
                file.write(f"{key.capitalize()}: {value}\n")
            file.write(f"Rating: {rating}/5 stars\n")
        print(f"Summary saved successfully to {filename}\n")
    except Exception as e:
        print(f"Failed to save file: {e}")

def main():
    print("Welcome to your Simple Personal Assistant!\n")

    while True:
        user_info = get_user_info()
        display_summary(user_info)

        save = input("Would you like to save this summary to a file? (yes/no): ").strip().lower()
        rating = input("How would you rate this assistant (1-5 stars)? ").strip()

        if save == 'yes':
            save_summary(user_info, rating)

        restart = input("Would you like to restart and enter new details? (yes/no): ").strip().lower()
        if restart != 'yes':
            print("Thank you for using the Simple Personal Assistant. Goodbye!")
            break

if __name__ == "__main__":
    main()