# def dec_fun(fn):
#     def inn_fun(n1,n2):
#         if n1<n2:
#             (n1,n2)=(n2,n1)
#         return fn(n1,n2)
#     return inn_fun

# @dec_fun
# def sub(m1,m2):
#     return(m1-m2)

# @dec_fun
# def div(m1,m2):
#     return(m1/m2)

# print(sub(56,67))
# print(div(89,341))        




def dec_fun(fn):
    def inn_fun(y1,y2):
        return fn(y1**2,y2**2)
    return inn_fun



@dec_fun
def add(k1,k2):
    return (k1+k2)

@dec_fun
def product(u1,u2):
    return (u1*u2)


print(add(7,9))
print(product(6,8))


