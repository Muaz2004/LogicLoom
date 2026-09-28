
class Solution:
    def grayCode(self, n: int) -> list[int]:
        maxi: int = (2 ** n)

        ans: list[int] = []
        for i in range(0, maxi):
            curr_code: int = i ^ (i // 2)
            ans.append(curr_code)

        return ans