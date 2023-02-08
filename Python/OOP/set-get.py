# class SinhVien có 2 thuộc tính name, id và 2 phương thức set, get
class SinhVien:             # CamelCase 
    name = "NULL"
    id = -1

    def get(self):
        print(self.name)
        print(self.id)

    def set(self, name, id):
        self.name = name
        self.id = id


obj1 = SinhVien()
obj1.get()
print(type(obj1))   # <class '__main__.SinhVien'>

obj2 = SinhVien()
obj2.set("Khánh", 10)
obj2.get()
