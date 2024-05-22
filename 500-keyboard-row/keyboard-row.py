class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        final=[]
        str1 = "qQwWeErRtTyYuUiIoOpP"
        str2 = "aAsSdDfFgGhHjJkKlL"
        str3 = "zZxXcCvVbBnNmM"



       
        r1=list(str1)
        r2=list(str2)
        r3=list(str3)
        print(r1,r2,r3)
        for word in words:
            thebool=False
            for char in word:
                if(char not in r1):
                    thebool=True
                    break
            if thebool==False:
                final.append(word)
            thebool=False
            for char in word:
                if(char not in r2):
                    thebool=True
                    break
            if thebool==False:
                final.append(word)
            thebool=False
            for char in word:
                if(char not in r3):
                    thebool=True
                    break

            if thebool==False:
                final.append(word)
            thebool=False
        return final

        