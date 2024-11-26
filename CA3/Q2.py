def count_occurrences(s):
    count_h = s.count('H')
    count_p = s.count('P')
    count_hp = s.count('HP')
    count_ph = s.count('PH')
    return count_h, count_p, count_hp, count_ph

def can_form_string(a, b, c, d, s):
    count_h, count_p, count_hp, count_ph = count_occurrences(s)
    used_hp = min(count_hp, c)
    used_ph = min(count_ph, d)
    remaining_h = count_h - used_hp - used_ph
    remaining_p = count_p - used_hp - used_ph
    if remaining_h == a and remaining_p == b:
        return "YES"
    return "NO"

def solve_magic_book(t, test_cases):
    results = []
    for case in test_cases:
        a, b, c, d, s = case
        result = can_form_string(a, b, c, d, s)
        results.append(result)
    return results

def main():
    t = int(input())
    test_cases = []
    for _ in range(t):
        a, b, c, d = map(int, input().split())
        s = input().strip()
        test_cases.append((a, b, c, d, s))
    results = solve_magic_book(t, test_cases)
    print("\n".join(results))

if __name__ == "__main__":
    main()
