#include <iostream>
#include <vector>
#include <chrono>

int main() {
    int n = 10000000;
    std::vector<int> numbers;
    std::vector<int> squares;

    for (int i = 1; i <= n; ++i) {
        numbers.push_back(i);
    }

    auto start = std::chrono::high_resolution_clock::now();

    for (int i = 0; i < n; ++i) {
        squares.push_back(numbers[i] * numbers[i]);
    }

    auto end = std::chrono::high_resolution_clock::now();
    std::chrono::duration<double> elapsed = end - start;

    std::cout << "Time taken: " << elapsed.count() << " seconds" << std::endl;

    return 0;
}
