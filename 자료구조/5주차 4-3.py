def checkBracketsUpgrade(statement):
    stack = []
    for ch in statement:
        if ch in ('{','[','('):
            stack.append(ch)
        elif ch in ('}',']',')'):
            if len(stack)==0:
                return False, 2,8,len(statement)
            else:
                left = stack.pop()
                if(ch=="}" and left !="{")or(ch=="]" and left !="[")or(ch==")" and left !="("):
                    return False ,3,12,len(statement)
    if not stack:
        return True,0, None,None
    if stack:
        return False,1, 16,len(statement)
        
myLines = ["{A[(i+1)] = 0}", "if ( (i==0) and (j==0):", "A[(i+1]) =0"]

for s in myLines:
    m,error,line,char  = checkBracketsUpgrade(s)
    print(s," ---> ", m, "에러코드:", error, "라인수: ",line,"문자수: ",char)