# I didn't use dictionaries but the chr and ord.


def other_to_ten(num, base_from):
    res = 0
    power = 0
    for digit in reversed(str(num)):
        if digit.isdigit():
            value = int(digit)
        else:
            value = ord(digit.upper()) - ord("A") + 10
        res += value * (base_from**power)
        power += 1

    return res


def ten_to_other(num, base_to):
    num = int(num)
    if num == 0:
        return "0"

    res = ""
    while num != 0:
        remainder = num % base_to
        num = num // base_to
        if remainder < 10:
            digit = str(remainder)
        else:
            digit = chr(ord("A") + remainder - 10)
        res = digit + res

    return res


# Test case
# print(other_to_ten("B53", 16))
# print(ten_to_other("2899", 8))


def anybase_to_anybase(num_str, base_from, base_to):
    decimal = other_to_ten(num_str, base_from)
    converted = ten_to_other(decimal, base_to)
    print(f"{num_str} (base {base_from}) = {converted} (base {base_to})")
    return converted


def main():
    print("Base Converter (Supports base 2 to 16)")
    num_str = input("Enter the number to convert (e.g., B53): ").strip()
    base_from = int(input("Enter the base of that number (2-16): "))
    base_to = int(input("Enter the base to convert to (2-16): "))

    try:
        if not (2 <= base_from <= 16 and 2 <= base_to <= 16):
            raise ValueError("Base must be between 2 and 16.")

        anybase_to_anybase(num_str, base_from, base_to)

    except ValueError as e:
        print("Error:", e)


if __name__ == "__main__":
    main()
    print("\n")

    # Test cases
    print("Test case b i):")
    anybase_to_anybase("8723782367", 9, 15)
    num_str = "8723782367"
    print("\n")

    print("Test case b ii):")
    anybase_to_anybase("123456789ABCDEF", 16, 10)
    print("\n")

    print("Test case b iii):")
    anybase_to_anybase("11111110111011011011111011101111", 2, 16)
