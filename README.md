# Flask-Restful

Welcome to my Github portfolio!

Just like many other developers, I certainly like to express myself by showing how I code and refactor modules. In our world, an ability to write clean, testable, and maintainable code is undoubtedly one of the most important fundamentals to possess. Hence, I would like to display one of my projects implemented in Python and flask_restful. It starts with running a web application in localhost. With client's HTTP requests, the web app performs CRUD transactions and returns data if needed.

Please note that this document is written based on Windows.

EDIT [07-03-2017]
Added the API Template Generator in tools/ directory, which will enable us to easily write bulk codes.

EDIT [07-03-2017]
Deployed the application to AWS! Click [here](http://saemi.ap-northeast-2.elasticbeanstalk.com/) if you are interested. <3

## Prerequisites

First of all, it is recommended to install virtualenv which you can easily do so by using pip. This will keep you away from your local dependency.
```
pip install virtualenv
```
Once you have installed, head to the custom folder and create your environment.
```
cd path\to\custom\folder
mkdir myproject
virtualenv myproject
```
Now that you have your fresh and new environment, the only last thing to do is to activate.
```
cd myproject
Scripts\activate
```
For your information, you also can turn off the mode by typing below command.
```
Scripts\deactivate
```


![Pip Install](https://github.com/sungpilpaek/flask_restful/blob/master/img/pip_install.gif)


### Getting Started

In 'myproject' folder, clone this repo.
```
git clone https://github.com/sungpilpaek/flask_restful.git
```


![Git Clone](https://github.com/sungpilpaek/flask_restful/blob/master/img/git_clone.gif)


### Installing

To install, go to the flask_restful folder and run setup.py
```
cd flask_restful
python setup.py install
```


![Setup Py](https://github.com/sungpilpaek/flask_restful/blob/master/img/setup_py.gif)


The only last task remaining is to run our main app.
```
cd src
python app.py
```


![Run App](https://github.com/sungpilpaek/flask_restful/blob/master/img/run_app.gif)


Open up a browser, and type URL.
```
http://localhost:5000
```

Based on AJAX request, the web application performs unique-id-check.

![Input Test](https://github.com/sungpilpaek/flask_restful/blob/master/img/input_test.gif)


Since that I have designed this project as REST API service, we can play with it using built-in Windows PowerShell!

In PowerShell console, declare what username will be attached inside the body.
```
$postParams = @{username='Charmander'}
```
Then, send a POST HTTP request to our local server.
```
Invoke-WebRequest -Uri http://localhost:5000/api/v1/subscription -Method POST -Body $postParams
```
To see if the username was successfully registered, send a GET HTTP request.
```
Invoke-WebRequest -Uri http://localhost:5000/api/v1/subscription -Method GET
```

![Play With PowerShell](https://github.com/sungpilpaek/flask_restful/blob/master/img/play_with_powershell.gif)

## Running the tests

Pytest is used for the testing framework. To run a test suite, type below command in a flask_restful folder.
```
python run_pytest.py
```

## Built With

* [Flask](http://flask.pocoo.org/) - The web framework used
* [Flask Restful](https://flask-restful.readthedocs.io/en/0.3.5/) - The api framework used
* [Pytest](https://docs.pytest.org/en/latest/) - The testing framwork used
* [Pycrypto](https://pypi.python.org/pypi/pycrypto) - Encryption/Decryption library used

## Authors

* **Sung-Pil Paek** - *Initial work* - [GitHub](https://github.com/sungpilpaek)