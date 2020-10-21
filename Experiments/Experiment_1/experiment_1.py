import time
from multiprocessing import Process, Pool
import threading


def factorial(num):
    result = 1
    for i in range(1, num+1):
        result *= i
    return result


def factorial_mu(start, end):
    result_mu = 1
    for i in range(start, end+1):
        result_mu *= i
    return result_mu


class Mythread(threading.Thread):
    num1 = 0
    num2 = 0
    factorial1 = 1

    def run(self):
        self.factorial1 = 1
        for i in range(self.num1, self.num2 + 1):
            self.factorial1 *= i


if __name__ == '__main__':

    t1 = time.time()
    res1 = factorial(200000)
    t2 = time.time()
    str1 = repr(res1)
    str1 = str1[:10]
    print("res = {}\ntime = {}".format(str1, t2 - t1))

    print("start main threading")
    t3 = time.time()
    threads = [Mythread() for i in range(8)]
    res2 = 1
    j = 0
    for t in threads:
        num_j = 0 + j * 25000
        t.num1 = num_j + 1
        t.num2 = num_j + 25000
        t.start()
        j += 1
    for t in threads:
        t.join()
    for t in threads:
        res2 *= t.factorial1
    t4 = time.time()
    print("End Main threading")
    str2 = repr(res2)
    str2 = str2[:10]
    print("res = {}\ntime = {}".format(str2, t4 - t3))

    t5 = time.time()
    pool = Pool(8)
    r = range(0, 200001, 25000)
    results = []
    for j in zip([x+1 for x in r], r[1:]):
        # print(j)
        s = pool.apply_async(factorial_mu, j)
        results.append(s)
    res3 = 1
    for res in results:
        res3 *= res.get()
    pool.close()
    pool.join()
    t6 = time.time()
    str3 = repr(res3)
    str3 = str3[:10]
    print("res = {}\ntime = {}".format(str3, t6 - t5))
