class Solution:
    def isBalanced(self, parenthesis): 
        brackets = 0
        parens = 0
        curly = 0
        for p in parenthesis:
            if "{" == p:
                curly = curly + 1
            if "}" == p:
                curly -= 1
            if "[" == p:
                brackets += 1
            if "]" == p:
                brackets -= 1
            if "(" == p:
                parens += 1
            if ")" == p :
                parens -= 1
        if brackets == 0 and parens == 0 and curly == 0:
            return True
        return False
        
        pass

def main():
    str1=input()
    tc1= Solution()
    ans=tc1.isBalanced(str1)
    print(ans)

if __name__ == "__main__":
    main()
