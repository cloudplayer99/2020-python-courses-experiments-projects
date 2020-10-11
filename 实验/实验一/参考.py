"""
多进程合适计算类。当计算结果很大的时候，采用多进程。
我们将1到100000000分段，用多进程对每段进行求和。
在将每段求和的结果汇集相加，就得到1到100000000的和了。
"""

########## 用多进程计算1-100000000的和 ###########
from multiprocessing import Pool


def sum_nums(start,end):
    # 计算分段中的数据之和
    result = 0
    for i in range(start,end+1):
        result += i
    return result

def main():
    pool = Pool(8)
    n = int(1e4)
    r = range(0,10**8+1,n)
    # 以0开头，100000000结尾，步长n为10000。即结果为0,10000，20000,30000……
    results = []
    for j in zip([x+1 for x in r],r[1:]):
        # x+1 for x in r结果为1,10001,20001,30001……
        # r[1:]结果为10000,20000,30000,40000……个数比上面的少1个
        # 用zip函数，结果为（1,10000），（10001,20000），（20001,30000）……列表长度与最短的对象相同，即与r[1:]个数相同
        # 这样就把1-100000000分段了。
        s = pool.apply_async(sum_nums,j)
        # 此处j是一个元组，所以直接在apply_async括号里填j就行
        # 此处得到的结果是multiprocessing.pool.ApplyResult 这种形式，需要用get函数将返回结果的值取出
        results.append(s)
    sum_results = 0
    for res in results:
        sum_results += res.get()
        # 此处res.get()取出的值是int类型

    pool.close()
    pool.join()
    print(sum_results)


if __name__ == '__main__':
    main()

"""
总结：
1. 求和用for循环和range函数搭配使用
2. 当数据很多时，选定分段的步长，然后将数据分段。此处用到的也是python最基本的list下标操作（r[1:]）和for循环
3. 用zip函数，它将对象中对应的元素打包成一个个元组，这样传递给我们的求和函数sum_nums,作为求和的数据开始值和结束值
4. 用进程池返回的不是int类型的值，我们需要用get()函数将返回的每个分段求和结果的值取出，再进行所有分段的值相加，最后得出1-100000000所有数据之和
"""