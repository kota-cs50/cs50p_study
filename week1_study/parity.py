def main():
    x = int(input("What's x? "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")

def is_even(n):
    return  n % 2 == 0

main()

#bool式が使われている→真偽のどちらかをきいてどちらかを返すもの。

