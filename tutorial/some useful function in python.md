#### `list comprehension`
the concept of list comprehension is also applied to set and dictionary.
https://www.cc.ntu.edu.tw/chinese/epaper/home/News_Content_n_103858_s_246084.html
#### `map(function, iterable)`
it will take all element in an iterable object (like list, tuple), and put them into the function and generate some mapped result. (The iterable object can be multiple, anyway, it should follow the count of arguments of the given function).

```python=
arr = map(int, input().split(' ')) # it will return a map object (like iterator or address)
print(arr)

arr = list(arr) # for readability
print(arr)
```

#### `join(iterable)`
it will concatenate all shxt in an iterable object to one string using specified delimeters/seperators. Example:
```python
s = "###".join(["Taiwan", "Canada", "Brazil", "Japan"])
print(s)
```
The result should be `Taiwan###Canada###Brazil###Japan`