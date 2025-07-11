import os
import sys

class ClassLoader():

    def __new__(cls):
        # creates a singleton object, if it is not created, 
        # or else returns the previous singleton object
        if not hasattr(cls, 'instance'):
            cls.instance = super(ClassLoader, cls).__new__(cls)
        return cls.instance

    def __init__(self):
        # determine if application is a script file or frozen exe
        if getattr(sys, 'frozen', False):            
            self._application_path = os.path.join(os.path.dirname(sys.executable), '_internal')
            print('sys.executable: ', self._application_path)
        # Running unpacked
        elif __file__:
            # This assumes that the .py file is running at project root,
            # with resources in a sub-directory. However, as we're using
            # src/ and carrot/ namespace, this would not work.
            # self._application_path = os.path.dirname(__file__)
            self._application_path = os.getcwd()
            print('cwd: ', self._application_path)
        else:
            # When we're not sure, don't prepend any path.
            self._application_path = ''
            print('*: ', self._application_path)

    def get_resource(self, resource_path: str) -> str:        
        abs_path = os.path.join(self._application_path, resource_path)
        return abs_path
