# Flask Restful

Author: Sung-Pil Paek

Welcome to my Github portfolio! Just like many other developers, I certainly like to express myself by showing how I code. In our world, an ability to write clean, testable, and maintainable code is undoubtedly one of the most important fundamentals to possess. Hence, I display one of my projects implemented in Python and flask_restful. It starts with running a web application in localhost. With client's HTTP requests, the web app performs CRUD transactions and returns data if needed.

Finally, please note that this document is written based on Windows.

## Prerequisites

First of all, it is recommended to install virtualenv which you can easily do so by using pip.
```
pip install virtualenv
```
Once you have installed, head to custom folder and create your own environment.
```
cd path\to\custom\folder
mkdir myproject
virtualenv myproject
```
Now that you have your fresh and new environment, the only last thing to do is to activate it.
```
cd myproject
Scripts\activate
```
For your information, you can turn off the mode by typing below command.
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

In order to install, go to the flask_restful folder and run setup.py
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

Open up a browser, and type url.
```
http://localhost:5000
```
![Type Url](https://github.com/sungpilpaek/flask_restful/blob/master/img/type_url.gif)

## Running the tests

Explain how to run the automated tests for this system

### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```

## Built With

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - The web framework used
* [Maven](https://maven.apache.org/) - Dependency Management
* [ROME](https://rometools.github.io/rome/) - Used to generate RSS Feeds

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **Sung-Pil Paek** - *Initial work* - [GitHub](https://github.com/sungpilpaek)