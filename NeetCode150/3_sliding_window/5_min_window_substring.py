"""
-> create a hashamap of the  elements from the substring
->

"""
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        L = 0
        str_t = list(t)
        str_len = float("inf")
        newstring = []
        result = ""
        for R in range (len(s)):
            newstring.append(s[R])

            while all(item in newstring for item in str_t) :
                # print(f"Before Popping: {newstring}")
                result = "".join(newstring)
                str_len= min(str_len,R-L+1)
                newstring.pop(0)
                # print(f"Aftere Popping: {newstring}")
                L+=1

        # print(result)
        return result
"""
A D O B E C O D E B A N C ", "ABC
0 1 2 3 4 5 6 7 8 9 10 11 12
"""
print(Solution().minWindow("ADOBECODEBANC","ABC"))
print(Solution().minWindow("A","A"))
print(Solution().minWindow("a","aa"))


"""
Apprach 2: using hash map
"""

class Solution:
    def minWindow(self, s: str, t: str) -> str:

        res , reslen = [-1,-1] ,float("inf")
        t_map ={}
        window = {}
        for c in T:
            t_map[c] = 1 + t_map.get(c,0)
        have , need = 0 , len(t_map)

        l= 0
        for r in range (len(s)):
            c = s[r]
            window[c]  = 1+ window.get(c,0)

            if c in t_map and window[c]==t_map[c]:
                have+=1

            while have == need:
                if r-l+1<reslen:
                    res = [l,r]
                    reslen = [r-l+1]

                window[s[l]]-=1
                if s[l] in t_map and window[s[l]]<t_map[s[l]]:
                    have-=1
                l+=1

        l, r = res
        return s[l: r + 1] if resLen != float("infinity") else ""



