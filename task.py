# a=[1,2,3,4,5,6,7,8,9]
# print(a.index(6))
# # a.append(10)

# # print(a)
# # print(a.count(6))
# # a.sort()
# # print(a)
# # a.reverse()
# # print(a)

# a={1:"markand",2:"raj",3:"om",4:"dev"}
# print(a.keys())
# print(a.items())
# print(a[1])
# print(a.values())
# print(a.get(4))
# print(a.update({4:"rahul"}))
# a[5]="uu"
# print(a)
# del a[1]
# print(a)


# for i in a.values():
#     print(i)

# for i in a.keys():
#     print(i)

# for i in a.items():
#     print(i)

# a.update({5:"dev"})
# print(a)

# b=[1,2,3,4,5]
# print(b)
# print(b[1:3])
# b.append(6)
# print(b)
# b.pop()
# print(b)
# b.insert(6,6)
# print(b)
# b.copy()
# print(b)
# tryy=3
# user=input('you : ').lower()
# print(tryy)
# while user!='markand':
#     tryy-=1
#     if tryy==0:
#         break
#     user=input('you : ')
#     print(try


# with open('a.txt','w+')as f:
#     f.write("hy my name is markand")
#     f.seek(0)
#     print(f.tell())
#     print(f.read(5))
#     print(f.tell())
#     f.seek(14)
#     print(f.read())

from functools import reduce
a=[1,2,3,4,5,6,7,8,9,10]
print(list(map(lambda x:x*x,a)))
print(list(filter(lambda x: x%2==0,a)))
b=[1,2,3,4,5,6,7,8,9,10]
print(reduce(lambda x,y: x+y,b))
a=b
if a is b:
    print('y')
else:
    print('n')

def q(w):
    def e():
        print('1')
        w()
        print('3')
    return e

@q
def r():
    print('2')
r()

print(type(r))

a='1'
print(set(a))











