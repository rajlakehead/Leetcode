from collections import deque

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        radiant = deque()
        dire = deque()
        n = len(senate)
        
        # Populate queues with indices
        for i, senator in enumerate(senate):
            if senator == 'R':
                radiant.append(i)
            else:
                dire.append(i)
        
        # Process the voting
        while radiant and dire:
            r_idx = radiant.popleft()
            d_idx = dire.popleft()
            
            # Whoever comes first gets to ban the other and moves to the next round
            if r_idx < d_idx:
                radiant.append(r_idx + n)  # Move to the next round
            else:
                dire.append(d_idx + n)
        
        return "Radiant" if radiant else "Dire"
