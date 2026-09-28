import streamlit as st
import pandas as pd
import plotly.express as px
import os

# Page Configuration
st.set_page_config(page_title="CCM Assurance Dashboard", layout="wide")
st.title("🛡️ Continuous Control Monitoring (CCM) Dashboard")
st.markdown("Automated IT Risk & Segregation of Duties (SoD) Assurance")

# Load Data - with error handling for deployment
@st.cache_data
def load_data():
    file_path = "audited_system_logs.csv"
    if not os.path.exists(file_path):
        st.error(f"Data file '{file_path}' not found. Please ensure it is uploaded to your GitHub repository.")
        st.stop()
        
    df = pd.read_csv(file_path)
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    return df

df = load_data()

# Sidebar for Executive Filtering
st.sidebar.header("Audit Filters")
selected_dept = st.sidebar.multiselect(
    "Filter by Department", 
    options=df['department'].unique(), 
    default=df['department'].unique()
)

filtered_df = df[df['department'].isin(selected_dept)]
risk_df = filtered_df[filtered_df['engine_flag'] != 'Clear']

# Calculate KPIs
total_events = len(filtered_df)
flagged_events = len(risk_df)
failure_rate = (flagged_events / total_events) * 100 if total_events else 0

# Top KPI Layout
col1, col2, col3 = st.columns(3)
col1.metric("Total System Events Analyzed", f"{total_events:,}")
col2.metric("Control Failures Detected", f"{flagged_events:,}", delta_color="inverse")
col3.metric("Control Failure Rate", f"{failure_rate:.2f}%", delta_color="inverse")

st.markdown("---")

# Visualizations
col_chart1, col_chart2 = st.columns(2)

with col_chart1:
    st.subheader("Risk Distribution by Control Type")
    if not risk_df.empty:
        fig_pie = px.pie(
            risk_df, 
            names='engine_flag', 
            hole=0.4, 
            color_discrete_sequence=px.colors.sequential.RdBu
        )
        st.plotly_chart(fig_pie, use_container_width=True)
    else:
        st.info("No risks detected for the selected criteria.")

with col_chart2:
    st.subheader("Control Failures by Department")
    if not risk_df.empty:
        fig_bar = px.bar(
            risk_df, 
            x='department', 
            color='engine_flag', 
            barmode='group',
            color_discrete_sequence=px.colors.qualitative.Set1
        )
        st.plotly_chart(fig_bar, use_container_width=True)
    else:
        st.info("No risks detected for the selected criteria.")

st.markdown("---")

# Explainable AI / Audit Trail Data Table
st.subheader("Detailed Audit Trail: High-Risk Events")
st.markdown("This table isolates the specific system logs that triggered the deterministic rules or machine learning anomaly thresholds, providing actionable evidence for remediation.")

st.dataframe(
    risk_df[['timestamp', 'user_id', 'department', 'action_type', 'system_module', 'amount', 'engine_flag']]
    .sort_values(by='timestamp', ascending=False),
    use_container_width=True,
    hide_index=True
)
