x = int(input("what's x ? "))
y = int(input("what's y ? "))

if x == y:
    print("x is equal to y")
else:
    print("x is not equal to y")

"""
if x < y:
    print("x is less then y")
elif x > y: 
    print("x is greater than y")
else:
    print("x is equal to y")

・elifは、ifの条件が成り立たなかった場合に使う追加の条件分岐。
・条件が一致すればその場で処理を終了するため、無駄がない。
・elseは、上のすべての条件に当てはまらなかった場合の処理を書く。
・条件が1つしか残っていないときに、コードを簡潔にできる。
"""

