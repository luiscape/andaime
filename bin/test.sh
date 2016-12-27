#!/bin/bash

run_unit_tests() {
  nosetests --with-xunit \
            --xunit-file=$CIRCLE_TEST_REPORTS/django/test-results.xml \
            --rednose \
            --with-coverage \
            --no-byte-compile \
            --nologcapture \
            --cover-inclusive \
            --with-id \
            --cover-min-percentage=90 \
            --cover-html \
            --cover-html-dir=$CIRCLE_TEST_REPORTS/coverage/ \
            -v
}

run_cli_tests() {
  echo '-----------------------------'
  echo 'Running CLI functional tests.'
  echo '-----------------------------'
}

#
#  Run tests with coverage.
#  Checks if program is on CircleCI,
#  for outputing JUnit XML test results
#  in the "artifacts" folder.
#
if [[ $CIRCLECI ]]
  then
    echo '--------------------------'
    echo 'Running tests on CircleCI.'
    echo '--------------------------'
    if run_unit_tests
      then

        if run_cli_tests
          then
            echo '--------------------------'
            echo 'Done'
            echo '--------------------------'
          else
            exit 1
          fi

      else
        echo '--------------------------'
        echo 'Failed'
        echo '--------------------------'

        exit 1
      fi

  else

    echo '------------------------------------'
    echo 'Running tests on local environment.'
    echo '------------------------------------'

    source venv/bin/activate
    nosetests --rednose \
            --with-coverage \
            --no-byte-compile \
            --nologcapture \
            --with-id \
            --cover-inclusive \
            --cover-min-percentage=90 \
            --cover-html \
            -v
fi