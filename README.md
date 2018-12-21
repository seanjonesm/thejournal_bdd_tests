# thejournal_bdd_tests
Automated test implementation of the basic website functionality of TheJournal.ie

The technology chosen for this technical challenge was python, selenium and a python module called 'behave' to implement Gherkin-style behavioral driven testing. Tests have been successfully run using Firefox but it should also work with Chrome. Test run automation was also implemented using a simple Jenkins pipeline script which checks out, runs the test cases and reports results. For screenshots of this, please see here: https://1drv.ms/w/s!ApNq4fx4xLAhfteQ4ZZA32jGR-k 

In order to run the tests successfully, a python dev environment is required and the selenium and behave modules installed (e.g. using pip) 

**features\basic_tests.feature:** This is the feature file consisting of the the test cases using natural language constructs based on the Gherkin syntax. The required test scenarios are outlined here and the steps for each are defined. 

Scenarios to be tested are: 
- Load The Journal.ie Home Page
- Measure home page load time and ensure that it loads in under 3 seconds
- Load the business section
- Verify that the top three business articles load and author name is populated

**features\steps\step_definitions.py:** This is where the Gherkin test cases are linked with the underlying python code. All the required Given/When/Then scenarios are defined here. Definitions are parameterized where possible which will allow code reuse as the number of test cases grow. e.g. select a parameter driven category from navigation bar, test the top N articles on the page. 

**features\environment.py:** Behave looks for this file during runtime and is used for setting up and tearing down the test environment. Here it's used for defining the web driver object and launching/closing the web browser. 

**framework\app.py:** Consists of the App class to execute the test cases via the selenium web driver. See comments for an explanation of each function. 

**behave.ini:** used to configure behave. Currently used to configure preferred web browser and enable junit reporting

**Jenkinsfile:** source-controlled pipeline script. Simple script to do a git checkout, run a command to execute the feature file test cases and archive the results in junit format



