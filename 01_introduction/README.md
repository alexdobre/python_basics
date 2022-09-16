# Lesson 1 Introduction

Install the PyCharm IDE https://www.jetbrains.com/help/pycharm/installation-guide.html

Install git for windows: https://git-scm.com/download/win
Look for the 64 bit standalone installer. Install with default settings.

Configure the PyCharm terminal to use git bash. To do this go to File -> Settings -> Terminal and under "Shell Path"
navigate to where git is installed. The folder path may look something like: C:\Users\Programming\AppData\Local\Programs\Git\bin\bash.exe

Restart PyCharm and verify the terminal is bash by typing any command in it such as 

```commandline
pwd
```

## Install PIP

Via the terminal run 
```
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
```
Verify PIP installation is successful by 
```commandline
pip --version
```

## Install Flask and run the app

To install falsk: 

```commandline
pip install flask
```

Verify flask installed successfully: 

```commandline
python -c "import flask; print(flask.__version__)"
```

Run the app: 
```commandline
flask --debug --app hello run  
```
The above command will run the hello.py file as a flask app.

See the app running on your local machine by accessing:  http://127.0.0.1:5000

To run a version of the app that uses an HTML template run: 

```commandline
flask --debug --app hello_html run
```
