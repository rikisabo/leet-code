# Longest Balanced Subarray
# balanced := (#distinct evens) == (#distinct odds)
# O(n log n) with Segment Tree (range add + find leftmost zero)

class SegTree:
    def __init__(self, n):
        self.n = n
        size = 4 * n
        self.mn = [0] * size   # min in segment
        self.mx = [0] * size   # max in segment
        self.lazy = [0] * size # lazy add

    def _apply(self, idx, val):
        self.mn[idx] += val
        self.mx[idx] += val
        self.lazy[idx] += val

    def _push(self, idx):
        if self.lazy[idx] != 0:
            val = self.lazy[idx]
            self._apply(idx * 2, val)
            self._apply(idx * 2 + 1, val)
            self.lazy[idx] = 0

    def range_add(self, ql, qr, val):
        if ql > qr:
            return
        self._range_add(1, 0, self.n - 1, ql, qr, val)

    def _range_add(self, idx, l, r, ql, qr, val):
        if qr < l or r < ql:
            return
        if ql <= l and r <= qr:
            self._apply(idx, val)
            return
        self._push(idx)
        mid = (l + r) // 2
        self._range_add(idx * 2, l, mid, ql, qr, val)
        self._range_add(idx * 2 + 1, mid + 1, r, ql, qr, val)
        self.mn[idx] = min(self.mn[idx * 2], self.mn[idx * 2 + 1])
        self.mx[idx] = max(self.mx[idx * 2], self.mx[idx * 2 + 1])

    def find_leftmost_zero(self, ql, qr):
        if ql > qr:
            return None
        return self._find_leftmost_zero(1, 0, self.n - 1, ql, qr)

    def _find_leftmost_zero(self, idx, l, r, ql, qr):
        if qr < l or r < ql:
            return None

        # אם כל הטווח חיובי או כל הטווח שלילי → אין בו 0
        if self.mn[idx] > 0 or self.mx[idx] < 0:
            return None

        if l == r:
            return l

        self._push(idx)
        mid = (l + r) // 2
        left = self._find_leftmost_zero(idx * 2, l, mid, ql, qr)
        if left is not None:
            return left
        return self._find_leftmost_zero(idx * 2 + 1, mid + 1, r, ql, qr)


class Solution:
    def longestBalanced(self, nums):
        n = len(nums)
        if n == 0:
            return 0

        st = SegTree(n)
        last = {}  # value -> last index
        best = 0

        for r in range(n):
            x = nums[r]
            prev = last.get(x, -1)

            delta = 1 if (x % 2 == 0) else -1
            st.range_add(prev + 1, r, delta)

            l = st.find_leftmost_zero(0, r)
            if l is not None:
                best = max(best, r - l + 1)

            last[x] = r

        return best
