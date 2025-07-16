# BudgetBee

# 💰 BudgetBee – Smart Expense Tracker

**BudgetBee** is a personal finance web app that lets users upload bank statements in CSV format, automatically categorize transactions, and visualize income and spending trends — all in one dashboard.

Built using **Streamlit**, **Pandas**, **Matplotlib**, and **Seaborn**.

---

## 🚀 Live Demo

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://budgetbee.streamlit.app)

Try it live here 👉 **[budgetbee.streamlit.app](https://budgetbee.streamlit.app)**

---



## 🔍 Features

- 📤 Upload your own bank statement (`CSV`)
- 🧠 Auto-categorize transactions based on description
- 💸 Calculate total income, expenses & balance
- 📊 Visualize category-wise spending (Pie, Bar)
- 📅 Track daily expenses over time (Line chart)
- 🐍 100% Python + Streamlit + Data Science tools

---

## 🧪 Sample Data Format

Your uploaded CSV file should have these **three columns**:

| Date       | Description     | Amount |
|------------|-----------------|--------|
| 2025-07-01 | Amazon Purchase | -1200  |
| 2025-07-02 | Salary Credit   | 30000  |
| 2025-07-03 | Zomato Order    | -400   |

- `Date`: in YYYY-MM-DD format  
- `Description`: vendor or transaction name  
- `Amount`: positive for income, negative for expenses

---

## 📁 Project Structure

BudgetBee/
├── data/
│ └── sample_bank_statement.csv # Sample test data
├── notebooks/
│ └── analysis.ipynb # Jupyter analysis (optional)
├── app/
│ └── streamlit_app.py # Web app main file
├── requirements.txt # Required packages for deployment
├── .gitignore
└── README.md


---

## ⚙️ How to Run Locally

1. Clone the repository:

```bash
git clone https://github.com/Muddassir-05/BudgetBee.git
cd BudgetBee

🛠 Tech Stack
Python 3.10+

Pandas – data processing

Matplotlib & Seaborn – visualizations

Streamlit – dashboard app

👨‍💻 Author
Mohd Muddassir Ahmed
📫 GitHub • LinkedIn
💼 B.E. in CSE (Data Science Specialization)
📍 India

⭐️ Show Some Love
If you found this project helpful:

⭐️ Star this repository

🌀 Share with your friends

🛠 Fork it and build your own