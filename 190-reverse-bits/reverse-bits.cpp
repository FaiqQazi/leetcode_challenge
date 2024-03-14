#include <cstdint>
#include <string>
#include <algorithm> // For reverse

class Solution {
public:
    uint32_t reverseBits(uint32_t n) {
        // Convert the integer to a binary string representation
        std::string binaryStr = std::bitset<32>(n).to_string();

        // Reverse the binary string
        std::reverse(binaryStr.begin(), binaryStr.end());

        // Convert the reversed binary string back to an integer
        uint32_t result = std::bitset<32>(binaryStr).to_ulong();

        return result;
    }
};
