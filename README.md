# **Nordic44-Nordpool**: An Open Data Processing Software Toolset for an Equivalent Nordic Grid Model Matched to Historical Electricity Market Data

This repository gathers the python resources developed to fetch and process the NordPool market data to prepare case file in Modelica, CIM 14, and PSS/E.  
The scripts in this repository have been used to generate case files for every hour of every day of 2015 and 2016.   
The generated datasets are available at:
- 2015 data [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.162907.svg)](https://doi.org/10.5281/zenodo.162907)
- 2016 data [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.162921.svg)](https://doi.org/10.5281/zenodo.162921)

The dataset generation is documented in the paper below, see [Ref00].

## Using this model, data or related software = cite our publications!
We are happy to contribute with this repository, however, if you use any of the data or software provided, we will appreciate if you cite the following publications, as follows:

1. Cite that `the raw and processed data files corresponding to the model are available as an open data set and documented in [Ref00].`
2. Cite that the first appearance of the model, i.e. `the model is first presented in [Ref01]`


- [Ref00] L. Vanfretti, S.H. Olsen, V.S.N. Arava, G. Laera, A. Bidadfar, T. Rabuzin, S.H. Jackobsen, J. Lavenius, M. Baudette, and F.J. Gomez Lopez "An Open Data Repository and a Data Processing Software Toolset of an Equivalent Nordic Grid Model Matched to Historical Electricity Market Data," submitted for publication, Data in Brief, 2016. Download the pre-print of the submitted paper from this [link](https://github.com/SmarTS-Lab/Nordic44-Nordpool/releases/download/v1.0.0/DIB.Article.preprint.pdf)

- [Ref01] L. Vanfretti, T. Rabuzin, M. Baudette, M. Murad, iTesla Power Systems Library (iPSL): A Modelica library for phasor time-domain simulations, SoftwareX, Available online 18 May 2016, ISSN 2352-7110, http://dx.doi.org/10.1016/j.softx.2016.05.001.

## Acknowledgment

This work was originally developed in the context of the FP7 [iTesla project](http://www.itesla-project.eu/), and further extended within the ITEA3 [openCPS](https://itea3.org/project/opencps.html) project.

## Installation of the repository

The content of the repository can be installed using the following commands:

 clone the repository:
  > git clone git@github.com:SmarTS-Lab/Nordic44-Nordpool.git

 install the scripts:
  >python setup.py install

## Structure of the repository

The repository is organised as follows:

- nordic44:
 1. *n44.py* contains the Python class responsible for the mapping between Nord Pool data and the Nordic 44 PSS/E base case contained in the folder models

 2. *nordpool.py* contains the Python class responsible for reading in Nord Pool market data to a dictionary. It supports to read in from both the ftp server and from excel files.

 3. *readraw.py* contains the Python class responsible for reading in a Nordic 44 case from a raw file to Python dictionaries

 4. *torecord.py* contains the Python class responsible for writing a Nordic 44 case contained in Python dictionaries to modelica records.

 5. *utilities.py* contains utility functions. Most notibly is the function data_from_nordpool which can download market data from the Nord Pool ftp server and store it to, excel, raw files, and records.

 4. *PSSE_to_CIM14_batch.py* is the Python script used for converting PSS/E files to CIM v14 files

- examples:
 1. *data_set_from_excel.py*  example demonstrating how excel files can be read into Python and used to create raw PSS/E cases from the market data.

 2. *data_set_from_excel.py* example demonstrating how one can download market data from the Nord Pool ftp server and construct PSSE/cases.

 3. *multiple_data_sets_from_nordpool.py* example demonstrating how the utility function *data_from_nordpool* can be used to download multiple data sets from the ftp server and stored to both raw files and modelica records.

- bin:
 1. *nordic44_script.py* Wrapper for the command line. When installing the repository "using python setup.py install" this script should be put in a folder for executables allowing one to construct datasets directly from the command line without invoking the Python interpreter.



## External Resources
The scripts available in this repository are used in an ecosystem build by several software component developed / used at SmarTS Lab.
The goal is to generate case files with the powerflow solution matching the data available from the electricity market dispatch.   

- Market data:  
The source data for building the case files is obtained directly from [Nord Pool](http://www.nordpoolspot.com/Market-data1/Power-system-data/Production1/Production1/ALL1/Hourly1/?view=table).
- CIM profiles:
 - The generation of CIM profile requires [PSS ODMS](http://w3.siemens.com/smartgrid/global/en/products-systems-solutions/software-solutions/planning-data-management-software/model-data-management/pages/pss-odms.aspx) (additional license required)
 - CIM profiles can be used in any CIM-compliant software
- Modelica:  
The script generates data record containing the power flow solution to be used in combination with the SmarTS Lab Nordic44 model.
 - Running Modelica models requires a Modelica-compliant IDE (such as [OpenModelica](https://openmodelica.org/), [Dymola](http://www.modelon.com/products/dymola/))
 - The OpenIPSL and Nordic44 model are available in the [OpenIPSL repository](https://github.com/SmarTS-Lab/OpenIPSL)
- PSS/E case files:  
Running the simulation for the generated files requires [PSS/E](http://w3.siemens.com/smartgrid/global/en/products-systems-solutions/software-solutions/planning-data-management-software/planning-simulation/Pages/PSS-E.aspx) (additional license required).

## Copyright Statement
Nordic44-Nordpool: A toolbox to extract powerflow data from Nordpool and prepare it for the SmarTS Lab N44 model.

Copyright (C) 2016 The authors:
- Luigi Vanfretti,
- Svein H Olsen,
- V. S. Narasimham Arava,
- Giuseppe Laera,
- Ali Bidadfar,
- Tin Rabuzin
- Sigurd H Jakobsen,
- Jan Lavenius,
- Maxime Baudette,
- Francisco J. Gómez López

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
