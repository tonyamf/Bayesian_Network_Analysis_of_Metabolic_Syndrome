# Bayesian Network Analysis of Metabolic Syndrome

This repository contains the code and resources for the research paper "Explorative Approach with Bayesian Networks for Metabolic Syndrome." The project uses Bayesian networks to model the probabilistic relationships between various medical factors associated with metabolic syndrome.

## Table of Contents
- [Project Overview](#project-overview)
- [Dataset](#dataset)
- [Methodology](#methodology)
  - [Bayesian Network Types](#bayesian-network-types)
  - [Structure Learning Algorithms](#structure-learning-algorithms)
- [Code Structure and Usage](#code-structure-and-usage)
- [How to run](#how-to-run)
- [Data provenance and privacy](#data-provenance-and-privacy)
- [Results](#results)
- [Contributing](#contributing)
- [License](#license)

## Project Overview

Metabolic syndrome is a cluster of conditions that occur together, increasing the risk of heart disease, stroke, and type 2 diabetes. This project uses an explorative approach with Bayesian networks to investigate the probabilistic dependencies among these conditions. By modeling these relationships, we can gain a better understanding of the syndrome's underlying mechanisms.

## Dataset

The dataset used in this project is `data.csv`, which contains information on the following variables:
- `DBP`: Diastolic Blood Pressure
- `SBP`: Systolic Blood Pressure
- `FastingBloodSugar`: Fasting Blood Sugar
- `Triglycerides`: Triglyceride levels
- `HDLcholestrol`: High-Density Lipoprotein (HDL) Cholesterol
- `LDLcholestrol`: Low-Density Lipoprotein (LDL) Cholesterol
- `IDFMetsynd`: Diagnostic variable for metabolic syndrome based on International Diabetes Federation criteria.
- `ATPMetssynd`: Diagnostic variable for metabolic syndrome based on ATP III criteria.

## Methodology

### Bayesian Network Types
The project explores three types of Bayesian Networks to model the data:
- **Gaussian Bayesian Networks:** For continuous data.
- **Multinomial Bayesian Networks:** For discrete data.
- **Hybrid Bayesian Networks:** For a mix of continuous and discrete data.

### Structure Learning Algorithms
Three different approaches for learning the network structure are implemented:
- **Score-based:** These algorithms use a scoring function to find the best network structure (e.g., Hill-Climbing).
- **Constraint-based:** These algorithms use conditional independence tests to learn the network structure (e.g., Grow-Shrink).
- **Hybrid:** These algorithms combine elements of both score-based and constraint-based methods (e.g., RSMAX2).

## Code Structure and Usage
The R code is in `main_file.Rmd`; `preprocess.ipynb` (Python) discretises the data. The R notebook includes steps such as:
1.  **Data Loading and Preprocessing:** The `data.csv` file is loaded, and missing values are removed.
2.  **Data Discretization:** Both unsupervised and manual methods are used to discretize the data for multinomial and hybrid models.
3.  **Model Building:** Various Bayesian network models are built using different structure learning algorithms.
4.  **Model Evaluation:** The models are evaluated using scoring functions and k-fold cross-validation.

## How to run
Requirements: R >= 4.3 and the packages `bnlearn`, `deal`, `gRbase`, `gRain`, `gRim`, `ROCR` (plus `rmarkdown`/`knitr` to knit).
```r
install.packages(c("bnlearn", "deal", "gRbase", "gRain", "gRim", "ROCR", "rmarkdown"))
```
Run from the repository root (the CSV paths are relative):
```sh
Rscript -e 'rmarkdown::render("main_file.Rmd")'   # or open main_file.Rmd in RStudio and run chunk by chunk
```
`main_file.Rmd` is an exploratory notebook: it was written as a scratchpad, so some late chunks refer to objects
that are never created in the file (for example `fit`, `dag.deal`). Knitting the whole file in one go is therefore
expected to stop with an error in those chunks; this has not been verified because `bnlearn` could not be installed
in the environment used for the last check.

Python smoke test (no R needed): checks that `dataD.csv` is exactly `data.csv` discretised with the thresholds in `preprocess.ipynb`:
```sh
pip install -r requirements.txt
python scripts/check_discretization.py .
```
`preprocess.ipynb` reads `data.xls`, the original source spreadsheet, which is **not** in this repository, so the notebook cannot be re-run as is.
`data.csv` and `dataD.csv` are its outputs.

## Data provenance and privacy
`data.csv` has 9,971 rows of clinical measurements (blood pressure, glucose, lipids, two syndrome labels) and no names or IDs.
The repository does not say where the data came from or whether it is a public dataset. **Source: unknown. Treat as a possible
privacy problem until the origin and licence are confirmed.**

## Results
No result numbers are stored in this repository (the notebook has no saved outputs). An earlier version of this README
claimed about 91% accuracy for predicting `ATPMetssynd`; nothing in the repository supports that figure, so it was removed.
Re-run the notebook to obtain results.

## Contributing
Contributions to this project are welcome. Please feel free to open an issue or submit a pull request with any improvements or bug fixes.

## License
This project is licensed under the MIT License. (No `LICENSE` file is present in the repository yet.)
