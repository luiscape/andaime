### Extending / Adding Tasks
All tasks inherit from the `Task()` base class. In order to extend this program (i.e. adding tasks to the scaffolding process) it is advised to use the following as an example:

```python
class NewTask(Task):
	'''
	Class for accomplishing New Task.
	'''
	def __init__(self):
		'''
		Method that initializes class. 
		Here we use super() for accessing
		the atributes of the Task() base class.
		'''
		super().__init__(name='new-task')

	def _run():
		'''
		Method for running the specific tasks
		that accomplish this job.
		'''
		pass
```

As shown above, you are welcome to write a task in any format. As long as it inherits from the `Task()` base class and has a `_run()` method, it can be run.
