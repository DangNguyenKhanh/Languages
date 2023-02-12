# Ghi dữ liệu bằng lệnh write
f = open("inp.dat", 'w')
f.write("Dang Nguyen Khanh\n")
f.write("31082002\n")
f.close()


# Ghi dữ liệu bằng print sẽ mặc định có kí tự \n - hay dùng
f = open("inp.dat", 'w')
print("Dang Nguyen Khanh", file=f)
print("ID:", file=f, end=' ')   # Tùy chỉnh
print("31082002", file=f)
f.close()


# Ghi dữ liệu f.writelines(list)
f = open("inp.dat", 'w')
a = ["abc\n", "123\n", "ABC\n"]
f.writelines(a)
f.close()


#
