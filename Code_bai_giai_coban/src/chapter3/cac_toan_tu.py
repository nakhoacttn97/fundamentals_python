
# salary = 1200
# cond = salary>=5000 and salary<=7000
# print(cond) # in ra False

# salary = 7000
# cond = salary>=5000 and salary<=7000
# print(cond) # in ra True

# salary = 1200
# cond = 5000<=salary<=7000
# print(cond) # in ra False

# salary = 7000
# cond = 5000<=salary<=7000
# print(cond) # in ra True

# depid = 70
# cond = depid==50 or depid==70 or depid==90
# print(cond) # in ra True

# depid = 70
# cond = depid in [50,70,90]
# print(cond) # in ra True

# tìm nhân viên có lương>=5000 và ở các phòng 50 hoặc 60
salary = 2000
depid = 50
cond = salary>=5000 and depid==60 or depid==50
print(cond) # in ra True

# tìm nhân viên có lương>=5000 và ở các phòng 50 hoặc 60
salary = 2000
depid = 50
cond = salary>=5000 and (depid==60 or depid==50)
print(cond) # in ra False

