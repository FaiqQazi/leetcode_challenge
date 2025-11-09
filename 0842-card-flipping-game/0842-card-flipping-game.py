class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        best=float('inf')
        bad=[]
        for i in range(len(fronts)):
            if fronts[i]==backs[i]:
                bad.append(fronts[i])
        for i in range(len(fronts)):
            if fronts[i] in bad and backs[i] in bad:
                continue
            if fronts[i] in bad:
                best=min(best,backs[i])
                print(f"min between {best} and {backs[i]}")
                print(f"best is {best}")
            elif backs[i] in bad:
                best=min(best,fronts[i])
                print(f"min between {best} and {fronts[i]}")
                print(f"best is {best}")
            elif fronts[i] not in bad and backs[i] not in bad:
                print(f"min between {best} and {fronts[i]} and {backs[i]}")
                best=min(fronts[i],backs[i],best)
                print(f"best is {best}")
        if best==float('inf'):
            return 0
        else:
            return best



        