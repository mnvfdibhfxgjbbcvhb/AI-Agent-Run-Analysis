# AI Agent Run Analysis

## Project Overview
This project analyzes AI agent execution logs using MySQL, Python, Pandas, Matplotlib, and Seaborn.

## Objectives
- Analyze AI agent execution status and success rates.
- Compare LLM model costs and latency.
- Analyze prompt and completion token usage.
- Evaluate agent performance using human evaluation scores.
- Identify trends in AI execution activity.

## Tools and Technologies
- MySQL
- Python
- Pandas
- Matplotlib
- Seaborn

## SQL Analysis
The project includes 30 SQL queries covering basic SQL, aggregations, joins, subqueries, CTEs, and window functions.

## Visualizations
1. AI runs by status
2. Top AI agents by run count
3. Total cost by LLM model
4. Average latency by model
5. Prompt tokens vs. completion tokens
6. Average human evaluation score by agent
7. Run status distribution
8. Latency distribution
9. Run cost vs. latency
10. AI runs over time

## How to Run
1. Install the dependencies using `pip install -r requirements.txt`.
2. Configure your local MySQL connection.
3. Run `ai_agent_visualizations.py`.

*Note: Configure your own database credentials and load the required tables before running the analysis.*