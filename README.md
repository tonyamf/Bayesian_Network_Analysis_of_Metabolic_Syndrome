# Bayesian Network Analysis of Metabolic Syndrome

This repository contains the code and resources for the research paper "Explorative Approach with Bayesian Networks for Metabolic Syndrome." The project uses Bayesian networks to model the probabilistic relationships between various medical factors associated with metabolic syndrome.

## Table of Contents
- [Project Overview](#project-overview)
- [Dataset](#dataset)
- [Methodology](#methodology)
  - [Bayesian Network Types](#bayesian-network-types)
  - [Structure Learning Algorithms](#structure-learning-algorithms)
- [Code Structure and Usage](#code-structure-and-usage)
- [Setup and Installation](#setup-and-installation)
- [Corrections and Improvements](#corrections-and-improvements)
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
The R code for this project is in the `main_file.Rmd` file. It includes the following steps:
1.  **Data Loading and Preprocessing:** The `data.csv` file is loaded, and missing values are removed.
2.  **Data Discretization:** Both unsupervised and manual methods are used to discretize the data for multinomial and hybrid models.
3.  **Model Building:** Various Bayesian network models are built using different structure learning algorithms.
4.  **Model Evaluation:** The models are evaluated using scoring functions and k-fold cross-validation.

## Setup and Installation
To run the R code, you need to have R and RStudio installed. You will also need to install the following packages:
```r
install.packages(c("bnlearn", "deal", "gRain", "gRbase", "gRim"))
```
You will also need to have the `data.csv` file in the same directory as the R Markdown file.

## Corrections and Improvements

The following improvements have been made to the original R code:
1.  **File Paths:** The original code used hardcoded file paths. The corrected version assumes the data file is in the same directory as the script.
2.  **Code Clarity:** Added comments to the code to explain the different steps and methodologies.
3.  **Code Organization:** Removed unused code and organized the script to be more readable and maintainable.

## Results
The analysis suggests that the hybrid-based learning structure for a Gaussian Bayesian Network, when fitted with manually discretized data, provides the most accurate and interpretable model of the relationships between the factors contributing to metabolic syndrome. The model achieves an accuracy of approximately 91% in predicting the `ATPMetssynd` diagnostic variable.

## Contributing
Contributions to this project are welcome. Please feel free to open an issue or submit a pull request with any improvements or bug fixes.

## License
This project is licensed under the MIT License. See the `LICENSE` file for more details.
