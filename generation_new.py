if __name__ == '__main__':
    str1_in = input()
    n, k = (int(i) for i in str1_in.split())
    str2_in = input()
    num_exp = [int(i) for i in str2_in.split()]
    # algorithm start
    poly1 = [0 for i in range(n + 1)]
    for i in range(0, n+1, num_exp[0]):
        poly1[i] = 1
    num_exp.pop(0)
    poly2 = [0 for i in range(n + 1)]
    for exp in num_exp:
        for j in range(n + 1):  # 遍历poly1中的每个项
            for k in range(0, n + 1 - j, exp):
                # 对于poly1中给定的幂j，g(x, i)中提供的项的幂不得超过num-j
                poly2[k + j] += poly1[j]  # 幂为k+j的项的系数增加1*poly1[j]
        poly1 = poly2  # 将poly2中的计算结果转存到poly1中
        poly2 = [0 for i in range(n + 1)]
    result = poly1[n] % 998244353
    print(result)
