class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        if len(A) != len(B):
            return False

        if A == B:
            # 只要出现过一次相同字符就可以进行交换
            s = set()
            for ch in A:
                if ch in s:
                    return True
                s.add(ch)
            return False

        # 剩下情况不相等的位置应该刚好是2个
        buf = []
        for i in range(len(A)):
            if A[i] != B[i]:
                if len(buf) >= 2:
                    return False
                buf.append([A[i], B[i]])

        return len(buf) == 2 and buf[0][0] == buf[1][1] and buf[0][1] == buf[1][0]
