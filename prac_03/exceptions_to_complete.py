is_finished = False
while not is_finished:
    try:
        result = int(input("Enter a valid integer: "))
        is_finished = True  # Exit loop after getting a valid integer
    except ValueError:  # Handle the exception for invalid integer input
        print("Please enter a valid integer.")
print("Valid result is:", result)