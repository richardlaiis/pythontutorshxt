
### 區域變數 (local variable)
在函數裡面宣告的變數，只能在**函數裡面**使用。

----

### 全域變數 (global variable)
在主程式 (main function) 中宣告，**宣告之後**可以在程式**任何區塊**使用

----

```python=
def myfunc():
	x = 300
	print(x)
myfunc()
```

----

```python=
def myfunc():
	x = 300  
	def myinnerfunc():
		print(x)  
	myinnerfunc()  
myfunc()
```

----

```python=
x = 300  
def myfunc():
	print(x)  
  
myfunc()
print(x)
```

----

### what is the output?
```python=
x = 300
  
def myfunc():
	x = 200
	print(x)  
  
myfunc()
print(x)
```

----

透過 `global` 這個關鍵字，我們可以將所指的變數變為全域！
```python=
def myfunc():
	global x
	x = 300  

myfunc()
print(x)
```

----

```python
x = 300  
  
def myfunc():
	global x
	x = 200

myfunc()  
print(x)
```

----

[reference - Python Scope](https://www.w3schools.com/python/python_scope.asp)