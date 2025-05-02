import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Set page title and layout
st.set_page_config(page_title="Streamlit Demo App", layout="wide")

# Title and Header
st.title("Streamlit Demo: Exploring Functions")
st.header("Get Acquainted with Streamlit Features")

# Section 1: Text Display
st.subheader("1. Text Display Functions")
st.write("This is a simple text output using **st.write()**.")
st.markdown("### Markdown Example")
st.markdown("This is *italic*, **bold**, and a [link](https://streamlit.io/).")
st.text("Raw text using st.text() for fixed-width font.")
st.caption("This is a caption for small text.")

# Section 2: Input Widgets
st.subheader("2. Input Widgets")
col1, col2 = st.columns(2)

with col1:
    name = st.text_input("Enter your name:", "Type here...")
    age = st.slider("Select your age:", 0, 100, 25)
    if st.button("Submit"):
        st.success(f"Hello, {name}! You are {age} years old.")

with col2:
    option = st.selectbox("Choose a color:", ["Red", "Blue", "Green"])
    st.write(f"You selected: {option}")
    rating = st.radio("Rate this app:", ["1 Star", "2 Stars", "3 Stars"])
    if rating:
        st.info(f"You rated: {rating}")

# Section 3: Data Display
st.subheader("3. Data Display")
data = pd.DataFrame({
    "Category": ["A", "B", "C", "D"],
    "Values": [10, 20, 15, 25]
})
st.write("Sample DataFrame:")
st.dataframe(data)
st.write("Summary Statistics:")
st.table(data.describe())

# Section 4: Plotting
st.subheader("4. Data Visualization")
chart_type = st.selectbox("Select chart type:", ["Bar", "Line", "Scatter"])

if chart_type == "Bar":
    fig, ax = plt.subplots()
    data.plot(kind="bar", x="Category", y="Values", ax=ax)
    st.pyplot(fig)
elif chart_type == "Line":
    fig, ax = plt.subplots()
    data.plot(kind="line", x="Category", y="Values", ax=ax)
    st.pyplot(fig)
elif chart_type == "Scatter":
    np.random.seed(42)
    scatter_data = pd.DataFrame({
        "X": np.random.rand(50),
        "Y": np.random.rand(50)
    })
    fig, ax = plt.subplots()
    sns.scatterplot(data=scatter_data, x="X", y="Y", ax=ax)
    st.pyplot(fig)

# Section 5: File Upload
st.subheader("5. File Upload")
uploaded_file = st.file_uploader("Upload a CSV file:", type=["csv"])
if uploaded_file:
    df_uploaded = pd.read_csv(uploaded_file)
    st.write("Uploaded Data:")
    st.dataframe(df_uploaded)
    st.write("First 5 rows:")
    st.dataframe(df_uploaded.head())

# Section 6: Sidebar
st.sidebar.header("Sidebar Controls")
theme = st.sidebar.radio("Choose theme:", ["Light", "Dark"])
if theme == "Dark":
    st.sidebar.write("Dark theme selected (customize in config.toml).")
show_code = st.sidebar.checkbox("Show source code")

if show_code:
    st.subheader("6. Source Code")
    with open(__file__, "r") as f:
        st.code(f.read(), language="python")

# Footer
st.markdown("---")
st.write("Built with Streamlit | Explore more at [Streamlit Docs](https://docs.streamlit.io/)")