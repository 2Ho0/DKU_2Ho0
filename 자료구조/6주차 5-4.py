from collections import deque

def checkPalindromeByDeque(isPalindrome):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    isPalindrome = isPalindrome.lower()
    queue = deque([])

    for i in isPalindrome:
        if i in alphabet:
            queue.append(i)
    
    for i in range(len(queue)):
        tmp = queue.popleft()
        
        if tmp == queue[-1]:
            del queue[-1]
        else:
            print("회문이 아닙니다")
            break
        if len(queue) == 1 or len(queue)==0:
                    print("회문이 맞습니다")
                    break
                
myLines = ["madam, I'm Adam", "race car"]
for s in myLines:
    checkPalindromeByDeque(s)