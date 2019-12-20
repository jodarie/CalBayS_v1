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


