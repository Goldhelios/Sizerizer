import json
import streamlit as st
from streamlit_option_menu import option_menu
from functions  import *
import jsonification
import datetime
import requests

# Page Configuration
st.set_page_config(layout="centered",page_title="Sizerizer",page_icon=":straight_ruler:")

# Title of the Application
st.write("###")
st.title("WMT Sizerizer")
st.write("Welcome to the Sizerizer, a tool to help inform resource allocation, staffing decisions, and project management strategies for your client request.")

# Navigation Menu
with st.container():

    # Display the navigation menu using the option_menu widget
    selected = option_menu(
        menu_title=None,
        options=['Sizerizer', 'Taxonomy', 'FAQ'],
        icons=['robot', 'book', 'star'],
        orientation='horizontal'
    )


# FAQ Page
if selected == 'FAQ':
    with st.container():
        st.title("FAQ")
        # add a text box for the user to input the YouTube link
      

# Taxonomy Page
if selected == "Taxonomy":
    with st.container():

        # Display the summary text
        st.markdown("# Taxonomy on Walmart")

        # Read the content of the summary.txt file
        with open("sum.txt", "r") as f:
            summary_text = f.read()
        st.write(summary_text)
        with open("sum.txt", "w") as f:
            f.write("")
        st.write("")


#Sizerizer Page
if selected == "Sizerizer":

    col1, col2 = st.columns(2)

    with col1:


        #Size Analysis
        st.write("#")
        st.header(":blue[Size Analysis]", divider="blue")

        # Read the size_questions.json file
        with open('size_questions.json', 'r') as file:
            questions_data = json.load(file)

        size_points = [get_user_input(q["question"], q["input_type"], q["answers"], key=f"size-{i}") for i, q in enumerate(questions_data)]

        if size_points:
            total_size_points = sum(size_points)
            average_size_points = total_size_points / len(size_points)

            # Calculate size using both methods
            size1 = size_method_range(average_size_points)
            size2 = size_method_avg(average_size_points)

        # Display the results

        col3, col4 = st.columns(2)
        if size1 == size2 and size1 != "":
            with col3:
                st.image(Giphy_Size_Selector(size1), use_column_width=True)
            with col4:
                st.write("##")
                st.write(f"{size1}")
        elif size1 != "" and size2 != "":
            with col3:
                st.image(Giphy_Size_Selector("or"), use_column_width=True)
            with col4:
                st.write("##")
                st.write(f"{size1} or {size2}")

        else:
            st.write("")
 

    with col2:

        # Complexity Analysis
        st.write("#")
        st.header(":green[Complexity Analysis]", divider="green")

        # Read the complexity_questions.json file
        with open('complexity_questions.json', 'r') as file:
            complexity_questions_data = json.load(file)

        responses = []

        s = 0
        complexity_answer1 = display_complexity_question(complexity_questions_data[s]["question"],complexity_questions_data[s]["input_type"], complexity_questions_data[s]["answers"],False)
        s = s+ 1
        complexity_answer2 = display_complexity_question(complexity_questions_data[s]["question"],complexity_questions_data[s]["input_type"], complexity_questions_data[s]["answers"],False)
        s = s+ 1
        complexity_answer3 = display_complexity_question(complexity_questions_data[s]["question"],complexity_questions_data[s]["input_type"], complexity_questions_data[s]["answers"],False)
        s = s+ 1
        if complexity_answer2 == "No, not a new concept":
            x = False
        else: 
            x = True
        complexity_answer4 = display_complexity_question(complexity_questions_data[s]["question"],complexity_questions_data[s]["input_type"], complexity_questions_data[s]["answers"],x)
        s = s+ 1
        complexity_answer5 = display_complexity_question(complexity_questions_data[s]["question"],complexity_questions_data[s]["input_type"], complexity_questions_data[s]["answers"],x)
        s = s+ 1
        if complexity_answer5 == "Existing Design (No New Design)":
            z = False
        else: 
            z = True
        complexity_answer6 = display_complexity_question(complexity_questions_data[s]["question"],complexity_questions_data[s]["input_type"], complexity_questions_data[s]["answers"],z)
        s = s+ 1
        complexity_answer7 = display_complexity_question(complexity_questions_data[s]["question"],complexity_questions_data[s]["input_type"], complexity_questions_data[s]["answers"],x)
        s = s+ 1
        complexity_answer8 = display_complexity_question(complexity_questions_data[s]["question"],complexity_questions_data[s]["input_type"], complexity_questions_data[s]["answers"],z)
        s = s+ 1
        complexity_answer9 = []
        complexity_answer9 = display_complexity_question(complexity_questions_data[s]["question"],complexity_questions_data[s]["input_type"], complexity_questions_data[s]["answers"],False)
        s = s+ 1
        if "Supplier (Merchant)" in complexity_answer9:
            q = False
        else: 
            q = True
        complexity_answer10 = display_complexity_question(complexity_questions_data[s]["question"],complexity_questions_data[s]["input_type"], complexity_questions_data[s]["answers"],q)
        s = s+ 1
        complexity_answer11 = display_complexity_question(complexity_questions_data[s]["question"],complexity_questions_data[s]["input_type"], complexity_questions_data[s]["answers"],q)
        s = s+ 1
        complexity_answer12 = display_complexity_question(complexity_questions_data[s]["question"],complexity_questions_data[s]["input_type"], complexity_questions_data[s]["answers"],False)
        s = s+ 1
        if "Onsite (Walmart)" in complexity_answer12:
            w = False
        else: 
            w = True
        if "Offsite (Other Location)" in complexity_answer12:
            o = False
        else: 
            o = True
        complexity_answer13 = display_complexity_question(complexity_questions_data[s]["question"],complexity_questions_data[s]["input_type"], complexity_questions_data[s]["answers"],w)
        s = s+ 1
        complexity_answer13 = display_complexity_question(complexity_questions_data[s]["question"],complexity_questions_data[s]["input_type"], complexity_questions_data[s]["answers"],o)
        s = s+ 1
        complexity_answer13 = display_complexity_question(complexity_questions_data[s]["question"],complexity_questions_data[s]["input_type"], complexity_questions_data[s]["answers"],o)
        s = s+ 1
        complexity_answer13 = display_complexity_question(complexity_questions_data[s]["question"],complexity_questions_data[s]["input_type"], complexity_questions_data[s]["answers"],False)
       

    #Log Final Group Decision

    st.write("#")
    st.title("Prepare Outcome Transmission")
    st.write('Once complete, please fill out the below and press log to store this information')

    Project_Name = st.text_input("Project Name")
    Group_Decision_Complexity = st.selectbox('Final Agreed Upon Comlexity', ["Simple","Standard","Complex"], index = None)
    Group_Decision_Size = st.selectbox('Final Agreed Upon Size', ["Small","Medium","Large","Extra Large"], index = None)
    Group_Decision_Comments = st.text_input("Comments")
    Submission_date = datetime.datetime.now()

    # Initialize session state for button click
    if "button_clicked" not in st.session_state:
        st.session_state.button_clicked = False

    # Function to handle button click
    def on_button_click():
        st.session_state.button_clicked = True

    # Button to trigger the success message
    st.button("Transmit Results", on_click=on_button_click, type="primary")

    # Conditionally display the success message
    if st.session_state.button_clicked:
        st.success('This project has been sizerized and stored.', icon="✅")

    #Prepare Selection & Decision Data For Transmit

    #Transmit Data Via Smartsheet API

