'''
Created on Feb 2, 2017

@author: KTPHUONG
'''
a, b, c , d = eval(input('Nhập a, b, c, d:\n'))
print('a, b, c, d = ', a, b, c, d)
gtln = a
gtnn = a
if gtln < b:
    gtln = b
if gtln < c:
    gtln = c
if gtln < d:
    gtln = d
print('Max =', gtln)
if gtnn > b:
    gtnn = b
if gtnn > c:
    gtnn = c
if gtnn > d:
    gtnn = d
print('Min =', gtnn)