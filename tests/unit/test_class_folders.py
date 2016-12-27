'''
Unit tests for the Folders() class. 
'''

import os
import shutil

from unittest import TestCase
from andaime.tasks.folders import Folders


class FoldersTestCase(TestCase):
    '''
    Unit tests for the Folders() class. 
    '''

    def _remove_folders(self):
        '''
        Private method for removing directories
        created by the test case.
        '''
        file_list = os.listdir('tests/output')
        for file in file_list:
            if file in self.directories:
                shutil.rmtree(os.path.join('tests/output', file))

    def setUp(self):
        '''
        Method that sets-up the test enviroment. 
        '''
        self.directories = ['tests', 'bin', 'test_project']
        self._remove_folders()

    def tearDown(self):
        '''
        Method that clears the test environment.
        '''
        self._remove_folders()

    def test_directories_are_created(self):
        '''
        Folders() creates correct directories.
        '''
        Folders(path='tests/output', project_name='test_project')

        files = os.listdir('tests/output')
        print(files)
        for d in self.directories:
            print(d)
            self.assertTrue(d in files)
