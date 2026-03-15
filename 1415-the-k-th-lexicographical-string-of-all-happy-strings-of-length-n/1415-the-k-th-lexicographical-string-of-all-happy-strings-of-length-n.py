class Solution(object):
    def getHappyString(self, n, k):
        total = 3 * (2 ** (n - 1))
        if k > total:
            return ""

        res = []
        prev = ""

        for pos in range(n):
            chars = ['a', 'b', 'c']
            if prev:
                chars = [ch for ch in chars if ch != prev]

            block_size = 2 ** (n - pos - 1)

            for ch in chars:
                if k > block_size:
                    k -= block_size
                else:
                    res.append(ch)
                    prev = ch
                    break

        return "".join(res)