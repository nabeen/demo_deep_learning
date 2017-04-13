## 使用する外部ライブラリ
* NumPy:数値計算ライブラリ
* Matplotlib:グラフ描画ライブラリ

## 使用するディストリビューション
* Anaconda:データ分析に重点を置いたディストリビューション
    * NumPy、Matplotlibも本ディストリビューションに含まれる

[Download Anaconda Now\! \| Continuum](https://www.continuum.io/downloads#osx)

## 算術演算
* Python3系では整数同士の除算は小数になる

## データ型
* `type()`で確認可能
    * `int`、`float`、`str`など

## 変数
```python
x = 10
print(x) # 10
```

## リスト(配列)
```python
a = [1,2,3,4,5]
print(a) # [1, 2, 3, 4, 5]
```

### スライシング
* リストのサブリストにアクセス可能

```python
a[1:3] # [2, 3]
a[3:]  # [4, 5]
a[:-2] # [1, 2, 3]
```

## ディクショナリ
```python
me = {'height': 180}
print(me)    # {'height': 180}
me['height'] # 180
```

## クラス
* メソッドの第一引数に`self`を渡す

## NumPy
### import
他の言語と同じように冒頭で`import`して使用する

```python
import numpy as np
```

### NumPy配列
`np.array()`でNumPyの配列を生成する

```python
x = np.array([1.0, 2.0, 3.0])
print(x) # [ 1.  2.  3.]
type(x)  # numpy.ndarray
```