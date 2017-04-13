## 使用する外部ライブラリ
* `NumPy`: 数値計算ライブラリ
* `Matplotlib`: グラフ描画ライブラリ

## 使用するディストリビューション
* `Anaconda`: データ分析に重点を置いたディストリビューション
    * `NumPy`、`Matplotlib`も本ディストリビューションに含まれる
    * `brew`などで入れてもいいが、ここでは使用するパッケージが含まれるAnacondaを使用する
    * `brew`などで入れた場合、各自で`NumPy`、`Matplotlib`等のパッケージは手動で入れること

[Download Anaconda Now\! \| Continuum](https://www.continuum.io/downloads#osx)

## 算術演算
* 四則演算は他のプログラミング言語と比較して特筆すべき点はない
* Python3系では整数同士の除算は小数になる

## データ型
* Pythonは全てがオブジェクトである
* `type()`で確認可能
    * `int`、`float`、`str`など

## 変数
他のプログラミング言語と比較して特筆すべき点はない。定義方法は以下。

```python
x = 10
print(x) # 10
```

## リスト(配列)
他のプログラミング言語と比較して特筆すべき点はない。定義方法は以下。

```python
a = [1,2,3,4,5]
print(a) # [1, 2, 3, 4, 5]
```

### スライシング
* リストのサブリストにアクセス可能
* 範囲指定で配列内の任意の範囲にアクセスできる

```python
a[1:3] # [2, 3]
a[3:]  # [4, 5]
a[:-2] # [1, 2, 3]
```

## ディクショナリ
連想配列。最近はディクショナリというのが流行り？らしい。

```python
me = {'height': 180}
print(me)    # {'height': 180}
me['height'] # 180
```

## クラス
Pythonのクラスの特徴として、メソッドの第一引数に`self`を渡す

see: `./src/man.py`

## NumPy
### import
他の言語と同じように冒頭で`import`して使用する

```python
import numpy as np
```

### NumPy配列
`np.array()`でNumPyの配列を生成するには以下のメソッドを使用する。生成されたオブジェクトは、`numpy.ndarray`である。

```python
x = np.array([1.0, 2.0, 3.0])
print(x) # [ 1.  2.  3.]
type(x)  # numpy.ndarray
```

### NumPy算術演算
要素ごとの演算。要素数が異なる場合はエラーとなる。

```python
x = np.array([1.0, 2.0, 3.0])
y = np.array([2.0, 4.0, 6.0])
x + y # array([ 3.,  6.,  9.])
x - y # array([-1., -2., -3.])
x * y # array([  2.,   8.,  18.])
x / y # array([ 0.5,  0.5,  0.5])
```

スカラ値との演算も可能

```python
x / 2.0 # array([ 0.5,  1. ,  1.5])
```

### NumPyのN次元配列
* `shape`: データ形状
* `dtype`: データ型

```python
A = np.array([[1, 2], [3, 4]])
print(A)
# [[1 2]
#  [3 4]]
A.shape # (2, 2)
A.dtype # dtype('int64')
```

* 同じ形状の行列であれば算術演算可能。スカラ値も前述同様

```python
A = np.array([[1, 2], [3, 4]])
B = np.array([[3, 0], [0, 6]])
A + B
# array([[ 4,  2],
#        [ 3, 10]])
A * B
# array([[ 3,  0],
#        [ 0, 24]])
```

### ブロードキャスト
要素数の異なる配列でも、自動的に拡大されて演算される。前述のスカラ値であれば、スカラ値の`shape`を同じ大きさまで拡大してから演算している。

### 要素へのアクセス
通常のインデックスを用いたアクセス以外にも、配列によって要素へのアクセスが可能。

```python
X = np.array([[51, 55], [14, 19], [0, 4]])
X = X.flatten()
print(X)               # [51 55 14 19  0  4]
X[np.array([0, 2, 4])] # array([51, 14,  0])
```

NumPyの配列に対して不等号演算をすると結果は`Boolean`となる。さらにこれを使って`True`に対応する要素のみを抜き出すことも可能。

```python
X > 15                 # array([ True,  True, False,  True, False, False], dtype=bool)
X[X > 15]              # array([51, 55, 19])
```
