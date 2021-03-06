# Time: O(n^2)
# Space: O(1)

class Solution:
    def longestPalindrome(self, s: str) -> str:

        if not s or s=="":
            return ""

        max_len = 0
        left = 0
        right = 0

        for i in range(len(s)):

            len1 = self.buildAroundCenter(s, i, i)
            len2 = self.buildAroundCenter(s, i, i+1)

            longer = max(len1, len2)

            if longer>max_len:
                left = i - ((longer-1)//2)
                right = i + (longer//2)
                max_len = longer

        return s[left:right+1]


    def buildAroundCenter(self, s, left, right):

        if right not in range(len(s)) or s[left]!=s[right]:
            return 0

        while left in range(len(s)) and right in range(len(s)) and s[left]==s[right]:
            left-=1
            right+=1

        return right-left-1

# Time: O(n^2)
# Space: O(n^2)
class Solution:
    def longestPalindrome(self, s: str) -> str:

        st_mat = [[False for _ in range(len(s))] for _ in range(len(s))]

        for i in range(len(s)):
            st_mat[i][i]=True

            if i+1 in range(len(s)):
                if s[i]==s[i+1]:
                    st_mat[i][i+1]=True

        # st_mat[i][j]=True if st_mat[i+1][j-1]==True and s[i]==s[j]

        # Order of filling up the matrix is important
        # We are essentially considering all combinations in this order:
        # [n-2..n-1], [n-3..n-1], [n-4..n-1], [0..n-1]
        for start in range(len(s)-2,-1,-1):
            for end in range(start+1, len(s)):

                if st_mat[start+1][end-1] and s[start]==s[end]:
                    st_mat[start][end] = True

        max_dim = (0,0)
        for row in range(len(s)):
            for col in range(row, len(s)):

                if st_mat[row][col]:
                    if col-row>max_dim[1]-max_dim[0]:
                        max_dim = (row,col)


        return s[max_dim[0]:max_dim[1]+1]
