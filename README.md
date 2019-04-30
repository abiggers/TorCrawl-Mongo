# TorCrawl-Mongo
=================
A simple web crawler written in python for collecting research data from the Tor anonymity network, more commonly known as "the dark web". This version of TorCrawl stores collected data in a mongodb database.

Although it is quite possible to drive the Tor Browser using Selenium Webdriver with gekkodriver, this scraping utility does not do so. While the dark web is a fascinating area for data research, as well as an essential component in the global fight to ensure a free and open internet, it is also a very dangerous place. Dynamic rendering of unknown and untrusted data is often dangerous enough on the 'clear net', and that danger is only multiplied on the dark web. Malicious embedded scripts could be activated, and highly illegal content could be unintentionally downloaded. For that reason, this tool has opted to use GET requests that include a header that specifies "Accept": "text/*" to prevent any non-text content from being scraped. This tool is for research purposes only, and is not intended to promote or assist with engaging in any illegal activity. 


In order to use TorCrawl-Mongo, you will need the following:


###Python 3.7
==============
This application uses python 3.7. All required packages and versions are included in the requirements.txt file.


###MongoDB
===========
The default MongoDB connection string URI for localhost is used in the code provided, but if you already have a prefered MongoDB Database setup, just replace mongodb://localhost:27017/ with the URI for your database.

If you have never used MongoDB and are unfamilliar with its installation and setup, the official documentation is available [here](https://docs.mongodb.com/manual/installation/)


###Tor
=====
Before you start TorCrawl, the Tor service must be running and connected. If you are unfamiliar with this process, the Tor Project provides excellent documentation [here](https://2019.www.torproject.org/docs/documentation.html.en)


In order for TorCrawl to work properly, you will need a database called TorCrawl with a collection called onions that contains at least one entry in the following format:

``{ "address": "tor address string goes here", "timeout":timeout integer in seconds, "attempts": 0}``

where address is a string that contains the http address of the onion service you are attempting to scrape, timeout is an integer representing the number of seconds to wait before timing out the connection attempt and moving on, and attempts is an integer representing the number of previous connection attempts that have been made for this entry. Always start with zero, as TorCrawl uses this to determine the order in which to attempt connecting to sites in your database.

If you do not have any starter data, I have included starter file. Simply run ``python seed.py`` from the TorCrawl directory to seed your database with a single entry for the Tor Hidden Wiki in the proper format. That should be enough to get you started.



###Using TorCrawl-Mongo
====
Once you have met all of the setup requirements outlined above, all you have to do is run ``python torcrawl.py`` from the TorCrawl-Mongo directory, and you are off and running. TorCrawl will begin looping through your database, attempting to connect to the address specified in each entry. If a connection is successful, it will begin scraping data from the page and all subdirectories on the site, adding any new onion addresses that it finds as new entries in the onion collection of your database for later scraping. Once it has looped through all subdirectories on the site, it will update the entry for that site in your database with all of the scraped data before moving on to the next entry. Any failure to connect after the specified timeout length will result in TorCrawl updating the entry to reflect an attempt to connect had been made, and incrementing the timeout time by 5. This will do two things: 1) It will push that entry down in priority one level. 2) The next time that TorCrawl attempts to connect with that address, it will wait 5 seconds longer than the previous try before timing out.

