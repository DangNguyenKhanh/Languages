Khởi tạo con trỏ không mặc định:
  int* p;


Khởi tạo con trỏ mặc định:
  int a = 10;
  int* p = &a;
 

Khởi tạo con trỏ là NULL;
  int* p = NULL;
  hoặc int* p = nullptr;


Sự tham chiếu của con trỏ tới biến:
  int a = 10;
  int* p = &a;
  *p = 20;
  cout << a;    // 20


Khởi tạo hằng con trỏ:
-> không được thay đổi giá trị (constant value) nhưng được trỏ tới vùng khác
  int a = 10, b = 20;
  const int* p;   // Không cần khởi tạo mặc định, có cũng được
  p = &a;         // *p = 10  OKE
  p = &b;         // *p = 20  OKE
  *p = 30;        // ERROR 
  

Khởi tạo con trỏ hằng:
-> Không được trỏ tới vùng khác (constant address) nhưng được thay đổi giá trị
  int a = 10, b = 20;
  int* const p = &a;    // Phải khởi tạo mặc định
  p = &b;               // ERROR
  *p = 30;              // a = 30   OKE


Khởi tạo hằng con trỏ hằng:
-> Không được trỏ vùng khác và không được thay đổi giá trị
  int a = 10, b = 20;
  const int* const p = &a;
  p = &b;               // ERROR
  *p = 30;              // ERROR

