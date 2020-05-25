# py_isear_dataset
The International Survey on Emotion Antecedents and Reactions as a python dataset for MachineLearning
http://www.affective-sciences.org/researchmaterial

# Purpose
The purpose of this code repository is to provide a python loader for the Isear Data set
The ISEAR dataset has been developped by the Swiss National Center of Competence in Research.

At first sight, it seems interesting as a text analysis dataset regarding emotions in language. 
Petty dabbler as I am currently, I'll let you be judge of it.

# Basic documentation
## the Isear.csv file
This file is the actual extract of the dataset, which was provided as an Access database.
The data has been cleaned and normalized a bit 

All value lists are including 0 as origin from now on, some results have been been downgraded by 1 to do so. 

There are 3 undocumented (as far as I know) fields, which are Field1 Field2 and Field3 which I kept for practical purposes. 

## Isear fields and values : the enums.py file
Everything you should need to know regarding the labels and values for this dataset should be in the enums.py file

## Usage
```python
from py_isear.isear_loader import IsearLoader
attributes = ['EMOT','SIT']
target = ['TROPHO','TEMPER']
loader = IsearLoader(attributes, target, True)
data = loader.load_isear('path/to/Isear.csv')
data.get_data() # returns attributes
data.get_target() # returns target
data.get_freetext_content() # returns the text content of the database
```
