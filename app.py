import streamlit as st
import pandas as pd

# Set page title and configure the page
st.set_page_config(
    page_title="Name Entry App",
    page_icon="📝",
    layout="centered"
)

# App title and introduction
st.title("Name Entry App")
st.write("Enter a name and click Submit to add it to the list.")

# Initialize session state to store names if it doesn't exist
if 'names' not in st.session_state:
    st.session_state.names = []

# Create a form for name entry
with st.form(key='name_form'):
    # Text input for name
    name_input = st.text_input("Enter a name", key="name_input")
    
    # Submit button
    submit_button = st.form_submit_button(label="Submit")
    
    # Add name to list when submit is clicked
    if submit_button and name_input:
        st.session_state.names.append(name_input)
        st.success(f"Added '{name_input}' to the list!")
        # Clear the input field by forcing a rerun
        st.session_state.name_input = ""
        st.experimental_rerun()

# Display the list of names in a table
if st.session_state.names:
    st.subheader("List of Names")
    
    # Convert the list of names to a DataFrame
    df = pd.DataFrame({"Name": st.session_state.names})
    
    # Display the DataFrame as a table
    st.dataframe(df, use_container_width=True)
    
    # Add a button to clear the list
    if st.button("Clear List"):
        st.session_state.names = []
        st.success("List cleared!")
        st.experimental_rerun()
else:
    st.info("No names have been added yet. Enter a name and click Submit to get started.")