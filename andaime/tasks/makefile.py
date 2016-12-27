'''
Makefile() class for creating a project Makefile.
'''
import io
import os

from ..task import Task


class Makefile(Task):
	'''
	'''
	def __init__(self, path='.'):
		'''
		'''
		self.path = path
		self.contents = '''
#+++++++++++++++++++++++++++++++++++++++++++++++#
#                                               #
#   MAKEFILE                                    #
#   --------                                    #
#                                               #
#   Contains commands for setting up a          #
#   development environment, linting,           #
#   and running test.                           #
#                                               #
#   - test:     runs all tests with nosetests   #
#               and reports coverage.           #
#                                               #
#   - setup:    creates a Python virtual        #
#               environment and installs all    #
#               dependencies. Also creates a    #
#               Docker container with a test    #
#               PostgreSQL database.            #
#                                               #
#   - lint:     runs Python's PEP8 checker.     #
#                                               #
#+++++++++++++++++++++++++++++++++++++++++++++++#


test:
	bash bin/test.sh;

setup:
	bash bin/setup.sh;

lint:
	bash bin/run_flake8.sh;

		'''
		super().__init__(name='makefile')
	
	@staticmethod
	def _create_makefile(self):
		'''
		Private method for creating a Makefile
		with its appropriate contents.
		'''
		d = os.path.join(self.path, 'Makefile')
		if os.path.exists(d):
			raise ValueError('Makefile already exists.')
		else:
			with io.FileIO(d, 'w') as file:
				file.write(self.contents)

	def _run(self):
		'''
		'''
		self._create_makefile(self)
