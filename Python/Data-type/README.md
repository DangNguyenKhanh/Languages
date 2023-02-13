KIỂU DỮ LIỆU CÓ THỂ THAY ĐỔI ĐƯỢC KHÔNG THAY ĐỔI ĐƯỢC- IMMUTABLE
- int, float, str, bool, tuple
- Example:
x = 42      # tạo mới đối tượng object integer thứ nhất
x = x + 1   # tạo mới đối tượng object integer thứ hai
- Ta thấy được thay vì thay đổi giá trị thì trình biên dịch lại tạo mới đối tượng nên được gọi là immutable

KIỂU DỮ LIỆU CÓ THỂ THAY ĐỔI ĐƯỢC - MUTABLE
- list, dict, set
- Thành phần của list và tuple có thể bất kì kiểu dữ liệu nào
- Thành phần của set là bất kỳ trừ set, list, dict
- Thành phần dict: key là immutable và value là bất kỳ
