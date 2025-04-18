# a) The extended_euclidean function
def extended_euclidean(a, m):
    old_r, r = a, m
    old_s, s = 1, 0
    old_t, t = 0, 1

    while r != 0:
        quotient = old_r // r
        old_r, r = r, old_r - quotient * r
        old_s, s = s, old_s - quotient * s
        old_t, t = t, old_t - quotient * t

    # print(old_r, old_s, old_t)

    inverse = (old_s % m + m) % m

    print(f"The inverse of {a} mod {m} is {inverse}")

    return old_r, old_s, old_t, inverse


# Test case
# extended_euclidean(517, 1021)


# b) The congruence_solve function
# i)
def congruence_solve(a, b, m):
    r, s, t, inverse = extended_euclidean(a, m)

    # ii)
    if b % r != 0:
        return "No solution can be found for the given parameters."

    # x = (s * (b // r)) % m
    x = (inverse * b) % m

    # x = x if x >= 0 else x + m

    # iii)
    return f"Given the linear congruence: 517x ≡ 17mod1021, the solution is x ≡ {x} (mod {m})"


# Test case
# print(congruence_solve(517, 17, 1021))


# c) The function to find the inverse of a mod m
def get_input():
    while True:
        try:
            a = int(input("Enter coefficient a: "))
            b = int(input("Enter constant b: "))
            m = int(input("Enter modulus m: "))
            print(f"Solving equation: {a}x ≡ {b} (mod {m})")
            confirm = input("Is this correct? (yes/no): ").strip().lower()
            if confirm == "yes":
                return a, b, m
        except ValueError:
            print("Please enter valid integers.")


def main():
    a, b, m = get_input()
    result = congruence_solve(a, b, m)
    print("Result:", result)


if __name__ == "__main__":
    main()
