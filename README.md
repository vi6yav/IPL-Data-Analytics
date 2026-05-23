# IPL Data Analytics Project

## Overview
This project focuses on analyzing Indian Premier League (IPL) match data to uncover insights related to player performance, team success, and match outcomes. The analysis is supported by an interactive dashboard for better visualization and understanding.

## Objectives
- Analyze player performance (batsmen and bowlers)
- Evaluate team performance across seasons
- Understand the impact of toss on match results
- Study scoring patterns across different match phases

## Dataset
The project uses two datasets:
- matches.csv — contains match-level data
- deliveries.csv — contains ball-by-ball data

## Tools and Technologies
- Python  
- Pandas  
- Matplotlib  
- Streamlit  

## Features and Analysis

### Team Performance
Identifies top-performing teams based on match wins.

### Toss Impact
Analyzes whether winning the toss influences match outcomes.

### Top Batsmen
Highlights players with the highest total runs.

### Top Bowlers
Identifies bowlers with the highest number of wickets.

### Match Phase Analysis
Compares scoring patterns across:
- Powerplay (overs 1–6)
- Middle Overs (7–15)
- Death Overs (16–20)

## Interactive Dashboard
An interactive dashboard is built using Streamlit to visualize all key insights in a clean and user-friendly interface.

## How to Run the Project

1. Install required libraries:
pip install pandas matplotlib streamlit

2. Navigate to the project folder:
cd IPL_Project

3. Run the dashboard:
streamlit run app.py

## Project Structure
IPL_Project/
│
├── app.py
├── matches.csv
├── deliveries.csv
├── IPL_Analysis.ipynb
├── README.md
└── Presentation (PPT/PDF)

## Conclusion
The analysis reveals that IPL performance is often dominated by a few key players and teams. While the toss provides a slight advantage, match outcomes are more strongly influenced by performance during different phases of the game, especially the death overs.
