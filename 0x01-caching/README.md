# 0x01. Caching
## Background Context
In this project, you learn different caching algorithms.


## Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

### General
1. What a caching system is
2. What FIFO means
3. What LIFO means
4. What LRU means
5. What MRU means
6. What LFU means
7. What the purpose of a caching system
8. What limits a caching system have

## Requirements
### Python Scripts
a. All your files will be interpreted/compiled on Ubuntu 18.04 LTS using python3 (version 3.7)
b. All your files should end with a new line
c. The first line of all your files should be exactly #!/usr/bin/env python3
d. A README.md file, at the root of the folder of the project, is mandatory
e. Your code should use the pycodestyle style (version 2.5)
f. All your files must be executable
g. The length of your files will be tested using wc
h. All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
i. All your classes should have a documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
j. All your functions (inside and outside a class) should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')
k. A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)

## More Info
### Parent class BaseCaching
All your classes must inherit from BaseCaching defined below:
	$ cat base_caching.py
	#!/usr/bin/python3
	""" BaseCaching module
	"""

	class BaseCaching():
	    """ BaseCaching defines:
	      - constants of your caching system
	      - where your data are stored (in a dictionary)
	    """
	    MAX_ITEMS = 4

	    def __init__(self):
	        """ Initiliaze
	        """
	        self.cache_data = {}

	    def print_cache(self):
	        """ Print the cache
	        """
	        print("Current cache:")
	        for key in sorted(self.cache_data.keys()):
