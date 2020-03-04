class Solution:
    def reverseWords(self, s: str) -> str:
        temp =''
        start = 0
        end   = 0
        for i in s:
            if(i != ' '):
                end +=1
                
            else:
                temp += (s[start :end][::-1])
                temp += ' '
                start = end+1
                end  = start
        temp += (s[start:][::-1])
        return temp       
自己的方法可以将 s 后面补齐个空格

join 方法
class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(s.split(' ')[::-1])[::-1]
        
        
class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join([i[::-1] for i in s.split()])

作者：qsctech-sange
链接：https://leetcode-cn.com/problems/reverse-words-in-a-string-iii/solution/python3-yi-xing-ji-su-by-jimmy00745/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

堆栈方法：
class Solution:
    def reverseWords(self, s: str) -> str:
        s=s+" "
        stack,res=[],""
        for i in s:
            stack.append(i)
            if i==" ":
                while(stack):
                    res=res+stack.pop()
        return res[1:]

作者：mian-mian-sir
链接：https://leetcode-cn.com/problems/reverse-words-in-a-string-iii/solution/python-chang-gui-jie-fa-li-yong-dui-zhan-by-mian-m/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。