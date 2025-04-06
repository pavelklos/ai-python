# 137 : Exercise: Extending List


class SuperList(list):

    def __len__(self):
        return 1000


super_list1 = SuperList()
print(type(super_list1))  # <class '__main__.SuperList'>
print(len(super_list1))  # 1000

super_list1.append(5)
super_list1.append(10)
super_list1.append(15)
print(super_list1)  # [5]
print(super_list1[0])  # 5
print(issubclass(SuperList, list))  # True
print(issubclass(list, object))  # True
