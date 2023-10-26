CRED = "\033[41m"
CGRE = "\033[42m"
CYEL = "\033[43m"
CBLU = "\033[44m"
CPUR = "\033[45m"
CEND = "\033[0m"
def sqrt(n):
    return float(n)**0.5
def sqr(n):
    return float(n)**2
def pow(n,p):
    return float(n)**float(p)
def printc(sen,col):
    print(col + sen + CEND)
def hilong():
    s1 = float(input("輸入第一個邊長： "))
    s2 = float(input("輸入第二個邊長： "))
    s3 = float(input("輸入第三個邊長： "))
    if s1>0 and s2>0 and s3>0 and s1+s2>s3 and s1+s3>s2 and s2+s3>s1:
        twoS = s1+s2+s3
        ans = sqrt(twoS*(twoS-s1*2)*(twoS-s2*2)*(twoS-s3*2)/pow(2,4))
        printc("由水怪公式計算出面積= "+str(ans)+"平方單位",CGRE)
    else:
        printc("error, please try again! ",CRED)
        hilong()
hilong()
