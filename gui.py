import streamlit as st
import pandas as pd

st.set_page_config(page_title="BI Copilot", page_icon="📊", layout="wide")

st.title("🤖 Autonomous BI Copilot")
st.write("Ask your multi-agent AI team to analyze business challenges or raw CSV data to generate strategic solutions.")

@st.cache_resource
def load_crew():
    from app import bi_crew
    return bi_crew

# 1. File Uploader Widget
uploaded_file = st.file_uploader("Upload a CSV dataset (Optional):", type=["csv"])
csv_context = ""

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write("### Dataset Preview")
    st.dataframe(df.head(5))
    csv_context = f"\n\nAttached CSV Summary:\nColumns: {list(df.columns)}\nRows: {len(df)}\nSample Data:\n{df.head(5).to_string()}"

# 2. Query Input Box
user_query = st.text_area(
    "Enter your business prompt:",
    value="Our SaaS company saw a 15% increase in churn rate among small business customers last quarter.",
    height=100
)

# 3. Execution & Processing
if st.button("Run Multi-Agent Analysis", type="primary"):
    full_prompt = user_query + csv_context
    with st.spinner("Agents are analyzing your request..."):
        try:
            bi_crew = load_crew()
            result = bi_crew.kickoff(inputs={"query": full_prompt})
            
            # Fix HTML tag formatting issues
            clean_result = str(result).replace("<br>", "\n").replace("<br/>", "\n")
            
            st.success("Analysis Complete!")
            st.markdown("---")
            st.markdown("### 📊 Executive Business Report")
            st.markdown(clean_result)

            # 4. Download Report Button
            st.download_button(
                label="📥 Download Executive Report (.md)",
                data=clean_result,
                file_name="executive_report.md",
                mime="text/markdown",
            )
        except Exception as e:
            st.error(f"An error occurred: {e}")
