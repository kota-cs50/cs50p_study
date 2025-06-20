# Week 1 課題まとめ

---

## deep.py（Deep Thought）

### 課題内容  
ユーザーが「42」または「forty-two」などの文字列を入力した際に、特別なメッセージを表示する。

### 確認したいこと
- str.strip()：入力された前後の空白を削除する（使い方が曖昧だった）
- str.lower()：入力をすべて小文字に変換（復習が必要）

---

## bank.py（Home Federal Savings Bank）

### 課題内容  
ユーザーの入力に応じて銀行の返答（"Hello", "How are you"など）を変化させる。

### 確認したいこと
- str.startswith()メソッドを初めて使ったため復習したい

---

## extensions.py（File Extensions）

### 課題内容  
ユーザーが入力したファイル名の拡張子を判別し、  
その拡張子に応じてMIMEタイプを出力する。

### 確認したいこと
- str.endswith() メソッドを初めて知ったので、使い方の確認が必要

---

## interpreter.py（Math Interpreter）

### 課題内容  
簡単な電卓プログラム。ユーザーが入力した数式（例："1 + 2"）を分割・計算して結果を表示する。

### 確認したいこと
- str.split(" ") を使って空白で文字列を分割し、複数の変数に代入する方法
- f"{value:.1f}" を使った少数第1位までのフォーマット（f文字列）
- float 型を使うことで、計算と出力の両方で少数処理が可能になる

---

## meal.py（Meal Time）

### 課題内容  
ユーザーから時刻（例："7:30"）を入力させ、それに応じて朝食・昼食・夕食の時間帯を判定し出力する。

### 確認したいこと
- main() と convert() の関係性が理解できていないので復習が必要
- print() を複数回に分けるか、変数にまとめて1回出力するかでの違い
- 何も出力しない場合、変数に None をあらかじめ代入しておく必要がある
