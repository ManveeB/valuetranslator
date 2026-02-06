import streamlit as st
import google.generativeai as genai

# 1. CONFIGURATION
st.set_page_config(page_title="AI Value Translator", page_icon="💰")
st.title("💰 AI Value Translator")
st.subheader("Turn problems into business cases.")

# 2. SETUP API (Securely)
try:
    api_key = st.secrets["GOOGLE_API_KEY"]
    genai.configure(api_key=api_key)
except Exception:
    st.error("⚠️ API Key missing! You need to add it to Streamlit Secrets.")
    st.stop()

# 3. THE USER INTERFACE
problem = st.text_area(
    "Describe the business problem:",
    placeholder="Example: My marketing team spends 10 hours a week resizing images manually."
)

if st.button("Generate Business Case"):
    if not problem:
        st.warning("Please describe a problem first.")
    else:
        with st.spinner("Analyzing industry benchmarks..."):
            try:
                model = genai.GenerativeModel('gemini-1.5-flash')
                prompt = f"""
                You are a Value Engineer. Analyze this complaint: "{problem}"
                
                Output specific markdown sections:
                ### 1. The Core Inefficiency
                (Brief summary)
                
                ### 2. The Math (Assumptions)
                * Role: [Role Name]
                * Avg Rate: $[Rate]/hr (Estimate based on US benchmarks)
                * Time Wasted: [Hours]/week
                
                ### 3. Projected Annual Savings
                # $[Total] / year
                (Calculation: Rate * Hours * 52)
                """
                
                response = model.generate_content(prompt)
                st.markdown("---")
                st.markdown(response.text)
                st.success("Analysis Complete!")

            except Exception as e:
                st.error(f"An error occurred: {e}")
