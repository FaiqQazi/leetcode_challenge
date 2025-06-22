import math

class Solution:
    def splitIntoFibonacci(self, num: str):
        n = len(num)
        max_len = min(10, n // 2)  # Updated limit: max 10 digits (fits in 32-bit signed int)
        print(f"Input num = {num}, Length = {n}, Max length guess = {max_len}\n")

        for length1 in range(1, max_len + 1):  # Allow small to large lengths
            for length2 in range(1, max_len + 1):  # ✅ Fix: allow second number to be longer
                print(f"Trying first length = {length1}, second length = {length2}")

                if length1 + length2 >= n:
                    print("  Skipping because not enough digits left for third number\n")
                    continue

                first = num[:length1]
                second = num[length1:length1 + length2]

                print(f"  Trying first = '{first}', second = '{second}'")

                # Skip invalid numbers with leading zeros
                if (first.startswith("0") and len(first) > 1) or (second.startswith("0") and len(second) > 1):
                    print("  Skipping due to leading zero\n")
                    continue

                a, b = int(first), int(second)

                if a >= 2**31 or b >= 2**31:
                    print("  Skipping because a or b exceeds 32-bit integer range\n")
                    continue

                fib = [a, b]
                idx = length1 + length2
                print(f"  Starting Fibonacci check with: {fib}, next index = {idx}")

                while idx < n:
                    c = fib[-1] + fib[-2]
                    if c >= 2**31:
                        print("    Next number too large, break\n")
                        break
                    cs = str(c)
                    print(f"    Expecting next number = {c} (as '{cs}') at position {idx}")

                    if not num.startswith(cs, idx):
                        print("    Mismatch, breaking this attempt\n")
                        break
                    fib.append(c)
                    idx += len(cs)
                    print(f"    Match! Sequence so far: {fib}, next index = {idx}")

                if idx == n and len(fib) >= 3:
                    print(f"✔️ Valid Fibonacci sequence found: {fib}\n")
                    return fib
                else:
                    print("❌ Did not use entire string or too short sequence, trying next\n")

        print("No valid Fibonacci sequence found.")
        return []
