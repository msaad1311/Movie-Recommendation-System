# Movie Recommendation System

## Table of Content

* [Demo](#Demo)
* [Overview](#Overview)
* [Motivation](#Motivation)
* [Tools Used](#Tools-Used)
* [Installation](#Installation)
* [Bug/Feature Request](##bug---feature-request)
* [Future Work](#Future-Work)
* [Acknowledgment](#Acknowledgment)


## Demo
The app of can be accessed via the following link:

[https://flightfare-prediction.herokuapp.com/](https://flightfare-prediction.herokuapp.com/)

[![](https://imgur.com/Zr0pbY3.png)](https://flightfare-prediction.herokuapp.com/)

## Overview
The app is a Flask based web application that recommends the user movies that are similar to the movie provided by the user. This recommendation is conducted via content based filtering methodology. The application not only caters Hollywood movies, but also take into account the Bollywood movies. 

The application is deployed on AWS and Heroku Platform. Due to storage constraints, only Hollywood movies model is deployed in AWS whereas in Heroku, both Hollywood and Bollywood movies are used.

## Motivation
Today in the era of science and technology, recommendation system plays a vital role in engaging the user to an application. These recommendation engines are so strong in their predictions that they can dynamically alter the state of what the user sees on their page based on the user’s interaction with the app. Hence, it is imperative that recommender system provide the result with greater precision to ensure the maximization of user screen time on the application. 

## Tools Used

[<img target="_blank" src="https://flask.palletsprojects.com/en/1.1.x/_images/flask-logo.png" width=170>](https://flask.palletsprojects.com/en/1.1.x/) 
[<img target="_blank" src="https://number1.co.za/wp-content/uploads/2017/10/gunicorn_logo-300x85.png" width=280>](https://gunicorn.org) 
[<img target="_blank" src="https://scikit-learn.org/stable/_static/scikit-learn-logo-small.png" width=200>](https://scikit-learn.org/stable/) 
[<img target="_blank" src="/Pictures/AWS.png" width=200>](https://scikit-learn.org/stable/) 

## Installation

The code is developed in Python 3.7.9. Whereas, the libraries used can be looked up in the `requirement.txt` file. In order to install the libraries kindly follow the following command after [cloning](https://www.howtogeek.com/451360/how-to-clone-a-github-repository/) the project:

```bash
pip install -r requirements.txt
```

## Bug / Feature Request

If you find a bug, kindly raise an [issue](https://github.com/msaad1311/Movie-Recommendation-System/issues) by including your search query and the expected result and I will try to resolve it. 

## Future Work

* Incorporate different filtering strategies such as collaborative filtering.
* Include more latest data of the movies.
* Include other film industries movies in the dataset.

## Acknowledgment 

* [Muhammad Anas Shahid](https://github.com/Anasshahidd21) for the support in HTML files.
