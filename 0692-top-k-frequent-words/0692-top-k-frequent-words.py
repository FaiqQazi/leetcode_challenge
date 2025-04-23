class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        arrhash={}
        print(words)
        for i in words:
            if i in arrhash:
                arrhash[i] += 1
            else:
                arrhash[i] = 1
        print(arrhash)
        #sort based on frequency
        sorted_items = sorted(arrhash.items(), key=lambda item: (-item[1],item[0]))
        print("sorted items 1 ")
        print(sorted_items)

        arr=[]
        result=[word for word , freq in sorted_items[:k]]
        return result







        