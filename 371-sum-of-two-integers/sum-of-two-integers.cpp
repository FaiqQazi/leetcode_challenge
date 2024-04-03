class Solution {
public:
    #include <iostream>

int getSum(int a, int b) {
    // Mask to limit to 32 bits
    unsigned int mask = 0xFFFFFFFF;
    
    // Perform addition without considering carry
    while (b != 0) {
        // Calculate sum without considering carry
        // Use bitwise XOR (^) to add bits without considering carry
        int sum_without_carry = (a ^ b) & mask;
        
        // Calculate carry using bitwise AND (&) followed by left shift (<<) operation
        int carry = ((a & b) << 1) & mask;
        
        // Update a and b for next iteration
        a = sum_without_carry;
        b = carry;
    }
    
    // Handle overflow
    if (a > 0x7FFFFFFF) {
        a = ~(a ^ mask);
    }
    
    return a;
}

int main() {
    int a = 1, b = 2;
    std::cout << getSum(a, b) << std::endl;  // Output: 3
    
    a = 2, b = 3;
    std::cout << getSum(a, b) << std::endl;  // Output: 5
    
    return 0;
}

};