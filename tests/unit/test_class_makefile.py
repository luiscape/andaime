'''
Unit tests for the Makefile() class. 
'''

import os

from unittest import TestCase
from andaime.tasks.makefile import Makefile


class MakefileTestCase(TestCase):
    '''
    Unit tests for the Makefile() class. 
    '''

    def _remove_makefile(self):
        '''
        Private method for removing a
        Makefile from a target test path.
        '''
        file_list = os.listdir('tests/output')
        for file in file_list:
            if file == 'Makefile':
                os.remove('tests/output/Makefile')

    def setUp(self):
        '''
        Method that sets-up the test enviroment. 
        '''
        self._remove_makefile()

    def tearDown(self):
        '''
        Method that clears the test environment.
        '''
        self._remove_makefile()

    def test_makefile_is_created(self):
        '''
        Makefile() creates a `Makefile` file successfully.
        '''
        Makefile(path='tests/output')

        files = os.listdir('tests/output')
        self.assertTrue('Makefile' in files)

    def test_makefile_raises_error_if_file_exists(self):
        '''
        Makefile()._craete_makefile() raises error if file exists.
        '''
        open('tests/output/Makefile', 'w+')

        class f:
            def __init__(self):
                self.path = 'tests/output'
                self.contents = 'foo'

        with self.assertRaises(ValueError):
            Makefile._create_makefile(f())
