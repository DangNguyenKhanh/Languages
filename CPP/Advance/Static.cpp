1. Biến static trong main:
  int main()
  {   
      for(int i = 0; i < 10; i++)
      {
          static int value = 0;
          value++;
          if(value == 9)
              cout << value << endl;
      }
  }


2. Biến static trong hàm:
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


3. Biến static trong class:
-> Được khởi tạo trước khi biên dịch tới hàm main
  class A
  {
      public:
          static int count;   // Khai báo bên trong - Muốn sử dụng được phải định nghĩa
      public:
          A()
          {
              count++;
          }
  };

  int A::count = 0;   // Định nghĩa bên ngoài 

  int main()
  {
     A obj1;
     cout << obj1.count << endl;  // 0
     A obj2;
     cout << obj2.count;          // 1
  }


4. biến đối tượng static trong class:
  class A
  {
      public:
          A() { cout << "A's Constructor Called " << endl;  }
  };

  class B
  {
      public:
          static A a;
      public:
          B() { cout << "B's Constructor Called " << endl; }
  };

  A B::a;   

  int main()
  {
      B b;
      return 0;
      // A's Constructor Called
      // B's Constructor Called
  }


5. Đối tượng static ảnh hưởng đến hàm hủy (destructor):
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


6. Hàm static trong class:
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
Hoặc ta có thể đặc tả hàm bên ngoài:
  class A
    {
        public:
            static void print();
    };

  void A::print()
  {
      cout << "Hello world!\n";
  }

  int main()
  {
      A::print();
  }


