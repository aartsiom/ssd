#include <iostream>
#include <vector>

void process(std::vector<uint64_t> &numbers, size_t q) {
    for (size_t i = 0; i < q; ++i) {
        size_t req_id;
        std::cin >> req_id;
        // std::cout << req_id << std::endl;
        if (req_id == 1) {
            size_t index;
            uint64_t value;
            std::cin >> index >> value;
            numbers[index - 1] = value;
        } else { 
            size_t l, r;
            std::cin >> l >> r;
            if (req_id == 2) {
                for (size_t i = l - 1; i < r; ++i) {
                    numbers[i] += 1;
                } 
            }
            if (req_id == 3) {
                uint64_t sum = 0;
                for (size_t i = l - 1; i < r; ++i) {
                    if (numbers[i] % 2 == 0)
                        sum += numbers[i];
                } 
                std::cout << sum << std::endl;
            }
            if (req_id == 4) {
                uint64_t sum = 0;
                for (size_t i = l - 1; i < r; ++i) {
                    if (numbers[i] % 2)
                        sum += numbers[i];
                } 
                std::cout << sum << std::endl;
            }
        }
    }
}


int main() {
    size_t n, q;
    std::cin >> n >> q;
    std::vector<uint64_t> numbers(n);
    for (auto &el: numbers) {
        std::cin >> el;
    }
    // for (auto el: numbers) {
    //     std::cout << el << ' ';
    // }
    process(numbers, q);
    return 0;
}