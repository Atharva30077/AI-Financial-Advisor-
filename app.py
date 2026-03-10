import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from financial_analysis import analyze_finances
from goal_planner import goal_planner
from chatbot import chatbot_response

# Page configuration
st.set_page_config(page_title="AI Financial Advisor", layout="wide")

# Load CSS
with open("styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Title
st.title("💰 AI Financial Advisor Dashboard")
st.markdown("AI-powered financial insights, budgeting guidance, and investment planning.")

# ---------------- SIDEBAR ---------------- #

st.sidebar.header("Enter Financial Details")

income = st.sidebar.number_input("Monthly Income (₹)", min_value=0)
expenses = st.sidebar.number_input("Monthly Expenses (₹)", min_value=0)
savings = st.sidebar.number_input("Total Savings (₹)", min_value=0)
debt = st.sidebar.number_input("Total Debt (₹)", min_value=0)

st.sidebar.subheader("Financial Goal")

goal_name = st.sidebar.text_input("Goal Name (Example: Buy House)")
goal_amount = st.sidebar.number_input("Target Amount (₹)", min_value=0)
goal_years = st.sidebar.number_input("Years to Achieve Goal", min_value=1)

analyze_button = st.sidebar.button("Analyze & Advise")

# ---------------- MAIN DASHBOARD ---------------- #

if analyze_button:

    st.subheader("📊 Financial Overview")

    # Financial Analysis
    result = analyze_finances(income, expenses, savings, debt)

    savings_ratio = result["savings_ratio"] * 100

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Income", f"₹{income}")
    col2.metric("Expenses", f"₹{expenses}")
    col3.metric("Savings", f"₹{savings}")
    col4.metric("Debt", f"₹{debt}")

    st.progress(int(min(savings_ratio, 100)))

    if savings_ratio < 20:
        st.warning("⚠️ Your savings ratio is low. Try reducing unnecessary expenses.")
    else:
        st.success("✅ Great! You have a healthy savings habit.")

    # ---------------- CHART ---------------- #

    st.subheader("📈 Expense Breakdown")

    data = {
        "Category": ["Income", "Expenses", "Savings", "Debt"],
        "Amount": [income, expenses, savings, debt]
    }

    df = pd.DataFrame(data)

    fig, ax = plt.subplots()
    ax.bar(df["Category"], df["Amount"])
    st.pyplot(fig)

    # ---------------- GOAL PLANNER ---------------- #

    if goal_amount > 0:

        st.subheader("🎯 Goal Planning")

        goal = goal_planner(goal_name, goal_amount, goal_years)

        st.write(f"Goal: {goal['goal']}")
        st.write(f"Target Amount: ₹{goal['target_amount']}")
        st.write(f"Time: {goal['years']} years")

        st.success(f"You need to save ₹{goal['monthly_savings_required']:.2f} per month to achieve this goal.")

# ---------------- CHATBOT ---------------- #

st.subheader("🤖 AI Financial Chatbot")

user_query = st.text_input("Ask a financial question")

if st.button("Chat Now"):

    if user_query.strip() == "":
        st.warning("Please enter a question.")
    else:
        response = chatbot_response(user_query)
        st.success(response)

# ---------------- ABOUT TOOL ---------------- #

st.markdown("---")

st.subheader("About This Tool")

st.markdown("""
AI Financial Advisor helps users analyze their financial health and receive intelligent insights.

Features include:

• Financial overview dashboard  
• Expense and savings analysis  
• Goal-based financial planning  
• AI chatbot for financial queries  

Technologies used:

- Python
- Streamlit
- Pandas
- Matplotlib
- Gemini AI (for chatbot integration)
""")
