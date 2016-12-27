'''
Folders task; creates the folder structure
necessary for my Python projects.

'''
import os

from ..task import Task


class Folders(Task):
    '''
    Class for creating a folder structure for
    Python projects.

    '''
    def __init__(self, project_name, path='.'):
        '''
        Method that initializes class.

        Parameters
        ----------
        * project_name (*str*):  

        '''
        self.path = path
        self.directories = [ os.path.join(self.path, d) for 
                             d in ['tests', 'bin', project_name ]]

        super().__init__(name='folders')

    def _create_directories(self):
        '''
        Private method that creates directories
        in the file system.
        '''
        for directory in self.directories:
            if not os.path.exists(directory):
                os.makedirs(directory)

    def _run(self):
        '''
        Private method that gets called by the Task()
        base class when this class is initialized.

        '''
        self._create_directories()
