# BiblicalMaterialIdentifierApparatus
Innovative chatbot for bible engagement. That helps to connect those interested in the bible with topics returned from bible APIs. 

<br/><br/>

# How to run
### First download the repository

<br/>

### Install *Anaconda*
Download from [anaconda.com](https://www.anaconda.com/products/individual#Downloads) <br/>
(You will need to create an account) <br/>
(Keep in mind you will need to verify your email as well) <br/>
(It will take a while)

<br/>

### Navigate to the repository and create the anaconda virtual environment
(PATH_TO_REPOSITORY/BiblicalMaterialIdentifierApparatus/) <br/>
To create the virtual environment run this command in your terminal
```bash
conda create --name BMIA --file requirements.txt
```
It may take a bit of time for the libraries to install <br/><br/>
***TIP:*** In **Windows** you can navigate in file explorer and then click on the *URI* (The path) and type `cmd` and hit {enter} to open a terminal window in the current directory

<br/>

### Activate the anaconda virtual environment
Run this command in your terminal
```bash
conda activate BMIA
```

### Starting the application
Just run this command in your terminal
```bash
py app.py
```

<br/><br/><br/><br/><br/><br/><br/><br/><br/>

## (DEV Only) For *PyCharm*
Open *PyCharm* then go to the bottom right hand corner were it says something along the lines of "Python *\[version\]* (*\[folder\]*)" <br/>
Click on it and then select "*Add Interpreter...*" <br/>
Select the "*Conda Environment*" tab <br/>
Change "*Python version*" to *3.8* <br/>
And then select "*Make avaliable to all projects*" <br/>
Then click "*ok*"
