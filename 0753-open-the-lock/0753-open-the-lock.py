from collections import deque
class Solution:
    def turn_knob_up(self,current,i):
        if current[i]=="9":
            num=0
        else:
            num=int(current[i])+1
        num_str=str(num)
        new_string = current[:i] + num_str + current[i+1:]
        return new_string
    def turn_knob_down(self,current,i):
        if current[i]=="0":
            num=9
        else:
            num=int(current[i])-1
        num_str=str(num)
        new_string = current[:i] + num_str + current[i+1:]
        return new_string


    def openLock(self, deadends: List[str], target: str) -> int:
        #make a graph
        graph={}
        graph["0000"]=[]
        queue=deque()
        queue.append(("0000",0))
        visited=set()

        while queue:
            #see if it is the target if it is then bactrack the path of the graph to see its path 
            current,steps=queue.popleft()
            if(current not in visited):
                visited.add(current)
            else:
                continue

            if current in deadends:
                continue
            
            if current==target:
                return steps
            else:
                #meaning that it is not the target
                #so we will make nodes on it 8 nodes with each dial up or down
                #and then append these nodes to the queue 
                
                for i in range(4):
                    up=self.turn_knob_up(current,i)
                    down=self.turn_knob_down(current,i)
                    queue.append((up, steps + 1))
                    queue.append((down, steps + 1))


                    
        return -1



                    




        