class Solution(object):
	def subtractProductAndSum(self, n):

		Product=1
		Sum=0
		while n>0:
			Product=Product*(n%10)
			Sum=Sum+(n%10)
			n=n//10
		return Product-Sum