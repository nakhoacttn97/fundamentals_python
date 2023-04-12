lst_1=[1,2,3,4,5]
lst_2=list(map(lambda i: i**2 , lst_1))
print(lst_2)
#
lst_3=[]
for i in lst_1:
    lst_3.append(i**2)
print(lst_3)    
