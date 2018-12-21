# thejournal_bdd_tests
Automated test implementation of some basic functionality of TheJournal.ie

The technology chosen for this technical challenge was python, selenium and a python module called 'behave' to implement Gherkin-style behavioral driven testing. Tests have been successfully run using Firefox but it should also work with Chrome. Test run automation was also implemented using a simple Jenkins pipeline script which checks out, runs the test cases and reports results. For screenshots of this, please see here: https://1drv.ms/w/s!ApNq4fx4xLAhfteQ4ZZA32jGR-k 

In order to run the tests successfully, a python dev environment is required and the __selenium__ and __behave__ modules installed (e.g. using pip) 

**features\basic_tests.feature:** this is the feature file consisting of the test cases using natural language constructs based on the Gherkin syntax. The required test scenarios are outlined here and the steps for each are defined. 

Scenarios to be tested are: 
- Load The Journal.ie home page
- Measure home page load time and ensure that it loads in under 3 seconds
- Load the "Business" section
- Verify that the top three business articles load and author name is populated

**features\steps\step_definitions.py:** here the Gherkin expressions are translated to python code. All the required Given/When/Then scenarios are defined here. Definitions are parameterized where possible which will allow code reuse as the number of test cases grow. e.g. selecting any category from navigation bar, test the top N articles on the page etc.

**features\environment.py:** behave looks for this file during runtime and is used for setting up and tearing down the test environment. Here it's simply used for defining the Firefox driver and launching/closing the web browser. 

**framework\app.py:** consists of the App class which is essentially the underlying python/selenium code to carry out the test steps. Refer to the comments for an explanation of each function. 

**behave.ini:** used to configure behave. Currently this is used to configure the preferred web browser and enable junit reporting

**Jenkinsfile:** source-controlled pipeline script. Simple script to execute the feature file test cases from source control and archive the results in junit format



