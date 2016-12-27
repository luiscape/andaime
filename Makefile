#+++++++++++++++++++++++++++++++++++++++++++++++#
#                                               #
#   MAKEFILE                                    #
#   --------                                    #
#                                               #
#   Contains commands for both setting          #
#   up the development environemnt and          #
#   managing the deployment of Docker           #
#   containers.                                 #
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

#
#   DEVELOP
#   -------
#
#   Commands relevant for the development
#   workflow; helps build dependencies,
#   setup the virtual environment, and
#   run tests.
#
test:
	bash bin/test.sh;

setup:
	bash bin/setup.sh;

lint:
	bash bin/run_flake8.sh;
