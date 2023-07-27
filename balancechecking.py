class Solution:
    def isBalanced(self, parenthesis): 
            #type parenthesis: string
            #return type: boolean
            dict = {"}":"{", "]":"[",")":"(", "{":"}", "[":"]","(":")"}
            list = []
            if len(parenthesis) <= 1:
                return False
            for c in parenthesis:
                if c in dict:
                    list.append(c)
            print(list)
            #TODO: Write code below to returnn a boolean value with the solution to the prompt. 
            count = 0
            print(parenthesis)
            for e in range(len(list)):
                count = 0
                char = parenthesis[e]
                for i in range(e, len(list)):
                    if ((char == dict[list[i]]) and (e != i)):
                         count = count+1
                if count == 0:
                    return False
            return True
                    
                
            pass

def main():
    str1=input()
    tc1= Solution()
    ans=tc1.isBalanced(str1)
    print(ans)

if __name__ == "__main__":
    main()
