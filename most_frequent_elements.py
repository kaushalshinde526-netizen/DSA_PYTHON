from typing import List

topkFrequent = input("Enter the list of numbers (comma separated): ")
k = int(input("Enter the value of k: "))

nums = [int(x) for x in topkFrequent.split(",")]

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freq = {}

        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1

        sorted_items = sorted(
            freq.items(),
            key=lambda x: x[1],
            reverse=True
        )

        result = []

        for num, count in sorted_items[:k]:
            result.append(num)

        return result



sol = Solution()


answer = sol.topKFrequent(nums, k)

print("Top K Frequent Elements:", answer)