def write_name_to_file():
    name = input("Enter your name: ")
    file = open('name.txt', 'w')
    file.write(name)
    file.close()


def read_name_and_greet():
    file = open('name.txt', 'r')
    name = file.read().strip()
    print(f"Hi {name}!")
    file.close()


def sum_first_two_numbers():
    with open('numbers.txt', 'r') as file:
        number1 = int(file.readline())
        number2 = int(file.readline())
    print(number1 + number2)


def sum_all_numbers():
    total = 0
    with open('numbers.txt', 'r') as file:
        for line in file:
            total += int(line)
    print(total)


if __name__ == "__main__":
    write_name_to_file()
    read_name_and_greet()
    sum_first_two_numbers()
    sum_all_numbers()