from itertools import permutations


def can_form_string(a, b, c, d, s):
    # Check if the length of s matches the total length of all words
    if len(s) != a + b + 2 * c + 2 * d:
        return "NO"

    # Create the list of words
    words = ['H'] * a + ['P'] * b + ['HP'] * c + ['PH'] * d

    # Try all permutations of the words
    for perm in permutations(words):
        # Join the words in this permutation
        candidate = ''.join(perm)

        # If the joined string matches the target string, return "YES"
        if candidate == s:
            return "YES"

    # If no permutation matches, return "NO"
    return "NO"


def main():
    # Read the number of test cases
    t = int(input())

    for _ in range(t):
        # Read input for each test case
        a, b, c, d = map(int, input().split())
        s = input().strip()

        # Call the function and print the result
        result = can_form_string(a, b, c, d, s)
        print(result)


if __name__ == "__main__":
    main()