////#https://chatgpt.com/g/g-YBobxC10a-competitive-programming-expert/c/6745b2e4-ce10-800f-b1ff-1fcabb9fe56c
//#now ,your algorithm is better, but have a problem. وقتی که تو میخوای swap انجام بدی، کاری که باید بکنی اینه که  بری در دو بازه حلقه بزنی، حلقه اول خونه های داخل بازه k که شامل خود خونه ای که اون لحظه بودیم نمیشه نیست، هست و بازه دوم خونه های بعد از بازه k هست که تا n که ببینیم با کدوم خونه از بازه k میتونیم اون رو جابجا کنیم که شرط زیبایی جواب بده.
//#now change that section of code



#include <iostream>
#include <vector>

using namespace std;

bool is_beautiful(const vector<int>& arr, int k) {
    int n = arr.size();
    for (int i = 0; i < n - 1; ++i) {
        bool found = false;
        for (int j = i + 1; j < min(i + k + 1, n); ++j) {
            if (arr[j] < arr[i]) {
                found = true;
                break;
            }
        }
        if (!found) {
            return false;
        }
    }
    return true;
}

string can_be_beautiful_with_swaps(int n, int k, vector<int>& heights) {
    if (is_beautiful(heights, k)) {
        return "YES";
    }

    for (int i = 0; i < n - 1; ++i) {
        // Check elements in the range of k excluding current index
        for (int j = max(0, i - k); j < i; ++j) {
            // Swap elements
            swap(heights[i], heights[j]);
            if (is_beautiful(heights, k)) {
                return "YES";
            }
            // Undo the swap
            swap(heights[i], heights[j]);
        }

        // Check elements after the current index
        for (int j = i + 1; j < min(i + k + 1, n); ++j) {
            swap(heights[i], heights[j]);
            if (is_beautiful(heights, k)) {
                return "YES";
            }
            swap(heights[i], heights[j]);
        }
    }

    return "NO";
}

int main() {
    // Reading input
    int n, k;
    cin >> n >> k;
    vector<int> heights(n);
    for (int i = 0; i < n; ++i) {
        cin >> heights[i];
    }

    // Solve and output the result
    cout << can_be_beautiful_with_swaps(n, k, heights) << endl;

    return 0;
}