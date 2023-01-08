Khởi tạo con trỏ không mặc định:
  int* p;


Khởi tạo con trỏ mặc định:
  int a = 10;
  int* p = &a;
 

Khởi tạo con trỏ là NULL:
  int* p = NULL;
  hoặc int* p = nullptr;


Kích thước của con trỏ:
  cout << sizeof(int*);                        // 4 (bytes)
  cout << (sizeof(int*) == sizeof(int));       // 1
  
  cout << sizeof(char*);                       // 4 (bytes)
  cout << (sizeof(char*) == sizeof(char));     // 0 vì 4 == 1

  cout << sizeof(float*);                      // 4 (bytes)
  cout << (sizeof(float*) == sizeof(float));   // 1
  
  cout << sizeof(double*);                     // 4 (bytes)
  cout << (sizeof(double*) == sizeof(double)); // 0 vì 4 == 8
  
  Địa chỉ một ô nhớ lưu ở dạng thập lục phân - hexadecimal: 0x61ff0c
  Khi chuyển về dạng nhị phân - binary: 0110 0001 1111 1111 0000 1100 = 24 kí số = 24 bits = 3 bytes
  Tuy nhiên một ô nhớ trong RAM = 32 bits = 4 bytes

Sự tham chiếu của con trỏ tới biến:
  int a = 10;
  int* p = &a;
  *p = 20;
  cout << a;    // 20


Địa chỉ lưu trữ của biến và địa chỉ của con trỏ
  int a = 10;
  cout << &a;     // 0x61ff0c - Địa chỉ của biến a
  int* p = &a;
  cout << p;      // 0x61ff0c - Địa chỉ trỏ tới của con trỏ p
  cout << &p;     // 0x61ff08 - Địa chỉ của con trỏ 


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

