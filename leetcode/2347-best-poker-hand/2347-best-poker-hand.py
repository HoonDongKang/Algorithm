class Solution(object):
    def bestHand(self, ranks, suits):
        """
        :type ranks: List[int]
        :type suits: List[str]
        :rtype: str
        """
        if suits.count(suits[0]) == len(suits):
            return "Flush"

        rank_map = {}
        for num in ranks:
            rank_map[num] = rank_map.get(num, 0) + 1

        max_count = max(rank_map.values())

        if max_count >= 3:
            return "Three of a Kind"
        elif max_count == 2:
            return "Pair"
        else:
            return "High Card"
