import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# Page configuration
st.set_page_config(page_title="Excellent University Dashboard", layout="wide")

# Dashboard title
st.title("🏛️ Excellent University Dashboard")
st.markdown("#### Institutional Analytics | 2023 – 2025")
st.markdown("---")

# Load data - Simplified
@st.cache_data
def load_data():
    np.random.seed(42)
    
    # Schools/Faculties at Excellent University
    departments = [
        "School of Business", "School of Engineering", "School of Computing & Informatics", 
        "School of Law", "School of Medicine", "School of Nursing", "School of Education",
        "School of Humanities", "School of Social Sciences", "School of Pharmacy",
        "School of Architecture", "School of Journalism", "School of Agriculture",
        "School of Dentistry", "School of Veterinary Medicine", "School of Public Health",
        "School of Economics", "School of Psychology", "School of Data Science", 
        "School of Environmental Sciences"
    ]
    
    years = [2023, 2024, 2025]
    
    data = []
    
    for year in years:
        growth = 1 + (year - 2023) * 0.15  # 15% growth rate for Excellent University
        
        for dept in departments:
            # Students - Higher enrollment for Excellent University
            if dept in ["School of Business", "School of Computing & Informatics", "School of Data Science"]:
                students = int(2500 * growth * np.random.uniform(0.9, 1.1))
            elif dept in ["School of Medicine", "School of Nursing", "School of Engineering"]:
                students = int(1800 * growth * np.random.uniform(0.9, 1.1))
            elif dept in ["School of Law", "School of Pharmacy"]:
                students = int(1200 * growth * np.random.uniform(0.9, 1.1))
            else:
                students = int(800 * growth * np.random.uniform(0.9, 1.1))
            
            # Completion rate - Higher rates for Excellent University
            if dept in ["School of Medicine", "School of Nursing", "School of Data Science"]:
                completion = np.random.uniform(88, 96) + (year - 2023) * 1.5
            elif dept in ["School of Business", "School of Computing & Informatics", "School of Engineering"]:
                completion = np.random.uniform(85, 93) + (year - 2023) * 2
            else:
                completion = np.random.uniform(80, 90) + (year - 2023) * 2
            
            completion = min(completion, 98)
            
            # Graduates
            graduating = int(students * np.random.uniform(0.24, 0.30))
            
            # Learning mode - More advanced for Excellent University
            if year == 2023:
                mode = np.random.choice(["Physical", "Virtual", "Blended"], p=[0.6, 0.2, 0.2])
            elif year == 2024:
                mode = np.random.choice(["Physical", "Virtual", "Blended"], p=[0.45, 0.3, 0.25])
            else:
                mode = np.random.choice(["Physical", "Virtual", "Blended"], p=[0.3, 0.4, 0.3])
            
            data.append({
                "Year": year,
                "Department": dept,
                "Total_Students": students,
                "Graduating_Students": graduating,
                "Completion_Rate": round(completion, 1),
                "Learning_Mode": mode,
                "Student_Satisfaction": round(np.random.uniform(3.8, 4.9), 1)  # Higher satisfaction
            })
    
    return pd.DataFrame(data)

# Financial data - Higher budget for Excellent University
@st.cache_data
def load_financial_data():
    years = [2023, 2024, 2025]
    
    financial_data = []
    
    for year in years:
        growth = 1 + (year - 2023) * 0.15
        
        tuition = 1200 * growth * np.random.uniform(0.95, 1.05)
        research = 350 * growth * np.random.uniform(0.9, 1.1)
        donations = 180 * growth * np.random.uniform(0.8, 1.2)
        other = 300 * growth * np.random.uniform(0.9, 1.1)
        
        total_revenue = tuition + research + donations + other
        
        salaries = 700 * growth * np.random.uniform(0.95, 1.05)
        infrastructure = 250 * growth * np.random.uniform(0.9, 1.1)
        operations = 350 * growth * np.random.uniform(0.95, 1.05)
        research_funding = 200 * growth * np.random.uniform(0.9, 1.1)
        
        total_expenses = salaries + infrastructure + operations + research_funding
        profit = total_revenue - total_expenses
        
        financial_data.append({
            "Year": year,
            "Tuition_Revenue": round(tuition, 1),
            "Research_Grants": round(research, 1),
            "Donations": round(donations, 1),
            "Other_Income": round(other, 1),
            "Total_Revenue": round(total_revenue, 1),
            "Salaries": round(salaries, 1),
            "Infrastructure": round(infrastructure, 1),
            "Operations": round(operations, 1),
            "Research_Funding": round(research_funding, 1),
            "Total_Expenses": round(total_expenses, 1),
            "Net_Profit": round(profit, 1)
        })
    
    return pd.DataFrame(financial_data)

