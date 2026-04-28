# Name Generator App 
***Updated 4/27/2026***

## Overview
This repository contains a Python script, NameGenerator.py, that utilizes the customtkinter library to create a modern application for generating random names. It can generate first names, last names, or both, based on a baby names dataset from Kaggle and the input file last-names.txt. I really enjoy using randomized names for faux data, game characters, and creative writing so I developed this application to make the process easier. I performed some brief and general analysis on the baby names dataset to make some alterations.

## File Structure

<details>
<summary>NameGenerator.py</summary>
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
<summary>NameGeneratorNotebook.ipynb</summary>

- Step by step Jupyter Notebook that contains detailed information on first name data.
- Includes preliminary exploration of the original dataset.
- Data is prepared so that infrequent names are dropped from the data to prevent skewed results. Unnecessary columns were also dropped along with duplicates so that randomization is not affected by repeated values.
- `cleaned_names.csv` is the new dataset created and imported into the application.
- Visualization of how many female and male names are provided in the dataset with a brief report.
</details>

## How to Run
1. Install libraries:

`pip install customtkinter plotly`

2. Run the application:

`python NameGenerator.py`

## Future Updates
Currently, I'm unsatisfied with the data I have for the application. It works for now, but in a future development I would like users to be able to choose what types of names they would like (Fantasy names, Regional names, etc.). I would like to get better results for this as well, so I plan on web scraping for names using Beautiful Soup library in Python. This is currently a hobby project so a specific date for this isn't set.
