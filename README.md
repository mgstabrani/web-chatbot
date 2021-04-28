# Tubes 3 Stima
> A simple web-based chatbot (deadline reminder assistant) implemented using string matching (Boyer-Moore and Regular Expression) algorithm.
> 
![tampilan awal](img/Screenshot%20from%202021-04-28%2023-02-37.png)
 
## General Info
This project is one of tasks in IF2211 Strategi Algoritma. The goal of this project is to create a web-based chatbot which can be a task reminder assistant. This project must be implemented using string matching algorithm such as Knuth-Morris-Pratt, Boyer-Moore, and Regular Expression.

## Technologies
* Python 3 (minimum)
* Flask
* Heroku

## Install
- clone this repository
```
git clone https://github.com/farishasim/tubes-3-stima.git
```
- install flask
```
pip install Flask
```

## Run
- Follow this instruction to run in your local web browser.
```
cd src
python -m flask run
```
- You can also see the deployement [here](https://botstimaku.herokuapp.com/)

## Features
- Adding new task.
- Display list of task.
- Display a deadline of certain task.
- Renew particular task.
- Mark a task as done.
- Help option.
- List of key words.
- Error message.
- Word recommendation.

## Author
- [Faris Hasim Syauqi (13519050)](https://github.com/farishasim)
- [Mgs. Tabrani (13519122)](https://github.com/mgstabrani)
- [Muhammad Rizal Muhaimin (13519136)](https://github.com/MrizalMuhaimin)

## Reference
- https://github.com/chamkank/flask-chatterbot
- https://dev.to/lordofdexterity/deploying-flask-app-on-heroku-using-github-50nh