# Load data
df = load_data()
df_finance = load_financial_data()

# Sidebar Filters
st.sidebar.header("🔍 Filter Dashboard")

years = st.sidebar.multiselect("Select Year(s)", df["Year"].unique(), default=[2023, 2024, 2025])
df_filtered = df[df["Year"].isin(years)]

depts = st.sidebar.multiselect("Select School/Faculty", df["Department"].unique(), default=df["Department"].unique()[:8])
df_filtered = df_filtered[df_filtered["Department"].isin(depts)]

modes = st.sidebar.multiselect("Select Learning Mode", df["Learning_Mode"].unique(), default=df["Learning_Mode"].unique())
df_filtered = df_filtered[df_filtered["Learning_Mode"].isin(modes)]

# Key Metrics
st.header("📊 University Overview")

col1, col2, col3, col4, col5 = st.columns(5)

total_students = df_filtered["Total_Students"].sum()
total_graduates = df_filtered["Graduating_Students"].sum()
avg_completion = df_filtered["Completion_Rate"].mean()
avg_satisfaction = df_filtered["Student_Satisfaction"].mean()
total_revenue = df_finance[df_finance["Year"].isin(years)]["Total_Revenue"].sum()

with col1:
    st.metric("👨‍🎓 Total Students", f"{total_students:,}")
with col2:
    st.metric("🎓 Graduates", f"{total_graduates:,}")
with col3:
    st.metric("📈 Completion Rate", f"{avg_completion:.1f}%")
with col4:
    st.metric("⭐ Satisfaction", f"{avg_satisfaction:.1f}/5.0")
with col5:
    st.metric("💰 Revenue", f"KES {total_revenue:.0f}M")

st.markdown("---")

# Tabs
tab1, tab2, tab3, tab4 = st.tabs(["📚 Academics", "🎓 Students", "💰 Finance", "📊 Insights"])

# TAB 1: Academics
with tab1:
    st.subheader("Completion Rate by School/Faculty")
    
    completion_data = df_filtered.groupby(["Year", "Department"])["Completion_Rate"].mean().reset_index()
    
    fig1 = px.bar(
        completion_data,
        x="Department",
        y="Completion_Rate",
        color="Year",
        title="Completion Rate by School/Faculty (%)",
        barmode="group"
    )
    st.plotly_chart(fig1, use_container_width=True)
    
    st.subheader("Learning Mode Distribution")
    mode_data = df_filtered.groupby(["Year", "Learning_Mode"])["Total_Students"].sum().reset_index()
    
    fig2 = px.bar(
        mode_data,
        x="Year",
        y="Total_Students",
        color="Learning_Mode",
        title="Physical vs Virtual vs Blended Learning",
        barmode="stack"
    )
    st.plotly_chart(fig2, use_container_width=True)
    
    # Research output
    st.subheader("Research Publications by School (2025)")
    research_data = df_filtered[df_filtered["Year"] == 2025].groupby("Department").size().reset_index(name="Publications")
    research_data["Publications"] = research_data["Publications"] * np.random.randint(5, 30, len(research_data))
    research_data = research_data.sort_values("Publications", ascending=False).head(10)
    
    fig_research = px.bar(
        research_data,
        x="Department",
        y="Publications",
        title="Top 10 Schools by Research Publications (2025)",
        color="Publications",
        color_continuous_scale="Viridis"
    )
    st.plotly_chart(fig_research, use_container_width=True)

