def fibonacci(x):
    sequence = []

    curr = 1
    prev = curr-1

    sequence.append(curr)

    for i in range(x-1):
        sum_ = curr + prev
        sequence.append(sum_)

        prev = curr
        curr = sum_

    return sequence

print(", ".join(map(str, fibonacci(int(input("\nNumber of Fibonaccis: "))))))
