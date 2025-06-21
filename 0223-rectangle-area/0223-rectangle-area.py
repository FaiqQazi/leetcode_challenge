class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        print(f"\n=== Starting computeArea ===")
        print(f"Input Rectangles:")
        print(f"Rectangle A: ({ax1}, {ay1}), ({ax2}, {ay2})")
        print(f"Rectangle B: ({bx1}, {by1}), ({bx2}, {by2})\n")
        
        l1 = ax2 - ax1
        w1 = ay2 - ay1
        l2 = bx2 - bx1
        w2 = by2 - by1
      
        
        
        if not (ax2 <= bx1 or ax1 >= bx2 or ay2 <= by1 or ay1 >= by2):

            m_l=0
            m_w=0
            if (bx1 <= ax1 <= bx2 or bx1 <= ax2 <= bx2 or ax1 <= bx1 <= ax2 or ax1 <= bx2 <= ax2):
                new_x1 = min(ax1, ax2, bx1, bx2)
                new_x2 = max(ax1, ax2, bx1, bx2)
                unknown = sorted([ax1,ax2,bx1,bx2])
                unknown=unknown[1:3]
                m_l = max(unknown)-min(unknown)
                
            if (by1 <= ay1 <= by2 or by1 <= ay2 <= by2 or ay1 <= by1 <= ay2 or ay1 <= by2 <= ay2):
                new_y1 = min(ay1, ay2, by1, by2)
                new_y2 = max(ay1, ay2, by1, by2)
                unknown = sorted([ay1,ay2,by1,by2])
                unknown=unknown[1:3]
                m_w = max(unknown)-min(unknown)

            m_area = m_l * m_w
            area = (l1*w1)+(l2*w2)
            return area - m_area

        else:
            a1 = l1 * w1
            a2 = l2 * w2
            area = a1 + a2
            return area
