from collections import defaultdict, deque
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v, w in flights:
            graph[u].append((v, w))

        q = deque()
        q.append((src, 0, 0))  # (node, cost, stops)
        min_cost = [float('inf')] * n
        min_cost[src] = 0

        while q:
            curr_node, curr_cost, curr_stop = q.popleft()
            if curr_stop > k:
                continue
            for neighbor, price in graph[curr_node]:
                new_cost = curr_cost + price
                # Only push if we found a cheaper path or fewer stops to this node
                if new_cost < min_cost[neighbor]:
                    min_cost[neighbor] = new_cost
                    q.append((neighbor, new_cost, curr_stop + 1))

        return min_cost[dst] if min_cost[dst] != float('inf') else -1
