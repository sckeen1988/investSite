# Investing Site

This creates a basic website and sqlite database allowing users to create accounts, log in, and finally connect to the database to eventually view live data for stock prices

## Description

I used flask to create and run an application that is broken into three parts:
1) models.py defines/creates an sqlite database where all information will be stored, and later retrieved for client viewing
2) views.py defines all the webpages that are not associated with the sqlite database are viewable by anyone with or without an account
3) auth.py Handles all cases where authorization is required, including logging in/out, creating an account, viewing account information

The Templates folder
The base.html file defines the base structure that all other pages will inherit from. Here I also import over some bootstrap templates for styling the page.
Each remaining template is the html base code for each page of the site.

## Getting Started

### Dependencies

Python 3 is required to run. 

All other dependencies can be installed via:
```
  pip install -r requirements.txt
```


### Executing program

To start the server, open the kis_site folder in the CLI and run

```
$ python main.py
```

Next you can either click the url link directly from the CLI or

Open your browser of choice and paste the folowing url
```
http://127.0.0.1:5000/
```

## Future goals

1) Allow users to 'sell' shares of the company
2) Do not require users to enter an interger into each submit form on myAccounts page
3) Add Admin page in order to see all users and delete users as needed
4) Migrate the sqlite database to postgres
5) Create a connection to TDAmeritrade's api and retrieve prices for SPY, display this value on the myAccount page.


## Version History

* 0.1
    * Initial Release
* 0.2
    * Added functionality to update database


## Acknowledgments

Inspiration, code snippets, etc.
* tech with tim youtube channel
