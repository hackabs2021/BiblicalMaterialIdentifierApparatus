# BiblicalMaterialIdentifierApparatus
Innovative chatbot for bible engagement. That helps to connect those interested in the bible with topics returned from bible APIs. 

<br/><br/>

# How to run
### First clone or download the repository

<br/>

### Install *Anaconda*
Download from [anaconda.com](https://www.anaconda.com/products/individual#Downloads) <br/>
(You will need to create an account and verify your email as well) <br/>
(It will take a while)

<br/>

### Navigate to the repository and create the anaconda virtual environment
(PATH_TO_REPOSITORY/BiblicalMaterialIdentifierApparatus/) <br/>
To create the virtual environment, run these commands in your terminal
```bash
%userprofile%\anaconda3\Scripts\activate.bat
conda deactivate
conda create --name BMIA
```
It will prompt you to "*Proceed*" type "y" then {enter}<br/><br/>
***TIP:*** In **Windows** you can navigate in file explorer and then click on the *URI* (The path) and type `cmd` and hit {enter} to open a terminal window in the current directory

<br/>

### Install libraries
Run this command in your terminal to install the libraries
```bash
conda env update --name BMIA --file environment.yml
```
It may take a bit of time for the libraries to install

<br/>

### Activate the anaconda virtual environment
Run this command in your terminal
```bash
conda activate BMIA
```

<br/>

### Install final library
Run this command in your anaconda virtual environment
```bash
python -m spacy download en
```
***TIP:*** In **Windows** you can clear the terminal using the command `cls`

<br/>

### Starting the application
Just run this command in your terminal
```bash
python BMIA/app.py
```
[\[Click here\]](http://127.0.0.1:5000/) once the application has started!

<br/><br/><br/>

# Uninstalling
### Delete repository
Just delete it

<br/>

### Remove the anaconda virtual environment
To remove the anaconda virtual environment, run this command in your terminal
```bash
conda env remove --name BMIA
```

<br/>

### Uninstall *anaconda*
Run this command in your terminal and find "*Anaconda3*" and {right-click} and hit "*Uninstall*"
```bash
start appwiz.cpl
```

<br/><br/><br/><br/><br/><br/><br/><br/><br/>

## (DEV Only) For *PyCharm*
Open *PyCharm* then go to the bottom right hand corner were it says something along the lines of "Python *\[version\]* (*\[folder\]*)" <br/>
Click on it and then select "*Add Interpreter...*" <br/>
Select the "*Conda Environment*" tab <br/>
Change "*Python version*" to *3.8* <br/>
Then click "*ok*"
