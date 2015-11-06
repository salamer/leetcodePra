class Solution(object):
	def lenthOfLastWord(self,s):
		if len(s)==0:
			return 0
		string=s.split(" ")
		for i in range(len(string)):
			if string[i]==" ":
				string.pop(i)
		last_string=string[-1]
		return len(last_string)
		
