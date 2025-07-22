### 定義
+ 一個函數呼叫它自己
+ 可以將大問題拆解為小問題 (base case)，現實生活中我們也稱這種概念叫做**分治** (Divide and Conquer)

----

### 如何寫遞迴函式？
1. 定義公式
2. 定義中止條件/回傳值
3. Code!

----

### 最直接的例子: 費氏數列
```python=
def fibnacci(n):
	if n == 0 or n == 1:
		return 1
	else:
		return fibnacci(n-1) + fibnacci(n-2)
```


----

### 階乘 ($!$)
```python=
def factorial(n):
	if n <= 1:
		return 1
	else:
		return n * factorial(n-1)
```


----

### 一起練習
+ https://snakify.org/en/lessons/functions/
+ 盡量不要使用遞迴以外的手法

----

### 遞迴有什麼缺點
1. 消耗大量記憶體
2. 重複計算，相當沒效率
3. 若遞迴深度過深，會導致 Stack Overflow

----

### 改進方式: 動態規劃 (Dynamic Programming)
+ 一樣將大問題轉化成子問題，但會將重複的子問題答案儲存，避免重複計算
+ Top-down v.s Bottom-up DP

----

### Better Fibonacci (Top-down)
```python=
fib = [-1] * 50
fib[0] = fib[1] = 1;

def fibnacci(n):
	if fib[n] != -1:
		return fib[n]
	else:
		fib[n] = fibnacci(n-1) + fibnacci(n-2)
		return fib[n]
```

----

### Better Fibonacci (Bottom-up)
```python=
fib = [-1] * 50
fib[0] = fib[1] = 1;

for i in range(2, 51):
	fib[i] = fib[i-1] + fib[i-2]

n = int(input("Please enter a positive integer"))
print(fib[n])
```
