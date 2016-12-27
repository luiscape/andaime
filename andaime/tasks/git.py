'''
Git task.

'''
from os import path
from git import Repo
from ..task import Task


class Git(Task):
	'''
	'''
	def __init__(self, directory='.'):
		'''
		Method that initializes class. Here
		we properly call the elements from
		the Task() base class with super().
		
		'''
		self.directory = directory
		super().__init__(name='git')

	def _run(self):
		'''
		Private for running task

		'''
		d = path.join(self.directory,'.git')
		r = Repo.init(d)
