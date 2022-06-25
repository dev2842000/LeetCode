class Solution(object):
	def fib(self, n):

    pre=0
    postpre=1
    result=0
    if n==0 or n==1:
        return n
    for i in range(1,n):
        result=pre+postpre
        pre=postpre
        postpre=result
    return result