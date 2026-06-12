import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("students_cleaned.csv")
dept_kpi = pd.read_csv("department_kpi.csv")

st.title("Student Performance Analytics Dashboard")

# KPI SECTION
st.subheader("Department KPIs")
st.dataframe(dept_kpi)

# FILTER
dept = st.selectbox("Select Department", df["department"].unique())
filtered = df[df["department"] == dept]

# VISUAL 1
st.subheader("Attendance vs Grade")
fig1, ax1 = plt.subplots()
sns.scatterplot(data=filtered, x="attendance_rate", y="final_grade", ax=ax1)
st.pyplot(fig1)

# VISUAL 2
st.subheader("Risk Distribution")
fig2, ax2 = plt.subplots()
sns.countplot(data=filtered, x="risk_category", ax=ax2)
st.pyplot(fig2)

# VISUAL 3
st.subheader("Grade Distribution")
fig3, ax3 = plt.subplots()
sns.histplot(filtered["final_grade"], bins=20, kde=True, ax=ax3)
st.pyplot(fig3)
