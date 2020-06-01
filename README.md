# Instructions
**Overview** 

This repository provides data and code to analyze correlations between brain size, FSIQ and, and reaction time. Code is provided in myanalysis.py, data is provided under the practical/ directory, and relevant details are described in myanalysis.pdf.

**Installation**

The provided python code was interpreted under a virtual environment called 'bhsenv.' The package specifics are described in the appended requirements.txt file.

**Running**

Simply create the virtual environment on your machine as per the header in requirements.txt, navigate to your clone of this repository, then type: 

> conda activate bhsenv

> python myanalysis.py

**Outputs**

The code will output Spearman's correlation coefficient for brain size, FSIQ, and reaction time directly to the python console. A figure showing the correlation between FSIQ and reaction time will also be produced.