# TAB 2: Students
with tab2:
    st.subheader("Student Population by School/Faculty")
    
    student_data = df_filtered.groupby(["Year", "Department"])["Total_Students"].sum().reset_index()
    
    fig3 = px.bar(
        student_data,
        x="Department",
        y="Total_Students",
        color="Year",
        title="Student Enrollment by School/Faculty",
        barmode="group"
    )
    st.plotly_chart(fig3, use_container_width=True)
    
    st.subheader("Top 10 Schools by Graduates (2025)")
    grad_data = df_filtered[df_filtered["Year"] == 2025].groupby("Department")["Graduating_Students"].sum().sort_values(ascending=False).head(10).reset_index()
    
    fig4 = px.bar(
        grad_data,
        x="Department",
        y="Graduating_Students",
        title="Schools with Highest Graduates (2025)",
        color="Graduating_Students",
        color_continuous_scale="Blues"
    )
    st.plotly_chart(fig4, use_container_width=True)
    
    st.subheader("Fastest Growing Schools")
    growth_data = df_filtered.groupby(["Year", "Department"])["Total_Students"].sum().reset_index()
    growth_2023 = growth_data[growth_data["Year"] == 2023].set_index("Department")["Total_Students"]
    growth_2025 = growth_data[growth_data["Year"] == 2025].set_index("Department")["Total_Students"]
    
    growth_rate = ((growth_2025 - growth_2023) / growth_2023 * 100).sort_values(ascending=False).head(10).reset_index()
    growth_rate.columns = ["Department", "Growth_Percent"]
    
    fig5 = px.bar(
        growth_rate,
        x="Department",
        y="Growth_Percent",
        title="School Growth Rate (2023-2025)",
        color="Growth_Percent",
        color_continuous_scale="Greens"
    )
    st.plotly_chart(fig5, use_container_width=True)
    
    # International students
    st.subheader("International Student Enrollment")
    international_data = df_filtered.groupby("Year")["Total_Students"].sum().reset_index()
    international_data["International_Students"] = international_data["Total_Students"] * np.random.uniform(0.15, 0.25, len(international_data))
    
    fig_intl = px.line(
        international_data,
        x="Year",
        y="International_Students",
        title="International Student Growth",
        markers=True,
        line_shape="linear"
    )
    st.plotly_chart(fig_intl, use_container_width=True)

