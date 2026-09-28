ACCESS THE DASHBAORD -------> https://it-risk-analysis-sejikm2appytmjdstxaadol.streamlit.app/

 Continuous Control Monitoring (CCM) & IT Risk Assurance


📌 Project Overview
Traditional IT auditing relies heavily on point-in-time sampling, which can leave critical gaps in enterprise risk management. This project simulates an automated **Continuous Control Monitoring (CCM)** system designed to analyze enterprise system logs (ERP, HRMS) in real-time. 

It utilizes a hybrid approach—combining deterministic rule-based logic with unsupervised machine learning—to detect Segregation of Duties (SoD) conflicts, access violations, and hidden transactional anomalies. The backend engine outputs to an interactive executive dashboard, providing an explainable, data-driven view of IT control effectiveness.

## 🚀 Key Features
*   **Synthetic Enterprise Data Engineering:** Generates realistic, time-stamped system logs mimicking human behavior across different corporate departments (Finance, HR, IT).
*   **Rule-Based Policy Engine:** Automatically flags explicit internal control failures, such as:
    *   **Segregation of Duties (SoD) Violations:** E.g., A single user creating an invoice and approving the corresponding payment.
    *   **Access & Time Anomalies:** E.g., IT personnel accessing financial ERPs, or mass data exports occurring at 2:00 AM.
*   **Machine Learning Outlier Detection:** Implements an `IsolationForest` model to identify novel, complex anomalies that fall outside hardcoded corporate policies.
*   **Interactive Assurance Dashboard:** A Streamlit-based web application featuring executive KPIs, interactive Plotly visualizations, and a detailed audit trail for remediation.

## 🛠️ Tech Stack
*   **Data Processing:** Python, Pandas, NumPy
*   **Machine Learning:** Scikit-learn (`IsolationForest`)
*   **Visualization & UI:** Streamlit, Plotly Express

## 💻 Local Installation & Usage

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/yourusername/deloitte-ccm-dashboard.git](https://github.com/yourusername/deloitte-ccm-dashboard.git)
   cd deloitte-ccm-dashboard
