class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
            
        # Mảng đếm 26 số 0 tương ứng với 26 chữ cái từ 'a' đến 'z'
        count = [0] * 26 
        
        for i in range(len(s)):
            # Tăng biến đếm cho ký tự trong s
            count[ord(s[i]) - ord('a')] += 1
            # Giảm biến đếm cho ký tự trong t
            count[ord(t[i]) - ord('a')] -= 1
            
        # Nếu là anagram, tất cả các phần tử trong count phải triệt tiêu về 0
        for c in count:
            if c != 0:
                return False
                
        return True