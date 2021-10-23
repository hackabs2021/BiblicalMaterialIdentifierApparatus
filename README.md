# BiblicalMaterialIdentifierApparatus
Innovative chatbot for bible engagement. Helps to connect those interested in the bible with topics returned from bible APIs. 

<br/><br/>

# How to run
### First download the repository

<br/>

# TEMP
- Add *Install PyCharm*
- Add *Anaconda* libs

### Install *Anaconda*
Download from [anaconda.com](https://www.anaconda.com/products/individual#Downloads) <br/>
(If you are downloading it you will need to create an account) <br/>
(Keep in mind you will need to verify your email as well) <br/>
(It will take a while)

#### For *PyCharm*
Open *PyCharm* then go to the bottom right hand corner were it says something along the lines of "Python *\[version\]* (*\[folder\]*)" <br/>
Click on it and then select "*Add Interpreter...*" <br/>
Select the "*Conda Environment*" tab <br/>
Change "*Python version*" to *3.8* <br/>
And then select "*Make avaliable to all projects*" <br/>
Then click "*ok*"

<br/>

### Make sure you have *python 3.10*
You can check by opening your terminal and running the command
```bash
python --version 
```
If you don't download from [python.org](https://www.python.org/downloads/release/python-3100/)

<br/>

### Make sure you have *virtualenv* installed
If you don't you can install it by running the command below in your terminal
```bash
python -m pip install virtualenv
```

<br/>

### Make sure you have *virtualenvwrapper* installed
If you don't you can install it by running the command below in your terminal
```bash
python -m pip install virtualenvwrapper
```

<br/>

### Navigate to the repository and create the virtual environment
(PATH_TO_REPOSITORY/BiblicalMaterialIdentifierApparatus/) <br/>
(In **Windows** you can navigate in file explorer and then click on the *URI* (The path) and type `cmd` to open a terminal window in the current directory) <br/>
To create the virtual environment run this command in your terminal
```bash
python -m venv website
```

<br/>

### Activate the virtual enviroment
#### Windows
```bash
start website/Scripts/activate.bat
```

#### MacOS & Linux
```bash
source venv/bin/activate
```
