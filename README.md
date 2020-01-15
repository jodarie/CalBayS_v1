# CalBayS_v1
### Calorimetry data analysis using Bayesian Statistics

@author Jose David Rivera

## Introduction

Script to perform statistical analysis via Bayesian approach of data obtained from ITC experiments.
CalBayS_v1 allows using more than one curve with different Wiseman C-parameter [DOI:10.1016/0003-2697(89)90213-3](https://www.sciencedirect.com/science/article/pii/0003269789902133?via%3Dihub) in a global fit, in order to compute the affinity and other thermodynamics parameters with high precision.

## Dependencies

CalBayS_v1 was run in Ubuntu 19.10 using the nohup option. The script is python 2.7 compatible and it requires the following packages:

- numpy
- matplotlib  
- scipy
- corner
- emcee
- random

## Configuration Parameters

The parameters should be set in params_all.py file.

#### Parallelization parameter

- run_nohup --> (True/False) Run in background the process, parallel when more than one model is used.

#### Input data   

To run the script the user must create files with each corresponding column to each experiment with different Wiseman C-parameter.

- Conc_protein_data --> Path + file name of protein concetration (&mu;M).
- Conc_ligand_data --> Path + file name of ligand concetration (&mu;M).
- DH_data --> Path + file name of enthalpy/molar.
- Volume_injection_data --> Path + file name of injection volume.
- Volume_cell --> Vector of cell volume (ml).
- Conc_injection --> Vector of injection concentration (&mu;M).

#### Output options 

- color --> Vector of the colors for each curve profile and data scatter figures.
- File_out --> Initial name of out file.

#### MCMC parameters

- Number_of_walkers --> Number of chains.
- Number_of_points --> Number of points in each chain.
- burn_in --> Number of points of burn in.

Note that the run time and reliability of calculation depend on number of chains and  points set here. For more details, the user is suggested to read [emcee documentation](https://emcee.readthedocs.io/en/stable/).  

#### Hill parameters 

- Hill --> (True/False) Set if the Hill model will be used.
- Boundary_conditions_Hill --> Tuple of boundary conditions (minnHill,maxnHill,minKd,maxKd,minDH,maxDH,minq0,maxq0).
- ePrior_Hill --> (True/False) Set Gaussian prior information for &epsilon; parameters, see the section below.
- eP_Hill --> Tuple of center values for &epsilon;.
- deP_Hill --> Tuple of sigma values for &epsilon;.

#### _n_-Independent parameters

- Indp --> (True/False) Set if _n_-independent sites model will be used.
- Boundary_conditions_Indp --> Tuple of boundary conditions (minn,maxn,minK,maxK,minDH,maxDH,minq0,maxq0).
- nPrior_Indp --> (True/False) Set Gaussian prior information for _n_ parameter, see the section below.
- nP_Indp --> Center value for _n_.
- dnP_Indp --> Sigma value for _n_.
- ePrior_Indp --> (True/False) Set Gaussian prior information for &epsilon; parameters, see the section below.
- eP_Indp --> Tuple of center values for &epsilon;.
- deP_Indp --> Tuple of sigma values for &epsilon;.

#### Stepwise parameters

- Stepwise --> (True/False) Set if Stepwise model will be used.
- Boundary_conditions_sw --> Tuple of boundary conditions (minlogK,maxlogK,minDH,maxDH,minq0,maxq0). 
- n_model_sw --> Define the number of Kd in Step-Wise model.
- ePrior_sw --> (True/False) Set Gaussian prior information for &epsilon; parameters, see the section below.
- eP_sw --> Tuple of center values for &epsilon;.
- deP_sw --> Tuple of sigma values for &epsilon;.

#### Stepwise parameters with equal &Delta;H<sub>bind</sub>

- Stepwise_eqDH --> (True/False) Set if stepwise model with equal DH for all binding sites will be used.
- Boundary_conditions_sweqDH --> Tuple of boundary conditions (minlogK,maxlogK,minDH,maxDH,minq0,maxq0). 
- n_model_sweqDH --> Define the number of Kd in Step-Wise model.
- ePrior_sweqDH --> (True/False) Set Gaussian prior information for &epsilon; parameters, see the section below.
- eP_sweqDH --> Tuple of center values for &epsilon;.
- deP_sweqDH --> Tuple of sigma values for &epsilon;.

## Parameters to fit

#### Parameters of interest

- _n_<sub>Hill</sub>: Hill coefficient.
- _K<sup>(i)</sup><sub>d</sub>_: Dissociation constant (_i_ for each event in stepwise model).
- _n_: Stoichiometry value (_n_-independent sites model). 
- &Delta;_H_<sup>(_i_)</sup><sub>bind</sub>: Molar binding enthalpy (_i_ for each event in stepwise model). For stepwise model with equal &Delta;_H_<sub>bind</sub>, the script computes a mean molar binding enthalpy for every binding site.

#### Nuisance parameters 

Here _i_ correponds to each measurement.

- &sigma;<sub>i</sub> : Measurement error.
- [_L_]<sup>(i)</sup><sub>0</sub>: Concentration of ligand in the syringe.
- &epsilon;<sub>i</sub>: Calibration factor of the initial protein concentration in the cell.
- &Delta;_H_<sup>(_i_)</sup><sub>0</sub>: Molar enthalpy offset. 


## Running the code

After download the code and setting the file params_all.py, the user can run it through the following command line:

```
$ python MAIN_RUN.py
```

The code has an example by using 4 titration curves. 


## Attribution

Please cite Cardoso, Rivera et al. (2019) if you find this code useful in your research.
The BibTeX entry for the paper is:

```
@article {Cardoso791178,
	author = {Cardoso, M. V. C. and Rivera, J. D. and Vitale, P. M. and Degenhardt, M. F. S. and Abiko, L.A. and Oliveira, C. L. P. and Salinas, R. K.},
	title = {CALX-CBD1 Ca2+-binding cooperativity studied by NMR spectroscopy and ITC with Bayesian statistics},
	elocation-id = {791178},
	year = {2019},
	doi = {10.1101/791178},
	publisher = {Cold Spring Harbor Laboratory},
	URL = {https://www.biorxiv.org/content/early/2019/10/03/791178},
	eprint = {https://www.biorxiv.org/content/early/2019/10/03/791178.full.pdf},
	journal = {bioRxiv}
}
```


