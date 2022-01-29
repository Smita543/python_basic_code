class employee1:
    def __init__(self):
        self.name = "smita"
        self.age = 20
        self.city = "gkp"


class employee2:
    def __init__(self):
        self.name = "khushi"
        self.age = 20
        self.city = "ntv"

    def compare(self,other):
        if self.city == other.city :
            return True
        else:
            return False


e1 = employee1()
e2 = employee2()
# print(e1.name)
# print(e1.age)
# print(e2.name)
# print(e2.age)


# if (e1.age == e2.age):
#     print ("same")
# else:
#     print("different")

if e2.compare(e1):
    print("they are same")
else:
    print("they are different")