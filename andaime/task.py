'''
Task base class.

'''

class Task:
	'''
	Base class for all andaime classes.
	This class can be inherited by specific
	task classes and retain all basic functionality.

	'''

	def __init__(self, name):
		'''
		'''
		self.id = name
		self.completed = None

		self.status_key = None
		self.message = None

		self.runner()


	def status(self, key, message=None):
		'''
		Method that sets the status of a task.

		'''
		if key is 'error':
			self.status_key = key
			self.message = message

		elif key is 'success':
			self.status_key = key
			self.message = 'Task (%s) completed successfuly.' % self.id

	def runner(self, verbose=True):
		'''
		Method that runs tasks from target 
		inherited class. 

		Parameters
		----------
		* verbose (*bool*):  Prints the logging information of
		                     a given tasks.

		'''
		def _status_logger(message):
			'''
			Private method for printing status messages. 

			Parameters
			----------
			* message (*str*):  Message to print in logger.

			'''
			print('Task ({task_id}): {message}'.format(task_id=self.id, message=message))


		try:
			self._run()
			self.status(key='success')

			if verbose:
				_status_logger(message='Ran successfully.')

		except Exception as e:
			self.status(key='error', message=e)

			if verbose:
				_status_logger(message=e)
