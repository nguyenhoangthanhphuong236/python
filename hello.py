# Bai8
# import math 

# def factorial(n):
#     if(n == 1): 
#         return 1
#     else:
#         return (n * factorial(n-1))
    
# print("Nhập x: ")
# x = float(input())
# print("Nhập eps: ")
# eps = float(input())
# mu = 1
# first = x
# second = first + math.pow(x,mu)/factorial(mu+2)
# while(math.fabs(first - second) > eps):
#     mu += 2 
#     first = second
#     second = first + math.pow(x,mu)/factorial(mu+2)
# print(first)

# Bai1
# import math

# def factorial(n):
#     if(n == 1): 
#         return 1
#     else:
#         return (n * factorial(n-1))
# eps = 0.0001
# x =1
# mu = 1
# first = 1
# second = first + x**mu / factorial(mu)
# while (math.fabs(first - second) > eps):
#     mu = mu + 1
#     first = second
#     second = first + x**mu / factorial(mu)
# print(first)

# Bai2
# import math

# def factorial(n):
#     if(n == 1): 
#         return 1
#     else:
#         return (n * factorial(n-1))
# x = 0.5
# eps = 0.000001
# mu = 1
# dau = -1
# first = 1
# second = first + dau * ((mu+1) * (mu+2) / 2) * x**mu
# while (math.fabs(first - second) > eps):
#     mu = mu +1
#     dau = - dau
#     first = second
#     second = first + dau * ((mu+1) * (mu+2) / 2) * x**mu
# print(first)

# Bai4
# import math

# def factorial(n):
#     if(n == 1): 
#         return 1
#     else:
#         return (n * factorial(n-1))

# def tichChan(n):
#     rs = 1
#     for i in range(1, n + 1) :
#         if(i%2 == 0):
#             rs = rs * i
#     return rs
# def tichLe(n):
#     rs = 1
#     for i in range(1, n + 1) :
#         if(i%2 != 0):
#             rs = rs * i
#     return rs
# eps = 0.001
# x = 1
# mu = 1
# first = 1
# dau = 1
# second = first + dau * tichLe(mu * 2 - 2)/ tichChan(mu * 2) * x**mu
# while (math.fabs(first-second) > eps):
#     mu = mu + 1
#     dau = -dau
#     first = second
#     second = first + dau * tichLe(mu * 2 - 2)/ tichChan(mu * 2) * x**mu
# print(first)

# Bai3
# import math
# def factorial(n):
#     if(n == 1): 
#         return 1
#     else:
#         return (n * factorial(n-1))
# x = 1
# eps = 0.000001
# mu = 1
# first = 0
# second = - first - x**mu/ mu
# while (math.fabs(first - second) > eps):
#     mu = mu + 1
#     first = second
#     second = - first - x**mu / mu
# print(first)

# Bai5
# import math

# def factorial(n):
#     if(n == 1): 
#         return 1
#     else:
#         return (n * factorial(n-1))

# def tichChan(n):
#     rs = 1
#     for i in range(1, n + 1) :
#         if(i%2 == 0):
#             rs = rs * i
#     return rs
# def tichLe(n):
#     rs = 1
#     for i in range(1, n + 1) :
#         if(i%2 != 0):
#             rs = rs * i
#     return rs
# x = 0.5
# eps = 0.00001   
# mu = 1
# first = 1
# dau = -1
# second = first + dau *tichLe(mu*2)/ tichChan(mu * 2) * x**mu
# while (math.fabs(first-second)>eps):
#     mu = mu + 1
#     dau = -dau 
#     first = second
#     second = first + dau* tichLe(mu*2)/ tichChan(mu * 2) * x**mu
# print(first)

# Bai6
# import math

# def factorial(n):
#     if(n == 1): 
#         return 1
#     else:
#         return (n * factorial(n-1))
# eps = 0.001
# x = 1
# mu = 1
# dau = 1 
# first = 0
# second = first + dau * x**mu/ factorial(mu)
# while (math.fabs(first - second) > eps):
#     mu += 2
#     dau = -dau
#     first = second
#     second = first + dau * x**mu / factorial(mu)
# print(first)

# Bai7
# import math

# def factorial(n):
#     if(n == 1): 
#         return 1
#     else:
#         return (n * factorial(n-1))   
# eps = 0.001
# x = 1
# mu = 2
# dau = -1
# first = 1
# second = first + dau * math.pow(x,mu) / factorial(mu)
# while (math.fabs(first - second) > eps):
#     mu += 2
#     dau = -dau
#     first = second
#     second = first + dau * math.pow(x,mu) / factorial(mu)
# print(first)

# Bai9
# import math
# def factorial(n):
#     if(n == 1): 
#         return 1
#     else:
#         return (n * factorial(n-1))
# eps = 0.0001
# mu = 2
# x = 2
# dau = -1
# first = 1
# second = first + dau * x**mu / factorial(mu+1)
# while (math.fabs(first - second) > eps):
#     mu += 2
#     first = second
#     dau = -dau
#     second = first + dau * x**mu / factorial(mu+1)
# print(first)

# Bai10
# import math

# def factorial(n):
#     if(n == 1): 
#         return 1
#     else:
#         return (n * factorial(n-1))
# eps = 0.001
# x = 1
# mu = 1
# dau = 1
# first = 0
# second = first + dau * x**mu / mu
# while (math.fabs(first - second) > eps):   
#     mu += 2
#     dau = -dau
#     first = second
#     second = first + dau * x**mu / mu
# print(first)

# Bai11
# import math

# def factorial(n):
#     if(n == 1): 
#         return 1
#     else:
#         return (n * factorial(n-1))
# eps = 0.001
# x =1
# mu = 1
# dau = 1
# first = 0
# second = first + dau * x**mu / mu
# while (math.fabs(first - second) > eps):
#     mu = mu + 1
#     dau = -dau
#     first = second
#     second = first + dau * x**mu / mu
# print(first)

# Bai12
# import math

# def factorial(n):
#     if(n == 1): 
#         return 1
#     else:
#         return (n * factorial(n-1))   
# eps = 0.000001
# x = 0.5
# first = 1
# mu = 1
# second = 2 * (first * (mu + 2 ) * x**mu / mu)
# while (math.fabs(first - second) > eps):
#     mu += 2
#     first = second
#     second = 2 * (first * (mu + 2 ) * x**mu / mu)
# print(first)

# Bai13
# import math

# def factorial(n):
#     if(n == 1): 
#         return 1
#     else:
#         return (n * factorial(n-1))
# eps = 0.0001
# x = 1
# mu = 1
# first = 0
# second = first + x**mu / factorial(mu)
# while (math.fabs(first - second) > eps):
#     mu += 2
#     first = second
#     second = first + x**mu / factorial(mu)
# print(first)

# Bai14
# import math

# def factorial(n):
#     if(n == 1): 
#         return 1
#     else:
#         return (n * factorial(n-1))   
# eps =0.001
# x = 1
# mu = 2
# first = 1
# second = first + x**mu / factorial(mu)
# while (math.fabs(first - second) > eps): 
#     mu += 2
#     first = second
#     second = first + x**mu / factorial(mu)
# print(first)