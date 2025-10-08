import streamlit as st  

# Basic text elements
st.title("My First Streamlit App")  # Adds a big title at the top of the app
st.header("Section 1")  # Adds a section header — good for breaking content into parts
st.subheader("Header")  # Slightly smaller than header — useful for structure
st.subheader("Subheader")  # Another level down — keeps things organized
st.text("Simple text")  # Displays plain, unformatted text — like a basic message
st.markdown("**Bold** and *italic* text")  # Markdown lets you add simple formatting like bold and italics

# Display data
st.write("Automatic data display")  # Streamlit's flexible method — handles strings, numbers, dataframes, and more
st.code("print('Hello World')", language='python')  # Nicely formats code blocks with syntax highlighting
st.latex(r"\int_{a}^{b} x^2 dx")  # Renders LaTeX math formulas — great for equations


# Exercise 2: Data Input Components
st.title("My second Streamlit App")
st.header("Section 2")
name = st.text_input("Enter your name", "John Doe")
description = st.text_area("Description", "Write something...")

age = st.number_input("Age", min_value=0, max_value=120, value=25)
score = st.slider("Score", 0, 100, 50)

option = st.selectbox("Choose an option", ["A", "B", "C"])
options = st.multiselect("Multiple options", ["X", "Y", "Z"])

date = st.date_input("Select date")
time = st.time_input("Select time")

if st.button("Click me"):
    st.write("Button clicked!")

if st.checkbox("Show/Hide"):
    st.write("Visible content")
    
    
    ## Exercise 3: Layout and Containers
    
    st.header("Section 3")

# Create two side-by-side columns
col1, col2 = st.columns(2)

with col1:  # Everything under this goes into the left column
    st.header("Column 1")
    st.write("Content for column 1")

with col2:  # Everything under this goes into the right column
    st.header("Column 2")
    st.write("Content for column 2")

# Expandable sections
with st.expander("Click to expand"):
    st.write("Expanded content here")

# Sidebar
st.sidebar.title("Sidebar")
sidebar_option = st.sidebar.selectbox("Select option", ["A", "B", "C"])