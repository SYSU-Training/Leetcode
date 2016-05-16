#Reverse Vowels of a String
class Solution(object):
	def reverseVowels(self,s):
		Vowels=['a','e','i','o','u']
		s_list=list(s)
		size=len(s_list)
		left,right=0,size-1
		while True:
			while left<size and s_list[left].lower() not in Vowels:
				left +=1
			while right>=0 and s_list[right].lower() not in Vowels:
				right -=1
			if left >= right:
				break
			s_list[left],s_list[right]=s_list[right],s_list[left]
			left,right=left+1,right-1
		return "".join(s_list)

'''
1.双指针问题
2. list转str  "".join(list)
3. str.lower()
'''

#精简版
def reverseVowels(self, s):
    vowels = re.findall('(?i)[aeiou]', s)
    return re.sub('(?i)[aeiou]', lambda m: vowels.pop(), s)
