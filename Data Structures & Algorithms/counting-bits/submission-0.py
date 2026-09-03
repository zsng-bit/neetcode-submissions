class Solution:
    def countBits(self, n: int) -> List[int]:
        new_l = []
        num = range(n+1)
        for i in num:
            count = 0
            for j in bin(i)[2:]:
                if j == '1':
                    count += 1
            new_l.append(count)
        return new_l
            


            
            
        
        