# TAB 3: Finance
with tab3:
    st.subheader("Revenue and Expenses Trend")
    
    finance_year = df_finance[df_finance["Year"].isin(years)]
    finance_melt = finance_year.melt(id_vars=["Year"], value_vars=["Total_Revenue", "Total_Expenses", "Net_Profit"], var_name="Category", value_name="Amount")
    
    fig6 = px.line(
        finance_melt,
        x="Year",
        y="Amount",
        color="Category",
        title="Revenue, Expenses & Profit (KES Millions)",
        markers=True
    )
    st.plotly_chart(fig6, use_container_width=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Revenue breakdown (latest year)
        rev_2025 = finance_year[finance_year["Year"] == 2025].iloc[0]
        revenue_data = pd.DataFrame({
            "Source": ["Tuition", "Research Grants", "Donations", "Other Income"],
            "Amount": [rev_2025["Tuition_Revenue"], rev_2025["Research_Grants"], rev_2025["Donations"], rev_2025["Other_Income"]]
        })
        
        fig7 = px.pie(
            revenue_data,
            values="Amount",
            names="Source",
            title=f"Revenue Breakdown (2025)",
            hole=0.3,
            color_discrete_sequence=px.colors.qualitative.Set3
        )
        st.plotly_chart(fig7, use_container_width=True)
    
    with col2:
        # Expense breakdown
        expense_data = pd.DataFrame({
            "Expense": ["Salaries", "Infrastructure", "Operations", "Research Funding"],
            "Amount": [rev_2025["Salaries"], rev_2025["Infrastructure"], rev_2025["Operations"], rev_2025["Research_Funding"]]
        })
        
        fig8 = px.pie(
            expense_data,
            values="Amount",
            names="Expense",
            title=f"Expense Breakdown (2025)",
            hole=0.3,
            color_discrete_sequence=px.colors.qualitative.Set2
        )
        st.plotly_chart(fig8, use_container_width=True)
    
    # Financial metrics
    st.subheader("Financial Health Metrics")
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        profit_margin = (rev_2025["Net_Profit"] / rev_2025["Total_Revenue"]) * 100
        st.metric("Profit Margin", f"{profit_margin:.1f}%", delta="+2.5%")
    
    with col2:
        rev_growth = ((finance_year[finance_year["Year"] == 2025]["Total_Revenue"].values[0] - 
                       finance_year[finance_year["Year"] == 2023]["Total_Revenue"].values[0]) / 
                      finance_year[finance_year["Year"] == 2023]["Total_Revenue"].values[0]) * 100
        st.metric("Revenue Growth (3yr)", f"{rev_growth:.1f}%", delta="+5.2%")
    
    with col3:
        expense_ratio = (rev_2025["Total_Expenses"] / rev_2025["Total_Revenue"]) * 100
        st.metric("Expense Ratio", f"{expense_ratio:.1f}%", delta="-1.8%")
    
    with col4:
        research_investment = (rev_2025["Research_Funding"] / rev_2025["Total_Revenue"]) * 100
        st.metric("R&D Investment", f"{research_investment:.1f}%", delta="+1.2%")
    
    # Year-over-year comparison
    st.subheader("Year-over-Year Financial Comparison")
    finance_comparison = finance_year.set_index("Year").T
    st.dataframe(finance_comparison, use_container_width=True)

# TAB 4: Insights
with tab4:
    st.subheader("Key Institutional Insights")
    
    # Department ranking
    st.markdown("### 🏆 School Performance Ranking (2025)")
    dept_2025 = df_filtered[df_filtered["Year"] == 2025].groupby("Department").agg({
        "Completion_Rate": "mean",
        "Student_Satisfaction": "mean",
        "Total_Students": "sum"
    }).reset_index()
    dept_2025 = dept_2025.sort_values("Completion_Rate", ascending=False)
    dept_2025["Rank"] = range(1, len(dept_2025) + 1)
    
    st.dataframe(dept_2025, use_container_width=True)
    
    # Top performing departments
    st.markdown("### 🎯 Strategic Recommendations for Excellence")
    
    recommendations = [
        "**🚀 Digital Excellence** - Achieve 50% online and blended learning by 2026 through advanced LMS implementation",
        "**🔬 Research Innovation** - Establish 5 new research centers and increase PhD enrollment by 40%",
        "**🌍 Global Partnerships** - Form strategic alliances with top 50 international universities",
        "**💡 Student Success** - Implement AI-driven personalized learning paths to boost completion rates to 95%",
        "**🏗️ Infrastructure Expansion** - Build new innovation hub and modernize all laboratories",
        "**👨‍🏫 Faculty Excellence** - Recruit 50 distinguished professors and provide annual research grants",
        "**💼 Industry Integration** - Launch mandatory internship programs with Fortune 500 companies",
        "**🎓 Alumni Network** - Develop global alumni mentoring platform for career development"
    ]
    
    for rec in recommendations:
        st.info(rec)
    
    # Satisfaction vs Completion scatter
    st.markdown("### 📊 Student Satisfaction vs Completion Rate")
    scatter_data = df_filtered.groupby("Department")[["Completion_Rate", "Student_Satisfaction"]].mean().reset_index()
    
    fig9 = px.scatter(
        scatter_data,
        x="Completion_Rate",
        y="Student_Satisfaction",
        text="Department",
        title="School Performance: Satisfaction vs Completion",
        size="Completion_Rate",
        color="Student_Satisfaction",
        color_continuous_scale="Viridis"
    )
    fig9.update_traces(textposition="top center")
    st.plotly_chart(fig9, use_container_width=True)
    
    # Excellence indicators
    st.markdown("### ⭐ Excellence Indicators")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("🎓 Graduate Employability", "94%", delta="+6%")
        st.metric("📝 Research Publications", "1,247", delta="+23%")
    
    with col2:
        st.metric("🌍 International Students", "22%", delta="+4%")
        st.metric("👨‍🏫 Faculty PhD Holders", "78%", delta="+8%")
    
    with col3:
        st.metric("🤝 Industry Partners", "156", delta="+31%")
        st.metric("🏆 Accredited Programs", "45", delta="+9")

# Data Download
st.markdown("---")
st.subheader("📎 Download Data")

col1, col2 = st.columns(2)
with col1:
    csv = df_filtered.to_csv(index=False).encode("utf-8")
    st.download_button("📊 Download Academic Data as CSV", csv, "excellent_university_academic_data.csv", "text/csv")

with col2:
    csv_finance = df_finance[df_finance["Year"].isin(years)].to_csv(index=False).encode("utf-8")
    st.download_button("💰 Download Financial Data as CSV", csv_finance, "excellent_university_financial_data.csv", "text/csv")

with st.expander("View Raw Academic Data"):
    st.dataframe(df_filtered, use_container_width=True)

with st.expander("View Raw Financial Data"):
    st.dataframe(df_finance[df_finance["Year"].isin(years)], use_container_width=True)

# Footer
st.markdown("---")
st.markdown("### 🎓 Excellent University - Committed to Academic Excellence and Innovation")
st.caption("📌 Excellent University Dashboard | Data Analytics 2023-2025 | Powered by Streamlit")
