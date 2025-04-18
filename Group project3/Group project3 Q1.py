def two_el_gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def GCD(numbers):
    result = numbers[0]
    for num in numbers[1:]:
        result = two_el_gcd(result, num)
    return result


def parse_input(user_input):
    if "," in user_input:
        parts = user_input.split(",")
    else:
        parts = user_input.split()
    return [int(p.strip()) for p in parts][::-1]


def main():
    user_input = input("Enter numbers (comma or space separated): ")
    try:
        numbers = parse_input(user_input)
        result = GCD(numbers)
        print("The GCD is:", result)
    except ValueError:
        print("Please enter valid integers only.")


if __name__ == "__main__":
    main()

    # Test cases
    numbers = [2, 4, 2042]
    result = GCD(numbers)
    print("Test cases a), The ", numbers, " of GCD is:", result)
    numbers = [330, 1505, 3289, 15301]
    result = GCD(numbers)
    print("Test cases b) ,The ", numbers, " of GCD is:", result)
