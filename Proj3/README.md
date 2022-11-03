# CSCE315_Project3 #

## TODO List ##
+ For each App, populate urls.py, views.py, and templates.py 
  + Should function without crashing, and allow simple navigation between pages in the app
+ Implement login functionality 
  + Should be able to go to customer view automatically, and collect needed password for the other view

## Please note ##
+ performQuery is function to access the database and perform queries
+ secrets, and it corresponding .secrets.json will be our method to maintain our credentials and github secureness 

## Virtual Environment ##
+ Before beginning development, be sure to activate the virtual environment 
  + To activate it: `source virt/Scripts/activate` or `source virt/bin/activate` on mac
  + To deactivate, use `deactivate`

## Running the project ##
+ In the Spin_n_Stone directory, can use: `python3 manage.py runserver`
  + This will begin the server on localhost, copy and past link displayed in the browser to see it 

## Apps ##

### login ###
+ This will be used to facilitate the login to all the different apps/views
  + note that customer does not require and credentials 

### manager ###
+ manager view, allows for total control and manipulation, an employee login
  + Will need proper credentials passed from the login 

### customer ###
+ credential-less login, simple UI to order pizza 

### server ###
+ credentialed login, will be somewhat more complicate then customer
  + Will allow the server to make more complicated orders, and some editing not available to the customer 