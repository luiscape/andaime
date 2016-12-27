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
