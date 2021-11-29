import time

def timeit(f):

    def timed(*args, **kw):

        ts = time.time()
        result = f(*args, **kw)
        te = time.time()
        print("Starting time:",ts*1000)
        print("Ending time:",te*1000)
        d=te-ts
        print("Difference:",d)
        return result

    return timed

@timeit
def fib(n):
    a, b = 0, 1
    while a < n:
        yield a
        a, b = b, a + b

n=int(input("Enter n:"))
for i in fib(n):
    print(i)