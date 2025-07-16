import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set the page config
st.set_page_config(page_title="BudgetBee 💰", layout="wide")

st.title("🐝 BudgetBee – Expense Tracker Dashboard")

# Upload CSV
uploaded_file = st.file_uploader("📤 Upload your bank statement (CSV)", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file, parse_dates=['Date'])

    st.success("✅ File uploaded successfully!")

    # Categorize transactions
    def categorize(description):
        description = description.lower()
        if any(keyword in description for keyword in ['salary', 'freelance']):
            return 'Income'
        elif any(keyword in description for keyword in ['zomato', 'starbucks', 'food']):
            return 'Food & Drink'
        elif any(keyword in description for keyword in ['amazon', 'shopping']):
            return 'Shopping'
        elif any(keyword in description for keyword in ['rent']):
            return 'Housing'
        elif any(keyword in description for keyword in ['electricity', 'internet']):
            return 'Utilities'
        elif any(keyword in description for keyword in ['petrol', 'fuel']):
            return 'Transport'
        elif any(keyword in description for keyword in ['movie', 'entertainment']):
            return 'Entertainment'
        else:
            return 'Others'

    df['Category'] = df['Description'].apply(categorize)

    # Show metrics
    total_income = df[df['Amount'] > 0]['Amount'].sum()
    total_expense = df[df['Amount'] < 0]['Amount'].sum()
    balance = total_income + total_expense

    col1, col2, col3 = st.columns(3)
    col1.metric("💸 Total Income", f"₹{total_income:,.2f}")
    col2.metric("🧾 Total Expenses", f"₹{abs(total_expense):,.2f}")
    col3.metric("📊 Balance", f"₹{balance:,.2f}", delta=f"{'▲' if balance > 0 else '▼'}")

    # Pie Chart - Category Distribution
    st.subheader("📊 Expense Distribution by Category")
    expense_data = df[df['Amount'] < 0]
    category_sums = expense_data.groupby('Category')['Amount'].sum().abs()

    fig1, ax1 = plt.subplots()
    ax1.pie(category_sums, labels=category_sums.index, autopct='%1.1f%%', startangle=140)
    ax1.axis('equal')
    st.pyplot(fig1)

    # Bar Chart
    st.subheader("📉 Total Spend by Category")
    fig2, ax2 = plt.subplots(figsize=(10, 5))
    sns.barplot(x=category_sums.index, y=category_sums.values, palette="Set2", ax=ax2)
    st.pyplot(fig2)

    # Line Chart - Daily Spend
    st.subheader("📅 Daily Expenses Over Time")
    daily_expense = expense_data.groupby('Date')['Amount'].sum()
    fig3, ax3 = plt.subplots(figsize=(10, 4))
    ax3.plot(daily_expense.index, daily_expense.values, marker='o', color='crimson')
    ax3.set_xlabel("Date")
    ax3.set_ylabel("Amount Spent (₹)")
    ax3.set_title("Daily Expenses")
    st.pyplot(fig3)

else:
    st.info("👆 Upload a CSV file to get started.")
