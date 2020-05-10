A = [23, 2, 0, 5, 1, 6, 3, 7, 1, 9, 0, 22, 1, 15, 0]

for n in range(0, len(A) - 1):
    for i in range(0, len(A) - 1):
        if(A[i] > A[i + 1]):
            A[i], A[i + 1] = A[i + 1], A[i]
print(A)
