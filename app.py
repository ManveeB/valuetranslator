import streamlit as st

# 1. The Title
st.set_page_config(page_title="Value Translator", page_icon="💰")
st.title("💰 AI Value Translator")

# 2. The Input
st.write("Translate your business problems into financial ROI.")
user_problem = st.text_area("What is the inefficient process?", placeholder="Example: My sales team spends 2 hours a week manually entering data.")

# 3. The Dummy Logic (We will add AI later)
if st.button("Calculate Savings"):
    if user_problem:
        st.success("Analysis Complete!")
        st.subheader("Projected Savings")
        # This is hard-coded for now just to test the app works
        st.metric(label="Annual Savings", value="$12,400", delta="High Confidence")
        st.write(f"You identified a problem with: **{user_problem}**")
    else:
        st.warning("Please describe a problem first.")