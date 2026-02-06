
class Solution:
    def calc_hash(self, s:str)->Dict[str,int]:
        hash_map={}
        for char in s:
            hash_map[char]=hash_map.get(char,0)+1
        return hash_map


    def checkInclusion(self, s1: str, s2: str) -> bool:

        s1_hash={}
        s1_hash=self.calc_hash(s1)
        print(f"s1 is {s1_hash}")
        i=0
        j=i+len(s1)
        for i in range(len(s2)):
            sub_arr_hash={}
            sub_arr=s2[i:j]
            # print(f"the sub arr is {sub_arr}")
            sub_arr_hash=self.calc_hash(sub_arr)
            # print(f"the sub arr hash is {sub_arr_hash}")
            if s1_hash==sub_arr_hash:
                # print("we found a match")
                return True
            i=i+1
            j=j+1
        return False



        