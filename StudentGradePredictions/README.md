# Student Grade Predictions

## Overview
This project involves predicting students' final grades in secondary education based on a variety of demographic, social, and academic features using linear regression. The dataset I'll be using contains information on student performance in mathematics collected from portugese schools. 
  
> Data: [Student Performance - UC Irvine](https://archive.ics.uci.edu/dataset/320/student+performance)

## Contents
<details>
<summary>student-mat.csv</summary>
- Ability to generate first names, last names, or full names based on user selection.
- First names can be filtered based on their gender (Option for feminine, masculine, or both).
- To recieve more specific results, users can now choose the first letter on both first and last names.
- Users can specify the number of names to be generated.
- Easy to use prompts guide the user through the name generation process.
- The program reads and processes names from text files and capitalizes them for consistent formatting.
- The application uses the customtkinter library to provide a graphical user interface (GUI), making it user-friendly and accessible.
- Incorporates interactive elements such as radio buttons, dropdown menus, and text input fields to capture user preferences.
</details>

<details>
<summary>GradePrediction.ipynb</summary>

- Step by step Jupyter Notebook that contains detailed information on first name data.
- Includes preliminary exploration of the original dataset.
- Data is prepared so that infrequent names are dropped from the data to prevent skewed results. Unnecessary columns were also dropped along with duplicates so that randomization is not affected by repeated values.
- `cleaned_names.csv` is the new dataset created and imported into the application.
- Visualization of how many female and male names are provided in the dataset with a brief report.
</details>


## Prerequisites
  
**Python:** Make sure you have Python installed on your system or download it here [Official Python Website](https://www.python.org/downloads/).   

**Jupyter Notebook:** Install Jupyter Notebook to run the .ipynb file. You can install it using pip if you don't already have it:

       pip install notebook
       
**Pandas:** Data manipulation and analysis library. Install using:

       pip install pandas

**NumPy:** Library for numerical computations. Install using:

       pip install numpy

**Scikit-Learn:** Machine learning library. Install using:

       pip install scikit-learn

**Plotly:** Interactive graphing library. Install using:

       pip install plotly

## Setup
1. Clone the repository or download the files into your local machine.
2. Navigate to the Project Directory.
3. Launch Jupyter Notebook.



