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
  class A
  {
      public:
          static int count;
      public:
          A()
          {

          }
  };

  int A::count = 0;

  int main()
  {
     A obj1;
     cout << obj1.count << endl;  // 0
     obj1.count++;
     A obj2;
     cout << obj2.count;          // 1
  }


Đối tượng static ảnh hưởng đến hàm hủy (destructor):
-> vì là đối tượng static nên hàm destruct chỉ hủy khi kết thúc chương trình hay vì hết scope của if(true)
  class A
  {
      public:
          A()
          {
              cout << "Constructor" << endl;
          }

          ~A()
          {
              cout << "Destructor" << endl;
          }
  };

  int main()
  {
     if(true)
     {
          static A obj;
     }
     cout << "Middle" << endl;
}


Hàm static trong class:
-> Hàm static cho phép gọi mà không cần đến khởi tạo đối tượng
  class A
  {
      public:
          static void print()
          {
              cout << "Hello world!\n";
          }
  };

  int main()
  {
      A::print();
  }


