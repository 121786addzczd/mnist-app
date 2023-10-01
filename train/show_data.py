from sklearn.datasets import fetch_openml

X, y = fetch_openml("mnist_784", version=1, return_X_y=True, as_frame=False)
print("Fetch OpenML completed")

print(f"len(X) - {len(X)}, len(y) = {len(y)}")

print("X[0]")
print(X[0])

print("y[0]")
print(y[0])

X0 = X[0]
print(f"len(X0) = {len(X0)}") # 28×28のデータ

print("x0")
for i, v in enumerate(X0):
    # 数字の部分を3桁で表示
    print("%3d " % v, end="") # printするごとに改行しないようにend=""
    if i % 28 == 27:
        # MMNISTのデータは28×28(784)のデータになっている
        print()


