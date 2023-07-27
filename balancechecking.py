class Solution:
    def isBalanced(self, parenthesis): 
            #type parenthesis: string
            #return type: boolean
            
            #TODO: Write code below to returnn a boolean value with the solution to the prompt. 
            count = 0
            print(parenthesis)
            for e in range(len(parenthesis)):
                count = 0
                char = parenthesis[e]
                for i in range(len(parenthesis)):
                    if ((char == parenthesis[i]) and (e != i)):
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
