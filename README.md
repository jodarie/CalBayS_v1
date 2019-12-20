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

