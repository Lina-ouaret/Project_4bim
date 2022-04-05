# Project_4bim

## Table of Contents
1. [General Information](#general-info)
2. [Technologies](#technologies)
3. [Installation](#installation)
4. [Collaboration](#collaboration)
5. [FAQs](#faqs)

## General Information
### Software Description
***
This software creates a synthesized portrait with facial features that resemble as close as possible to a criminal. The creation of the portrait is made based on a witness's successive choices between different propositions taken from a large-scale face attributes dataset. These choices are used by the software to identify the most likely facial characteristics in order to select and propose an image that corresponds to the witness's expectations and hopefully to the actual criminal. 

The software contains a user friendly Graphical User Interface and the algorithms used to propose a final portrait include a Neural Network Algorithm, that will reduce the size of the dataset images and a Genetic Algorithm that will combine and modify the image selected by the witness and propose new image.

### Repository Organization
*** 
The folder portrait_robot contains all the folders that define the software structure. In the folder portrait_robot there are 3 main folders:
Genetic_Algorithm, contains all the python, numpy and csv files needed for the genetic algorithm. 
Neural_Network, contains all the python, and numpy files needed for the neural network algorithm. 
Graphical_Inteface, contains all the the python, numpy, and png files needed for the graphical interface. This folder contains the main python file that defines the software execution. 

The folder tutorials contains two jupyther notebooks that can help you train with the Genetic Algorithm and the Neural Network Algorithm. 

The folder docs contains all the files needed to create the software's documentation. 

### Methodologies Description
Our project is based on 3 main lines  
1) Neural Algorithm : The objective is to reduce and find how to manipulate the encoded data with the annotations which represent the physical traits of faces and create a 'new' database with only the pictures that match the description of the criminal. So we decided to create clusters to reduce the database we noticed that the use of the 3 attributes (Male,Straight Hair,Young) greatly reduced the database. So we made several combinations of our 3 attributes, and  we arrived at the creation of 8 distinct clusters. So we were able to train our neural network on much smaller databases, which makes it possible to have an improvement in the quality of the photos obtained 
2) Genetic Algorithm : The purpose of the genetic algorithm is to reshape the suspect’s image using the various photo choices made by the victim that most closely resembles the suspect. The victim must have the choice of attributes in the genetic algorithm method. The algorithm must take into account the choice of the victim before making the next photo proposal. The mutation method chosen is the crossing over method.
3) GIU : The GIU will display the suspect image based on the victim's choice.     

## Technologies
***
A list of technologies used within the project:
* [python3](https://www.python.org/downloads/): Version 3.7.3
* [Library keras](https://keras.io/about/): Version 2.8.0
* [Library tensorflow](https://www.tensorflow.org/api_docs/python/tf): Version 2.8.0
* [Large-scale CelebFaces Attributes (CelebA) Dataset](http://mmlab.ie.cuhk.edu.hk/projects/CelebA.html)

## Installation
***
To use the application you need a python environnement and you have to verify the versions of python and modules.
In addition to use the followwing instructions you need a linux terminal.  
```
$ git clone https://example.com
$ cd ../path/to/the/file
$ pip3 install keras
$ python3 mainGUI.py
Then follow the intructions of the graphic interface.
```
## Collaboration
***
You can download the project on github but you can't collaborate directly on the project (it is private).

## Tutoriel 
## FAQs
***
A list of frequently asked questions
1. **This is a question in bold**

2. __Second question in bold__

3. **Third question in bold**
.
4. **Fourth question in bold**
| Headline 1 in the tablehead | Headline 2 in the tablehead | Headline 3 in the tablehead |
|:--------------|:-------------:|--------------:|
| text-align left | text-align center | text-align right |
