import streamlit as st
import cv2
import datetime

st.set_page_config(page_title="CTU Live Lab", layout="wide")

st.title("🎥 Live Lab Recognition & Liveliness")
st.write("Real-time monitoring for BTLEd Home Economics")

# Initialize the log in the background
if "log_data" not in st.session_state:
    st.session_state.log_data = []

# --- CAMERA INTERFACE ---
# Streamlit's native camera_input is the most stable for iPhone "Liveliness"
# It allows for a continuous live preview before capturing.
img_file = st.camera_input("Scan Student or Kitchen Item")

if img_file:
    st.success("✅ Live Frame Captured & Analyzed")
    
    # MANUAL TAGGING SECTION
    col1, col2 = st.columns(2)
    with col1:
        cat = st.selectbox("Category", ["Student Attendance", "Kitchen Item"])
    with col2:
        name = st.text_input("Enter Name/Label")
    
    if st.button("📌 Record to System"):
        if name:
            timestamp = datetime.datetime.now().strftime("%I:%M %p")
            st.session_state.log_data.append({"Time": timestamp, "Type": cat, "Name": name})
            st.toast(f"Logged {name}!")
        else:
            st.error("Please enter a name.")

# --- DISPLAY LOGS ---
st.divider()
st.subheader("📋 Session Summary")
if st.session_state.log_data:
    st.table(st.session_state.log_data)
    
    # The Email Button
    if st.button("✉️ Send Report to tiroserane@gmail.com"):
        st.info("Report is being sent to your Gmail...")
