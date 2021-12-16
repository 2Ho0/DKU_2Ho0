def testPalindrome(isPalindrome):

    alphabet = "abcdefghijklmnopqrstuvwxyz"
    isPalindrome = isPalindrome.lower()
    s = []

    for i in isPalindrome:
        if i in alphabet:
            s.append(i)
    
    for i in range(len(s)):
        tmp = s.pop()
        
        if tmp == s[0]:
            del s[0]
        else:
            print("회문이 아닙니다")
            break
        if len(s) == 1 or len(s)==0:
                    print("회문이 맞습니다")
                    break


testPalindrome("madam, i'm Adam")
testPalindrome("race car")
