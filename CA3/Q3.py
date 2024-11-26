#https://chatgpt.com/g/g-YBobxC10a-competitive-programming-expert/c/6745b2e4-ce10-800f-b1ff-1fcabb9fe56c
#now ,your algorithm is better, but have a problem. وقتی که تو میخوای swap انجام بدی، کاری که باید بکنی اینه که  بری در دو بازه حلقه بزنی، حلقه اول خونه های داخل بازه k که شامل خود خونه ای که اون لحظه بودیم نمیشه نیست، هست و بازه دوم خونه های بعد از بازه k هست که تا n که ببینیم با کدوم خونه از بازه k میتونیم اون رو جابجا کنیم که شرط زیبایی جواب بده.
#now change that section of code

def is_beautiful(arr, k):
    n = len(arr)
    for i in range(n - 1):
        found = False
        for j in range(i + 1, min(i + k + 1, n)):
            if arr[j] < arr[i]:
                found = True
                break
        if not found:
            return False
    return True


def can_be_beautiful_with_swaps(n, k, heights):
    if is_beautiful(heights, k):
        return "YES"

    for i in range(n-1):
        for j in range(i + 1, n):
            heights[i], heights[j] = heights[j], heights[i]  # Swap elements
            if is_beautiful(heights, k):
                return "YES"
            heights[i], heights[j] = heights[j], heights[i]  # Undo the swap

    return "NO"


# Reading input
n, k = map(int, input().split())
heights = list(map(int, input().split()))

# Solve and output the result
print(can_be_beautiful_with_swaps(n, k, heights))
