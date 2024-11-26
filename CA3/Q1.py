def can_form_teams(max_actors, k, actor_counts):
    teams = 0
    current_group = 0

    for count in actor_counts:
        current_group += count
        teams += current_group // max_actors
        current_group = min(current_group % max_actors, count)

        if teams >= k:
            return True

    return teams >= k


def find_max_actors(n, k, actor_counts):
    if n == 1:
        total_actors = actor_counts[0]
    else:
        total_actors = max(actor_counts[i] + actor_counts[i + 1] for i in range(n - 1))

    low, high = 1, total_actors
    best = 0

    while low <= high:
        mid = (low + high) // 2
        if can_form_teams(mid, k, actor_counts):
            best = mid
            low = mid + 1
        else:
            high = mid - 1

    return best * k


def max_actors_in_theater(t, test_cases):
    results = []

    for n, k, actor_counts in test_cases:
        result = find_max_actors(n, k, actor_counts)
        results.append(result)

    return results


def main():
    t = int(input())
    test_cases = []

    for _ in range(t):
        n, k = map(int, input().split())
        actor_counts = list(map(int, input().split()))
        test_cases.append((n, k, actor_counts))

    answers = max_actors_in_theater(t, test_cases)
    print("\n".join(map(str, answers)))


if __name__ == "__main__":
    main()