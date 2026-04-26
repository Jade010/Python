# Restaurant Picker App

## Overview
I love food and I can also be very indecisive about what I want to eat, usually this ends with my partner choosing for me. To solve this, I built a Python app to do it for me. This restaurant randomizer utilizes a samll restaurant dataset that I created in Excel. The app is able to filter by city and cuisine, previews options, and randomly selects a restaurant based on what I'm craving. Built with tkinter, pandas, and ttkbootstrap, with input validation and error handling.

## Features
* Import restaurant data from Excel files (.xlsx, .xls)
* Dynamic filtering by:

  * City
  * Restaurant type (cuisine)
* Interactive table display of filtered results
* Random restaurant selection with animated UI feedback
* Clean, modern interface using ttkbootstrap

## Tech Stack

* Python
* Tkinter (GUI framework)
* ttkbootstrap (modern UI styling)
* Pandas (data processing)

## File Requirements

The imported Excel file must include the following columns:

* Name
* City
* Type

Example:

| Name        | City    | Type     |
| ----------- | ------- | -------- |
| Sushi Place | Seattle | Japanese |
| Taco Spot   | Austin  | Mexican  |

## How to Run

1. Install dependencies:
   pip install pandas ttkbootstrap openpyxl

2. Run the application:
   python RestaurantRandomizer.py

## Project Structure

* RestaurantRandomizer.py → Main application file
* TexasRestaurants.xlsx → Excel file for restaurants in the Dallas-Fort Worth Metroplex
* WashingtonRestaurants.xlsx → Excel file for restaurants in Washington state

## Future Improvements
* Add ratings or ranking system
* Save favorite restaurants
* Add map integration (Google Maps API)

