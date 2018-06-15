#include <cmath>
#include <iostream>
using namespace std;

class Solution {
public:
    /**
     * @param number: A 3-digit number.
     * @return: Reversed number.
     */
    int reverseInteger(int number) {
        // write your code here
        
        int res = 0, i, tmp;

        for (i = 2; i >= 0; i--){
            tmp = int(std::pow(10, i));
            res += (number / tmp) * int(pow(10, 2 - i));
            number = number % tmp; 
        }

        return res;
    }
};

int main() {

    int number = 999, res;
    
    Solution sol;
    res = sol.reverseInteger(number);
    cout << "res: " << res << "\n";
    return 0;
}
