# Flask-MongoDB-API
<br>

## This project is having the following endpoints:

* **/api/plan/create - To create a new plan**
* **/api/plan/list_all - To retrieve all plans**
* **/api/plan/$plan_id/update - To update a particular plan**
* **/api/$user_id/plan - To retrieve a plan associated with a user**
* **/api/$user_id/plan/feature/limit - To return the limits for each feature**

## Setup for project:

* **virtualenv venv - To create a virtual environment so that it does not disturb the other projects**
* **source venv/bin/activate - To activate the virtual environment**
* **pip install flask - To install flask**
* **pip install Flask-PyMongo - To install pymongo. It is a python distribution containing tools for working with MongoDB, and is the recommended way to work with MongoDB from python.**
* Now install [Postman](https://www.getpostman.com/downloads/). It is a Google Chrome app for interacting with HTTP APIs. It presents you with a friendly GUI for constructing requests and reading responses.
* Now install [MongoDB Compass](https://www.mongodb.com/download-center/compass?jmp=docs). It is a simple-to-use, sophisticated GUI that allows any user within your organization to visualize and explore your data with ad-hoc queries in just a few clicks – all with zero knowledge of the MongoDB query language.
* * **Open MongoDB Compass and create a database and collection of your own choice and connect it with the server. In the main.py file I have "telecom" as my database and "plan" is the collection name.**

## Running the project:

* **Now open terminal and wrire python filename.py to run the python file.**
* Now you will see something like this: * Serving Flask app "__name__" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 964-909-305
* **Now open postman and start writing a particular endpoint with a specific method like - GET,POST,PUT etc.**
* **Following these steps you can use this API!!**
