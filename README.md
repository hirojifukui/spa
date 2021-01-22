# Sample Schedule App

This web application is for the purpose of teaching and showcasing common web technologies, in addition to the process of creating and deploying a web app. This application is developed in association with [STEAM Dojo](https://steamdojo.org/).  The application uses Vue.JS for the frontend and Flask for the backend. This Github Repository is managed by  [@SebastianVitug](https://github.com/sebastianvitug)



## Install Instructions
#### Main Technologies
-   Install Python from [https://www.python.org/](https://www.python.org/)
-   Install Node.js from [https://nodejs.org/en/download/](https://nodejs.org/en/download/)

Before installing the Flask Packages, we recommend creating a Python3 virtual environment using [venv](https://docs.python.org/3/library/venv.html) or [conda](https://www.anaconda.com/products/individual).
#### Flask Packages
1.  [Flask | 1.1.2](https://flask.palletsprojects.com/en/1.1.x/)
2.  [Flask-MongoEngine| 1.0.0](http://docs.mongoengine.org/projects/flask-mongoengine/en/latest/)
3.  [Flask-Cors | 3.0.9](https://flask-cors.readthedocs.io/en/latest/)

### Install Vue

With Node.js and npm installed uses these steps to install Vue

1. Go to the frontend directory

```
$ cd frontend
```
2. Install vue
```
$ npm install vue
$ npm upgrade
```
3. Install other vue libriaries
```
$ npm install --save vue-js-modal
$ npm install --save vue2-timepicker
```
### Install MongoDB
This application uses a MongoDB
- Can install from [MongoDB](https://www.mongodb.com/try/download/community)
-   Can also install directly from terminal if using MacOS and Homebrew 
### Starting a MongoDB process
    
-   Call `$ mongod` to start a Mongo daemon process with default parameters
    
-   On macOS can also run Mongo as a macOS service using
	-   `$ brew services start mongodb-community@4.4`
	-   `$ brew services stop mongodb-community@4.4`
## Running the Web App
#### Flask Environment
Must first set up the Flask environment before starting the Flask server

1. Go to the flask app directory
	```
	$ cd backend
	```

2. Setup Application Discovery. These instructions are from the [flask documentation](https://flask.palletsprojects.com/en/1.1.x/cli/):

	- Unix Bash:

	```
	$ export FLASK_APP=xpert-signup
	```
	- Windows CMD:
	```
	> set FLASK_APP=xpert-signup
	```
	- Windows PowerShell:
	```
	> $env:FLASK_APP = "xpert-signup"
	```
3. Return to the `\Backend\` directory with `$ cd ..` and use `$ flask run`

### Running Vue.js
1. Go to the frontend folder
```
$ cd frontend
```
2. Make sure npm has installed all the correct packages
```
$ npm install
$ npm upgrade
```
3. Compile and hot-reloads for development
```
$ npm run serve
```