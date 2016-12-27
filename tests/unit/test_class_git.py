"""
Unit tests for the Git() class. 
"""

import os
import shutil

from unittest import TestCase
from andaime.tasks.git import Git


class GitTestCase(TestCase):
    '''
    Unit tests for the Git() class. 
    '''

    def _remove_git_directory(self):
        '''
        Private method for removing a
        .git directory from a target
        test path.
        '''
        file_list = os.listdir('tests/output')
        for file in file_list:
            if file == '.git':
                shutil.rmtree('tests/output/.git')

    def setUp(self):
        '''
        Method that sets-up the test enviroment. 
        '''
        self._remove_git_directory()

    def tearDown(self):
        '''
        Method that clears the test environment.
        '''
        self._remove_git_directory()

    def test_class_inherits_task_correctly(self):
        '''
        Git() inherits Task() correctly, running at initialization.
        '''
        r = Git()
        self.assertTrue(r.status_key == 'success')

    def test_git_directory_is_created(self):
        '''
        Git() creates a `.git` directory successfully. 
        '''
        Git(directory='tests/output')

        files = os.listdir('tests/output')
        self.assertTrue('.git' in files)
