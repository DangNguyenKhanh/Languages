# Sử dụng 3 cặp dấu ngoặc kép
s = """Hello
world"""
print(s)
# Hello
# world


# Sử dụng ký tự xuống dòng \n
s = "Hello\nworld\noke"
print(s)
# Hello
# world
# oke


# Một số ký hiệu của ASCII
0  \0  : kí hiệu null                            
7  \a  : Kí hiệu bell (alert)                    
8  \b  : backspace
9  \t  : tab
10 \n  : newline
11 \v  : vertical feed - dữ liệu dọc
12 \f  : form feed
13 \c  : carriage return - vận chuyển trở lại


# Một số ký hiệu không trong ASCII
\<enter>
\\     : ký tự \
\'     : ký tự '
\"     : ký tự "
\N{tên Unicode} : ???
\u<hhhh>    : Unicode hex
\x<hh>      : ASCII hex

  
# Ngắt chuỗi
s = "abc" \
    "efg"
print(s)    # abcefg


  
