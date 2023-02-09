# Hàm khởi tạo
class SinhVien:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def get(self):
        print(self.name)
        print(self.id)

    def set(self, name, id):
        self.name = name
        self.id = id


obj1 = SinhVien("Khanh", 1)
obj2 = SinhVien("Hieu", 2)

print(obj1)     # <__main__.SinhVien object at 0x00000235099CCD90>

obj1.get()
obj2.get()


