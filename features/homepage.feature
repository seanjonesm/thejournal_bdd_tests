Feature: Genesis Automation Challenge QA - TheJournal.ie

Scenario: Load Home Page
When the user navigates to url "https://www.thejournal.ie"
Then the "home" page loads successfully

Scenario: Measure Home Page Load Time
Given the web browser is currently open
When the user navigates to url "https://www.thejournal.ie"
Then the "home" page loads successfully
And the page load time is under "3000" milliseconds

Scenario: Load Business Section
Given the url "https://www.thejournal.ie" is currently open
When the user selects "Business" from the navigation bar
Then the "business" page loads successfully

Scenario Outline: Verify that articlea load and author name is populated on all
Given the url "https://www.thejournal.ie/business" is currently open
When the user selects article "<article_num>"
Then the "article" page loads successfully
And the author name is populated
Examples:
|article_num    |
|1              |
|2              |
|3              |







