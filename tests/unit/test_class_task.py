'''
Unit tests for the Task() base class. 
'''

from unittest import TestCase
from andaime.task import Task


class TaskTestCase(TestCase):
	'''
	Test case for the Task() base class.
	'''

	class PseudoTask(Task):
		'''
		Class used for testing the
		properties of Task().
		'''
		def __init__(self, cause_error):
			self.cause_error = cause_error
			super().__init__(name='pseudo-task')

		def _run(self):
			if self.cause_error:
				raise ValueError('Induced error.')
			else:
				return True

	def setUp(self):
		'''
		Method for setting up the test
		case environment. Here we will
		be initializing a test class. 
		'''
		pass

	def test_class_manages_both_success_and_error(self):
		'''
		Task().runner() manages both success and error instances.
		'''
		r = self.PseudoTask(cause_error=True)
		self.assertTrue(r.status_key == 'error')

		r = self.PseudoTask(cause_error=False)
		self.assertTrue(r.status_key == 'success')
