'''
Created on Mar 12, 2017

@author: mayue
'''

headline1 = "abc"
headline2 = "def"
headline3 = "hijk"

print '|%s|%s|%s|' % (headline1.ljust(10), headline2.center(10, "+"), headline3.rjust(10))