## 注意大小写要统一，还要去除其他字符
python 
class Solution(object):
    def isPalindrome(self, s):
        i = 0
        length =0
        new_s = ''
        
        while(i<len(s)):
           
            if(('a'<=s[i] and s[i]<='z') or('A'<=s[i] and s[i]<='Z' )or ('0'<=s[i] and s[i]<='9') ):
                new_s += s[i]
                length += 1
#           if s[i+1] != '' :
            i += 1
        if(new_s == '' or len(new_s) == 1):
            return True
        for i in range(int(length/2)) :
            if new_s[i] != new_s[length-1-i]:
                if  new_s[i].isalpha() == False:
                    return False   
                if( ord(new_s[i])< ord(new_s[length-1-i])):
                    if(ord(new_s[i]) == ord(new_s[length-1-i]) -32):
                        continue
                else : 
                    if(ord(new_s[i]) == ord(new_s[length-1-i]) +32 ):
                        continue
                
                return False          
        return True

c++
class Solution {
public:
    bool isPalindrome(string s) {
        // 双指针
        if(s.size() <= 1) return true;
        int i = 0, j = s.size() - 1;
        while(i < j){
            while(i < j && !isalnum(s[i])) // 排除所有非字母或数字的字符
                i++;
            while(i < j && !isalnum(s[j]))
                j--;
            if(tolower(s[i++]) != tolower(s[j--])) //统一转换成小写字母再比较
                return false;
        }
        return true;
    }
};
python 3
class Solution:
    def isPalindrome(self, s: str) -> bool:
        i, j = 0, len(s) - 1
        while i < j:
            while i < len(s) and not s[i].isalnum():
                i += 1
            while j > -1 and not s[j].isalnum():
                j -= 1
            if i > j:
                return True
            if s[i].upper() != s[j].upper():
                return False
            else:
                i += 1
                j -= 1
        return True

