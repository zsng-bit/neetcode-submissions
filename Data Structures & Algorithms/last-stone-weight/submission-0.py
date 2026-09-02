class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            stones = sorted(stones)
            first_stone = stones.pop(len(stones)-1)
            second_stone = stones.pop(len(stones)-1)
            stones.append(abs(first_stone-second_stone))
        return stones[0]

