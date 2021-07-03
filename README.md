Infoblox Utility
===========================

Introduction
------------
Utility  which accepts string (varied length) as input, returns any
matched contact(s) from the address book. Address book is a csv file
which can be modified as per need

Prerequisites
-------------
Before using this tool make sure docker is installed on the host.

OS Requirements:
 - Linux (Ubuntu 16.04+, RHEL-7.x+ or CentOS-8.x+)
 - MacOS

Python PIP Requirements:
 No

Features
--------
Common features:
 - Accept string as input and matches eith with first name and last NAME
   from the address book.
 - If any valid match hit the output will be displayed on the console.

Configure Infoblox Utility first time on your setup
===========================================
 - Checkout the Infoblox repository in your local machine. Now goto assignment/pkg
   directory. Now perform following step to build docker image:

    sh-3.2# make
    ...
    ...
    Successfully tagged infoblox-search:latest

 - To check build docker image, run following command:
    sh-3.2# docker image ls | grep infoblox
    infoblox-search                      latest             

 - Command to clean docker image and created directories.
    sh-3.2# make clean


Launching Infoblox Utility
==================
 - Docker run commands can be utilized to test the utility. Add input string
   to be searched in docker args

   sh-3.2# docker run --rm infoblox-search:latest <serach string>

Valid TC
======================================================
sh-3.2# docker run --rm infoblox-search:latest smith
2021-07-03 09:07:20,638 - __main__ - INFO - Fetching contact smith from address book
2021-07-03 09:07:20,638 - __main__ - INFO - Dave,Smith,123 main st.,seattle,wa,43
2021-07-03 09:07:20,638 - __main__ - INFO - Alice,Smith,123 Main St.,Seattle,WA,45
2021-07-03 09:07:20,638 - __main__ - INFO - EvE,Smith,234 2nd Ave.,Tacoma,WA,25
2021-07-03 09:07:20,638 - __main__ - INFO - Ian,smith,123 main st ,Seattle,Wa,18
2021-07-03 09:07:20,639 - __main__ - INFO - Jane,Smith,123 Main St.,Seattle,WA,13

Invalid TC
======================================================
sh-3.2# docker run --rm infoblox-search:latest Demo
2021-07-03 09:08:29,903 - __main__ - INFO - Fetching contact Demo from address book
2021-07-03 09:08:29,904 - __main__ - WARNING - No input found

Invalid TC
======================================================
sh-3.2# docker run --rm infoblox-search:latest 
2021-07-03 09:08:42,009 - __main__ - ERROR - Invalid input
