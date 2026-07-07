"""
Understand - 
Input: array of integers and an integer k where k is k most frequent element 
Output: list of the unique numbers of size k 

Plan - 
Hashmap (counter), priority queue 

Implement - 
1. Initialize the counter hashmap 
2. fill the counter hashmap with the freq of the elements in the array 
3. build a priority queue wrt the values of the elements 
4. loop over the top k elements in the priority queue and add to a res list 
5. return res list

"""
import heapq
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        count = Counter(nums)
        priority_queue = []
        for (key,value) in count.items():
            priority_queue.append((-value, key))
        heapq.heapify(priority_queue)
        res = []
        for i in range(k):
            res.append(heapq.heappop(priority_queue)[1])
        return res 
        """
        buckets = [[] for i in range(len(nums) + 1)]
        count = Counter(nums)
        max_freq = -1
        for key,value in count.items():
            buckets[value].append(key)
            if value > max_freq:
                max_freq = value 
        res = []
        for i in range(max_freq, 0, -1):
            res.extend(buckets[i])
            if len(res) == k:
                return res



        


        