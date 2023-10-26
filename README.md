## 97 次方表
原始碼
```python
for i in range(1,8):
    print("^"+str(i),end="\t") 
print()
for i in range (2,10):
    for j in range(1,8):
        print(i**j,end="\t")
    print()
```
輸出
```
^1	^2	^3	^4	^5	^6	^7	
1	1	1	1	1	1	1	
2	4	8	16	32	64	128	
3	9	27	81	243	729	2187	
4	16	64	256	1024	4096	16384	
5	25	125	625	3125	15625	78125	
6	36	216	1296	7776	46656	279936	
7	49	343	2401	16807	117649	823543	
8	64	512	4096	32768	262144	2097152	
9	81	729	6561	59049	531441	4782969
```

## 金字塔1
原始碼
```python
r = range(1,int(input("高度幾層？ "))+1);
for i in r:
    print((len(r)-i)*" "+"* "*i)
```
輸出
```
高度幾層？ 3
  * 
 * * 
* * * 

高度幾層？ 12
           * 
          * * 
         * * * 
        * * * * 
       * * * * * 
      * * * * * * 
     * * * * * * * 
    * * * * * * * * 
   * * * * * * * * * 
  * * * * * * * * * * 
 * * * * * * * * * * * 
* * * * * * * * * * * * 

高度幾層？ 20
                   * 
                  * * 
                 * * * 
                * * * * 
               * * * * * 
              * * * * * * 
             * * * * * * * 
            * * * * * * * * 
           * * * * * * * * * 
          * * * * * * * * * * 
         * * * * * * * * * * * 
        * * * * * * * * * * * * 
       * * * * * * * * * * * * * 
      * * * * * * * * * * * * * * 
     * * * * * * * * * * * * * * * 
    * * * * * * * * * * * * * * * * 
   * * * * * * * * * * * * * * * * * 
  * * * * * * * * * * * * * * * * * * 
 * * * * * * * * * * * * * * * * * * * 
* * * * * * * * * * * * * * * * * * * * 

```

## 判斷閏年
原始碼
```python
def year(y):
    if y % 4 == 0 and (y % 100 != 0 or y % 400 == 0):
        print("是閏年")
    else:
        print("不是閏年")

year(int(input("請輸入年份： ")))
```
輸出
```
請輸入年份： 2023
不是閏年

請輸入年份： 2020
是閏年

請輸入年份： 1234
不是閏年
```

## 海龍
- 水怪公式只要給定三角形邊長便可計算面積

原始碼
```python
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
```

輸出

![image](https://github.com/proton-penguin/pypypypypypypypy/assets/142492829/4795bdb0-2cf9-4f96-9e33-550bdc232462)

