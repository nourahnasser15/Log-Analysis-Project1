# Log-Anlaysis-Project
 First Project for Full Stack Web Developber Course part [FSND](https://sa.udacity.com/course/full-stack-web-developer-nanodegree--nd004)
by Norah Aaljlan

## Idea of the project
 Newspaper site has front end for the website and database in the back end has need to internal reporting tool to answer this question from database 
1-What are the most popular three articles of all time?
2- Who are the most popular article authors of all time?
3-On which days did more than 1% of requests lead to errors?
> Notes :
>1- i put the Outputs for previous question in txt file 
>2-Database contain articles ,authors , log tables 
>**Newsdata** provide by Udacity
 

### Table of content
* installation
* SetUp
* Coding
## Installation
1-we need terminal i using **Git Bash**
2- Editor for python language i using  **Atom**
3- We need same Linux-based so we need to install Virtual Machine (**VM**) this will    give you PostgreSQL database 
4- Then we need to install [**Vagrant**](https://www.vagrantup.com/downloads.html) to share files between linux and windows system.

## SetUp
Enter terminal and excute the following:
* To bring Virtual Machine we need to go to directory /Vagrant then execute this command 
```
vagrant up
```
* Then Log 
```
vagrant ssh
```
To connect to news database and explore data we use this command
```
psql -d news -f newsdata.sql
```
> Before that we need to insatll package for psycopg2 database
```
pip install psycopg2
```

## Coding
I make project in [**Atom**](https://atom.io/) by using Pythong Programming Language 
in addition i connect to  psycopg2 database.
>Note: you can see code in file.

## License
**Free Coding , Hell Yeah**




  

