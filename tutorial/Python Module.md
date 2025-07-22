
----

### 安裝模組
```
pip install [module_name]
```


----

### 引入模組
```python
import math

print(math.pow(2, -10))
```

----

### 只引入部份方法/常數
```python=
from math import pow, sqrt

print(pow(2, -10))
print(sqrt(3))
```

----

### 如何寫自己的函式?
1. 創建一個寫有函式、常數的 python 檔
2. 將它放在主程式同一個資料夾
3. 用前面教的方法使用模組中的函式/常數就可以了 (例如 `import module`， 如果你放函式的檔案叫做 `module.py` 的話)

