# Cấu trúc điều kiện
diem = input()
if not (diem.isdigit()):
    print("Điểm phải là ký số")
elif diem >= '8':
    print("Học sinh giỏi")
elif (diem >= '5') and (diem < '8'):
    print("Học sinh khá")
elif (diem >= '3') and (diem < '5'):
    print("Học sinh trung bình")
else:
    print("Học sinh yếu")

    
# Cấu trúc điều kiện kèm theo từ khóa in
numberString = "123"
if '1' in numberString:
    print("contain 1")


