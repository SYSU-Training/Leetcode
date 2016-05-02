#326 Power of Three
def divided_by(base, number):
    power=False
    t=1
    while(number>=(base**t)):
        if number%(base**t)==0:
            power=True
        else:
            power=False
        t=t+1
    if number==1:
        power=True
    return power
num=raw_input("number: ")
base=raw_input("base: ")
print divided_by(int(base),int(num))


#without loop and recursive
import math
def isPowerOfThree(self, n):
	return False if n <= 0 else n == pow(3, round(math.log(n, 3)))
'''
http://www.cnblogs.com/cotyb/p/5116442.html
'''
