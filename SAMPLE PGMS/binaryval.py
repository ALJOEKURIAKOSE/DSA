class Solution:
    def hammingWeight(self, n: int):
        i = 0
        entry = 0
        binval = bin(n)
        for i in binval:
             if i == '1':
                entry = entry+1
        print(entry)
inst = Solution()
inst.hammingWeight(11)
