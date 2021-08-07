a = int(2.7) # 2                float para int
b = float(a) # 2.0              int para float
c = complex(b) #(2+0j)          float para complexo
d = str(c) # "(2+0j)"           complexo para string

l1 = [1,2,3]
l2 = [1,4,9]
dic = dict(zip(l1,l2))          duas list para dict

t1 = 1,2,3
l_t1 = list(t1) #               tupla para lista
t2 = tuple(l_t1) #              lista para tupla

s1 = set(t1) #                  tupla para set
s2 = set(l_t1) #                lista para tupla
