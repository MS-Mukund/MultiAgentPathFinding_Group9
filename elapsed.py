from time import time 
class RunTime():
	def __init__(self):
		self.start = time()
	
	def elapsed(self):
		elapsed_time = time() - self.start
		if( elapsed_time > 300):
			return 1
		return 0