# **Nordic44-Nordpool**: An Open Data Processing Software Toolset for an Equivalent Nordic Grid Model Matched to Historical Electricity Market Data

This repository gathers the python resources developed to fetch and process the NordPool market data to prepare case file in Modelica, CIM 14, and PSS/E.  
The scripts in this repository have been used to generate case files for every hour of every day of 2015.   
The generated dataset is available at [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.162110.svg)](https://doi.org/10.5281/zenodo.162110)  
The 2015 dataset generation is documented in the paper below, see [Ref00].

## Using this model, data or related software = cite our publications!
We are happy to contribute with this repository, however, if you use any of the data or software provided, we will appreciate if you cite the following publications, as follows:

1. Cite that `the raw and processed data files corresponding to the model are available as an open data set and documented in [Ref00].`
2. Cite that the first appearance of the model, i.e. `the model is first presented in [Ref01]`


- [Ref00] L. Vanfretti, S.H. Olsen, V.S.N. Arava, G. Laera, A. Bidadfar, T. Rabuzin, S.H. Jackobsen, J. Lavenius, M. Baudette, and F.J. Gomez Lopez "An Open Data Repository and a Data Processing Software Toolset of an Equivalent Nordic Grid Model Matched to Historical Electricity Market Data," submitted for publication, Data in Brief, 2016.

- [Ref01] L. Vanfretti, T. Rabuzin, M. Baudette, M. Murad, iTesla Power Systems Library (iPSL): A Modelica library for phasor time-domain simulations, SoftwareX, Available online 18 May 2016, ISSN 2352-7110, http://dx.doi.org/10.1016/j.softx.2016.05.001.

## Acknowledgment

This work was originally developed in the context of the FP7 [iTesla project](http://www.itesla-project.eu/), and further extended within the ITEA3 [openCPS](https://itea3.org/project/opencps.html) project.

## Structure of the repository

The repository is organised as follows:

- nordic44:
 1. *n44.py* contains the Python class responsible for the mapping between Nord Pool data and the Nordic 44 PSS/E base case contained in the folder models
 
 2. *nordpool.py* contains the Python class responsible for reading in Nord Pool market data to a dictionary. It supports to read in from both the ftp server and from excel files.
 
 3. *readraw.py* contains the Python class responsible for reading in a Nordic 44 case from a raw file to Python dictionaries
 
 4. *torecord.py* contains the Python class responsible for writing a Nordic 44 case contained in Python dictionaries to modelica records.
 
 5. *utilities.py* contaings utility functions. Most notibly is the function data_from_nordpool which can download market data from the Nord Pool ftp server and store it to, excel, raw files, and records.

 4. *PSSE_to_CIM14_batch.py* is the Python script used for converting PSS/E files to CIM v14 files
 
 - Examples:


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



## Script documentation
This Section documents the input(s) and output(s) for each of the scripts available here.



----------------------------------------
FIX BELOW
----------------------------------------



### __00_Documentation__:

  1. __N44_changes.docx__ is a file describing the modifications applied to PSS/E Original case for setting up the PSS/E base case

  2. __N44_presentation.pptx__

### __01_PSSE_Resources__:
  1. __Models__ :

    * A folder with PSS/E files of the base case

    * A folder with a 7zip archive containing files of the original N44 system that has been modified to have the PSS/E base case

  2. __Snapshots__ :
    * **N44_2015xxxx** are folders named according to the day they refer to (for example _N44_20150401_ refers to the 1st of April 2015). In each folder there are Excel files (*Consumption_xx.xlsx*, *Exchange_xx.xlsx*, *Production_xx.xlsx*) with data downloaded from , an Excel file (*PSSE\_in\_out.xlsx*) summarizing the results from the Python script *Nordic44.py* in the folder **04_Python_Resources**, PSS/E snapshots for each hour before solving the power flow (*hx\_before\_PF.raw*) and after solving the power flow (*hx\_after\_PF.raw*)

    * *N44_BC.sav* is the PSS/E solved base case that Python script *Nordic44.py* (put the reference)

### __02_CIM14_Snapshots__:
  * **N44_2015xxxx** are folders named according to the day they refer to (e.g. **N44_20150401** refers to the 1st of April 2015). In each folder there are CIM files for each hour (*N44\_hx\_EQ.xml*, *N44\_hx\_SV.xml_, _N44\_hx\_TP.xml*)

  * **N44_noOL_RDFIDMAP.xml** is the file with IDs mapping of those cases (*N44_hx_noOL_EQ.xml*, *N44_hx_noOL_SV.xml*, *N44_hx_noOL_TP.xml*) with fixed overloading problems.

  * **N44_RDFIDMAP_2015-1.xml** and **N44_RDFIDMAP_2015-2.xml**  are the files with IDs mapping of the remaining snapshots from 2015

### __03_Modelica__:

  1. __iTesla_Platform__

    * **[iPSL](https://github.com/tinrabuzin/ipsl)** folder contains the version of the library which can be used to simulate snapshots generated from the iTesla Platform

    * **Modelica_snapshots** Modelica models generated from the snapshots by iTesla Platform

  2. __SmarTSLab__

    * **[OpenIPSL](https://github.com/SmarTS-Lab/OpenIPSL)** folder contains the version of the forked iPSL library which can be used to simulate the manually generated Modelica model of N44 with the record structures corresponding to the snapshots

    * **[Raw2Record](https://github.com/SmarTS-Lab/Raw2Record)** is a Python script which generates the Modelica records from the PSS/E snapshots

    * **Snapshots** folder contains Modelica records automatically generated from the PSS/E records

    * *N44_Base_Case.mo* is the handmade N44 model with the loaded record of the power flow results from the PSS/E base case. It can be used to load other PF results from the folder **03_Modelica/Snapshots**

### __04_Python_Resources__:
