class Solution:
    def hasSpecialSubstring(self, s: str, k: int) -> bool:

        for i in range(len(s)-k+1):
            curr = s[i:i+k]
            if len(set(curr)) == 1:
                if (i-1 >= 0 and s[i-1] not in curr) or i-1 < 0:
                    if (i+k < len(s) and s[i+k] not in curr) or i+k >= len(s):
                        return True
                    else:
                        continue
                else:
                    continue
            else:
                continue

        return False
