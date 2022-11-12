import timeit
import numpy


def while_loop(n=100_000_000):
    i = 0
    s = 0
    while i < n:
        s += i
        i += 1
    return s


def for_loop(n=100_000_000):
    s = 0
    for i in range(n):
        s += i
    return s


def sum_range(n=100_000_000):
    return sum(range(n))


def numpy_sum(n=100_000_000):
    return numpy.sum(numpy.arange(n))


def math_sum(n=100_000_000):
    return (n * (n-1)) // 2


def main():
    print(f'While loop {timeit.timeit(while_loop, number=1)}')
    print(f'For loop {timeit.timeit(for_loop, number=1)}')
    print(f'Sum built in {timeit.timeit(sum_range, number=1)}')
    print(f'Numpy sum {timeit.timeit(numpy_sum, number=1)}')
    print(f'Math sum {timeit.timeit(math_sum, number=1)}')


if __name__ == '__main__':
    main()
