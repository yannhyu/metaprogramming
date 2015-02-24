#two simple generator functions
def countup(n):
	x = 0
	while x < n:
		print('Counting up', x)
		yield
		x += 1

def countdown(n):
	while n > 0:
		print('T-minus', n)
		yield
		n -= 1
	print('Blastoff !!!')


from collections import deque

class TaskScheduler:
	def __init__(self):
		self._task_queue = deque()

	def new_task(self, task):
		'''
		admit a newly started task to the TaskScheduler
		'''
		self._task_queue.append(task)

	def run(self):
		'''
		run until there are no more Tasks 
		'''
		while self._task_queue:
			task = self._task_queue.popleft()
			try:
				# run unitl the next yield statement
				next(task)
				self._task_queue.append(task)
			except StopIteration:
			    # generator is no longer executing
			    pass


# sample use
sched = TaskScheduler()
sched.new_task(countdown(10))    
sched.new_task(countdown(6))
sched.new_task(countup(13))
sched.run()

