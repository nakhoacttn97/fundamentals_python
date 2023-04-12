# doc mot lan
f = open("bai_tho.txt","r", encoding="utf-8")
noi_dung = f.read()
print(noi_dung)
f.close()

# doc moi lan mot dong
f = open("bai_tho.txt","r", encoding="utf-8")
for d in f.readlines():
    print(d.strip())
f.close()

# ghi them vao bai_tho.txt
f = open("bai_tho.txt","a", encoding="utf-8")
f.write("\nChieu chieu ra ben Van Lau")
f.write("\nAi ngoi ai cau, ai sau ai tham")
f.close();
