#include <string>
#include <iostream>
#include <vector>

std::vector<int> make_z_function(std::string s, int beg) {
    std::vector<int> z(s.size());
	z[beg] = s.size() - beg;
	int l = beg;
	int r = beg;
	for (int i = beg + 1; i < s.size(); ++i) {
		z[i] = 0;
		if (i <= r)
			z[i] = std::min(r - i + 1, z[i - l + beg]);
		while (i + z[i] < s.size() && s[z[i] + beg] == s[z[i] + i])
			++z[i];
		if (i + z[i] - 1 > r) {
			r = i + z[i] - 1;
			l = i;
		}
	}
    return z;
}

int main() {
    std::string str;
    std::cin >> str;
    int best_len = 0;
	int best_i = 0;
	int best_cout = 0;
	for (int i = 0; i < str.size(); ++i) {
		
    	std::vector<int> z = make_z_function(str.substr(i, str.size()) + "$" + str, 0);
		for (int j = 1; j < str.size() - i; ++j) {
			int cur_len = 0;
			int cur_count = 0;
			for (int k = str.size() - i + 1; k < z.size(); ++k) {
				if (z[k] >= j) {
					cur_count += 1;
				}
			}
			if (j * cur_count > best_len * best_cout) {
				best_len = j;
				best_cout = cur_count;
				best_i = i;
			}
		}
	}
	if (best_cout * best_len < str.size()) {
		best_cout = 1;
		best_len = str.size();
		best_i = 0;
	}
	std::cout << best_cout << ' ' << best_len << std::endl;
	std::cout << str.substr(best_i, best_len) << std::endl;

    return 0;
}