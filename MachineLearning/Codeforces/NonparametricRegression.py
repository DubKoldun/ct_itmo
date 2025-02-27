from math import sqrt, pi, e, cos

n, m = input().split()
n = int(n)
m = int(m)

matrix = [[int(j) for j in input().split()] for i in range(n)]
request = [int(j) for j in input().split()]

def convert(ma):
    updma = []
    m_att = []
    for i in ma:
        buff = []
        for j in range(len(i)-1):
            buff.append(i[j])
        updma.append(buff)
        m_att.append(i[len(i)-1])
    return (updma, m_att)

matrix, main_attributes = convert(matrix)

def euclidean_distance(vec1, vec2):
    ans = 0.
    for i in range(len(vec1)):
        ans += (vec1[i] - vec2[i]) ** 2
    return sqrt(ans)

def manhattan_distance(vec1, vec2):
    ans = 0.
    for i in range(len(vec1)):
        ans += abs(vec1[i] - vec2[i])
    return ans

def chebyshev_distance(vec1, vec2):
    ans = float("-inf")
    for i in range(len(vec1)):
        ans = max(ans, abs(vec1[i] - vec2[i]))
    return ans

def in_range_one(variable, value):
    return value if abs(variable) < 1 else 0

kernel_functions = {
    "uniform":      lambda u: in_range_one(u, 0.5),
    "triangular":   lambda u: in_range_one(u, 1 - abs(u)),
    "epanechnikov": lambda u: in_range_one(u, 0.75 * (1 - u ** 2)),
    "quartic":      lambda u: in_range_one(u, (15 / 16) * (1 - u ** 2) ** 2),
    "triweight":    lambda u: in_range_one(u, (35 / 32) * (1 - u ** 2) ** 3),
    "tricube":      lambda u: in_range_one(u, (70 / 81) * (1 - abs(u) ** 3) ** 3),
    "gaussian":     lambda u: (1 / (2 * pi) ** (0.5)) * e ** (-0.5 * u ** 2),
    "cosine":       lambda u: in_range_one(u, (pi / 4) * cos(pi * u / 2)),
    "logistic":     lambda u: 1 / (e ** u + 2 + e ** (-u)),
    "sigmoid":      lambda u: 2 / (pi * (e ** u + e ** (-u)))
}

distance_functions = {
    "euclidean": euclidean_distance,
    "manhattan": manhattan_distance,
    "chebyshev": chebyshev_distance
}

def suma(m):
    buff = 0.
    for i in m:
        buff += i
    return buff


distances_by_fun = {
    "euclidean": [],
    "manhattan": [],
    "chebyshev": []
}

def calculate_distances():
    for dis_fun_name in distance_functions.keys():
        for obj1 in matrix:
            buff = distance_functions[dis_fun_name](request, obj1)       
            distances_by_fun[dis_fun_name].append(buff)

calculate_distances()

def kernel_regression(objs, x, neighbours = 0, window_size = 0, distance_function_name = "euclidean", kernel_function_name = "triangular"):
    kernel_function = kernel_functions[kernel_function_name]

    distances = distances_by_fun[distance_function_name]
    sorted = distances.copy()
    sorted.sort()

    window_parameter = 0.
    if (neighbours == 0):
        window_parameter = float(window_size)
    else:
        window_parameter = sorted[neighbours] 
    
    sum = 0.
    denominator = 0.

    if (window_parameter == 0.):
        window_parameter = 1.

    for i in range(len(objs)):
        buff = kernel_function(distances[i] / window_parameter)
        sum = sum + main_attributes[i] * buff
        denominator += buff
    
    return sum / denominator if denominator != 0. else suma(main_attributes) / len(objs)

dist_fun = input()
ker_fun = input()
window_type = input()
window_s = int(input())

if (window_type == "variable"):
    print('%.10f' % kernel_regression(matrix, request, neighbours = window_s, distance_function_name = dist_fun, kernel_function_name = ker_fun))
else:
    print('%.10f' % kernel_regression(matrix, request, window_size = window_s, distance_function_name = dist_fun, kernel_function_name = ker_fun)) 
    
    