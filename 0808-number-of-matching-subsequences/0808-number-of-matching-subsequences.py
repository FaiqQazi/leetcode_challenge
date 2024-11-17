# class Solution:
#     def numMatchingSubseq(self, s: str, words: List[str]) -> int:
#         def is_substring(a: str, hashmap1: dict) -> bool:
#             hashmap2 = {}
#             for i in a:
#                 hashmap2[i] =0
#             for i in a:
#                 hashmap2[i] +=1
#             for i in a:
#                 if (hashmap1.get(i, 0) == hashmap2[i]) or (i in hashmap1 and i in hashmap2):
#                     continue
#                 else:
#                     return False
#             return True

#         hashmap1 = {}
#         count = 0
#         for i in s:
#             hashmap1[i] =0
#         for i in s:
#             hashmap1[i] +=1
#         for i in words:
#             if is_substring(i, hashmap1):
#                 count += 1
#             else:
#                 print(f"{i} was not a subsequence of {s}, continue")
#         return count


# tried using a simple hash but that did not work

# class Solution:
#     def numMatchingSubseq(self, s: str, words: list[str]) -> int:
#         # Step 1: Build a dictionary of indices for each character in `s`
#         char_indices = defaultdict(list)
#         for index, char in enumerate(s):
#             char_indices[char].append(index)
#         print("{char_indices}")
#         for word in words:
#             for c in word :

# class Solution:
#     def numMatchingSubseq(self, s: str, words: List[str]) -> int:
#         # Step 1: Build a dictionary of indices for each character in `s`
#         char_indices = defaultdict(list)
#         for index, char in enumerate(s):
#             char_indices[char].append(index)

#         # Step 2: Check each word
#         count = 0
#         for word in words:
#             prev_index = -1
#             for c in word:
#                 # Find the smallest index greater than prev_index for character c
#                 indices = char_indices[c]
#                 found = False
#                 for i in indices:
#                     if i > prev_index:
#                         prev_index = i
#                         found = True
#                         break
#                 if not found:
#                     break
#             else:
#                 count += 1

#         return count

class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        # Step 1: Build a dictionary of indices for each character in `s`
        char_indices = defaultdict(list)
        for index, char in enumerate(s):
            char_indices[char].append(index)

        # Step 2: Check each word
        count = 0
        for word in words:
            prev_index = -1
            for c in word:
                # Find the smallest index greater than prev_index for character c
                indices = char_indices[c]
                pos = bisect_left(indices, prev_index + 1)
                if pos < len(indices):
                    prev_index = indices[pos]
                else:
                    break
            else:
                count += 1

        return count