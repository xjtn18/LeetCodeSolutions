import sys
sys.path.append("../")
from parseTC import *

#START
class Solution:
    def merge(self, nums1: [int], m: int, nums2: [int], n: int) -> None:
        y = 0 # y is the current index into nums2
        for x in range(m+n):
            if y == n: break
            if x == (m + y): # we've reached the 'end' of nums1 array
                nums1[x] = nums2[y]
                y += 1 # change current index into nums2 to get the next number to merge
            elif nums1[x] > nums2[y]:
                b = m + y - 1
                while b >= x:
                    nums1[b+1] = nums1[b]
                    b -= 1
                nums1[b+1] = nums2[y]
                y+=1

        return nums1
#END

print('\n### TESTCASES ###')
tcs, exps = get_testcases()
for x in range(len(tcs)):
    inp = tcs[x]
    func_name = "merge"
    exec("output = Solution()." + func_name + "(" + inp + ")")
    outcome = 'pass' if output == exps[x] else 'FAIL'
    print(inp, '-->', output, ':::', exps[x], '[' + str(outcome) + ']')
print("")


