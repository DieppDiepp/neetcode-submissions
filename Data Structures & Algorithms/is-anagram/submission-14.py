class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
            
        char_count = {}
        
        for i in range(len(s)):
            # Lấy giá trị hiện tại, nếu chưa có thì mặc định là 0
            char_count[s[i]] = char_count.get(s[i], 0) + 1
            char_count[t[i]] = char_count.get(t[i], 0) - 1
            
        # Kiểm tra xem có ký tự nào khác 0 không
        for count in char_count.values():
            if count != 0:
                return False
                
        return True