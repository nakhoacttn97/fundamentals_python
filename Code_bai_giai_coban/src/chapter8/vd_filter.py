lst=[1978,2000,2003,2005,2014,2018]
kq = list(filter(lambda y: (y%4==0 and y%100!=0) or y%400==0
    ,lst))
print(kq)    
