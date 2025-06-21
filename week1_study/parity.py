def main():
    x = int(input("What's x? "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")

def is_even(n):
    return  n % 2 == 0

main()

#ブール式（bool式）を使っている → 条件が「True（真）」か「False（偽）」かで処理を分岐させている


