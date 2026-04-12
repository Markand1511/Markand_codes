# class a:

#     def __init__(self,n):
#         self.name=[n]

#     def __add__(self,new):
#         return self.name + new.name

#     def __len__(self):
#         return len(self.name)

#     def __str__(self):
#         return "5674894"

# b=a(10)
# z=a(10)
# print(b+z)
# print(len(b))
# print(b)

class a:

    name="markand"

    def __init__(self,x):
        self.x=x

    def show(self):
        print(self.x)

    @classmethod
    def change(cls,new):
        cls.name=new

b=a("om")
b.show()
b.change("dev")
print(b.name)




