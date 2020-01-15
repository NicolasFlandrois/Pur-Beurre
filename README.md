# Pur-Beurre
OC - Project 8 - Python 3.7, Django, PostgreSQL, HTML/CSS/JS/Bootstrap

![](https://img.shields.io/badge/Python-%3E%3D3.7-yellow.svg)  ![](https://img.shields.io/badge/Django-2.2.8-brightgreen.svg) ![](https://img.shields.io/badge/local%20database-PostgreSQL-blue.svg)

-----------------------

This project offers a plateform for people in need of a snack, but are looking for something healthy.

A quick search can be done from the main page, and the site offers a list of substitutes in the same category, ordered from the best nutriscore to the worst.

If the user created its account and profile, it can also add a product to its favourites.

----------------------

A specific branch of this project is managed to be deployed on Heroku plateform, and using AWS S3 storage for media contents.

----------------------

In order to ease the database update, a custom command has been created.
This command will automatically update the products, checking and avoiding duplicates.

    python manage.py update_snacks

