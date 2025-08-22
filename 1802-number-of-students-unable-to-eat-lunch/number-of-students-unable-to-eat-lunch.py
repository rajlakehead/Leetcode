class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        count = Counter(students)
        q1 = deque(sandwiches)
        q2 = deque(students)

        while q1 and q2:
            if q1[0] == q2[0]:
                count[q1[0]] -= 1
                if count[q1[0]] == 0:
                    del count[q1[0]]
                q1.popleft()
                q2.popleft()
                
            else:
                q2.append(q2.popleft())
            
            
            if len(count) == 1 and q1[0] != q2[0]:
                return count[q2[0]]
            

        return 0
        