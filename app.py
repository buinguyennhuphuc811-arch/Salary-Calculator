import streamlit as st
import plotly.express as px

st.set_page_config(
    page_title="Salary Calculator",
    page_icon="💵",
    layout="centered"
)

st.title("💵 Salary Calculator")
st.write("Calculate your monthly take-home salary.")

st.divider()

# ===== INPUT =====

base_salary = st.number_input(
    "Base Salary (VND)",
    min_value=0.0,
    value=10000000.0,
    step=500000.0,
    format="%.0f"
)

bonus = st.number_input(
    "Bonus (VND)",
    min_value=0.0,
    value=1000000.0,
    step=500000.0,
    format="%.0f"
)

allowance = st.number_input(
    "Allowance (VND)",
    min_value=0.0,
    value=500000.0,
    step=500000.0,
    format="%.0f"
)

tax_rate = st.slider(
    "Tax Rate (%)",
    0,
    40,
    10
)

insurance_rate = st.slider(
    "Insurance (%)",
    0,
    15,
    8
)

st.divider()

# ===== CALCULATION =====

gross_salary = base_salary + bonus + allowance

tax = gross_salary * tax_rate / 100

insurance = gross_salary * insurance_rate / 100

net_salary = gross_salary - tax - insurance

# ===== RESULT =====

st.header("📊 Salary Summary")

col1, col2 = st.columns(2)

with col1:
    st.metric(
        "Gross Salary",
        f"{gross_salary:,.0f} VND"
    )

    st.metric(
        "Tax",
        f"{tax:,.0f} VND"
    )

with col2:
    st.metric(
        "Insurance",
        f"{insurance:,.0f} VND"
    )

    st.metric(
        "Take-home Salary",
        f"{net_salary:,.0f} VND"
    )

st.divider()

# ===== PIE CHART =====

labels = [
    "Take-home",
    "Tax",
    "Insurance"
]

values = [
    net_salary,
    tax,
    insurance
]

fig = px.pie(
    names=labels,
    values=values,
    hole=0.45,
    title="Salary Distribution"
)

st.plotly_chart(fig, use_container_width=True)

st.divider()

# ===== FINANCIAL ADVICE =====

st.subheader("💡 Recommendation")

saving_rate = (net_salary / gross_salary) * 100

if saving_rate >= 80:
    st.success("Excellent! Your deductions are low and your take-home salary is high.")

elif saving_rate >= 65:
    st.info("Good! Your salary distribution is healthy.")

else:
    st.warning("Your deductions are relatively high. Review your tax and insurance settings.")

st.caption("Made with ❤️ using Streamlit")
