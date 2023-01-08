Biến static trong hàm:
- Là biến cục bộ trong hàm nhưng tồn tại cho đến khi chương trình kết thúc
- Biến static chỉ được khởi tạo 1 lần, các lần sau trình biên dịch sẽ bỏ qua đoạn mã đó
  void A()
  {
      static int count = 0;
      count++;
      cout << count << endl;
  }
  int main()
  {
      A();    // 1
      A();    // 2
  }

Biến static trong class:
