# First

import streamlit as st
import json
import requests
import time
import re
from datetime import datetime
from User import UserData
import matplotlib.pyplot as plt

# with st.sidebar:
#     openai_api_key = st.text_input("OpenAI API Key", key="chatbot_api_key", type="password")
#     "[Get an OpenAI API key](https://platform.openai.com/account/api-keys)"
#     "[View the source code](https://github.com/streamlit/llm-examples/blob/main/Chatbot.py)"
#     "[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/streamlit/llm-examples?quickstart=1)"

def data_reports():
    labels = ["Harassment", "Discrimination", "Abuse", "Bullying", "Stalking", "Other"]
    sizes = [10, 30, 30, 10,10,10]
    # Create a pie chart
    fig, ax = plt.subplots()
    ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
    ax.axis('equal')

    # Display the pie chart in Streamlit
    st.pyplot(fig)


def validate_northeastern_email(email):
    # Use a regular expression to check if the input is a valid email ending with @northeastern.edu
    pattern = r'^\S+@northeastern\.edu$'
    return re.match(pattern, email) is not None

def validate_password(password):
    return len(password) >= 8

def register():
    st.title("Register")
    with st.form("register_form"):
        register = {}
        full_name = st.text_input("Full Name")
        email = st.text_input("Email ID")
        password = st.text_input("Password", type="password")
        # Every form must have a submit button.
        submitted = st.form_submit_button("Register")
        if submitted and (not email or not full_name or not password or not validate_password(password) or not validate_northeastern_email(email)):
            # api call
            alert = st.warning("Enter the details correctly.")
            time.sleep(2)
            alert.empty()
            # Navigate
        elif submitted:
            print(full_name, email, password)
            user = f"""{{
                    "fullname": "{full_name}",
                    "email": "{email}",
                    "password": "{password}"
                    }}"""
            user_data = {"full_name": full_name, "email":email, "password":password}
            # json_data = json.dumps(user_data)
            print(user_data)
            # api call
            response = requests.post(url="http://127.0.0.1:8000/api/register", data=user, headers={'Content-Type': 'application/json'})
            st.success(response)

            # Navigate

def login():
    st.title("Login")
    with st.form("login_form"):
        login = {}
        email = st.text_input("Email ID")
        password = st.text_input("Password", type="password")
        # Every form must have a submit button.
        submitted = st.form_submit_button("Login")
        if submitted and (not email or not password or not validate_password(password) or not validate_northeastern_email(email)):
            # api call
            alert = st.warning("Enter the details correctly.")
            time.sleep(2)
            alert.empty()
        elif submitted:
            print(email, password)
            user = f"""{{
                    "fullname": "",
                    "email": "{email}",
                    "password": "{password}"
                    }}"""

            # api call
            response = requests.post(url="http://127.0.0.1:8000/api/login", data=user, headers={'Content-Type': 'application/json'})
            if response.status_code == 200:
                response = response.json()
                print(response)
                res = str(response)
                if res in "User does not exist":
                    st.error("Login not successful")
                else:
                    arr = res.split()
                    fullname = arr[-1]
                    st.session_state['user'] = fullname
                    st.session_state['email'] = email
                    print(st.session_state)
                    st.success(res)
            else:
                st.error("Login not successful")


def chatbot():
    st.title("💬 The Husky Assistant") 
    if "messages" not in st.session_state:
        st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?"}]

    for msg in st.session_state.messages:
        st.chat_message(msg["role"]).write(msg["content"])

    if prompt := st.chat_input():
        print(prompt)
        st.session_state.messages.append({"role": "user", "content": prompt})
        st.chat_message("user").write(prompt)
        response = requests.get(url="http://127.0.0.1:8000/api/ask/"+prompt)
        # print(response.content)
        msg = response.text
        print(msg)
        msg = msg.replace('\\n\\n', '\\n')
        msg = msg.replace('\\n', '<br>')
        print(msg)
        st.session_state.messages.append({"role": "assistant", "content": msg})
        st.chat_message("assistant").write(msg, unsafe_allow_html=True)

def validate_phone_number(phone_number):
    return re.match(r'^\d{10}$', phone_number) is not None

def validate_date(date_text):
    try:
        datetime.strptime(date_text, '%Y-%m-%d')  # Adjust the format as needed
        return True
    except ValueError:
        return False

def social_issue_report_form():
    st.title("Social Issue Report Form")
    with st.form("report_form"):
        report = {'fullname': '',
                'email' : '',
                'phone' : '',
                'college_name'
                'issue_type' : '',
                'location' : '',
                'date' : '',
                'description' : '',
                'witnesses' : '',
                'actions_taken' : '',
                'additional_comments' : ''
        }

        user = st.session_state['user']
        email = st.session_state['email']
        fullname = st.text_input("Name", user, disabled=True)
        email = st.text_input("Email", email, disabled=True)
        phone = st.text_input("Phone Number (optional)")
        college_name = st.selectbox("College *", ["Choose an Option","College of Engineering", "Khoury College of Sciences", "School of Law", "D'Amore-McKim School of Business ", "College of Professional Studies", "Other (Specify)"])

        # affiliation = st.radio("Affiliation", ["Student", "Faculty", "Staff", "Other (Specify)"])

        issue_type = st.selectbox("Type of Issue *", ["Choose an Option","Harassment", "Discrimination", "Abuse", "Bullying", "Stalking", "Other (Specify)"])

        location = st.selectbox("Location *", ["Choose an Option","Smith Hall", "Stetson East", "East Village", "West Village G", "Hastings Hall", "Other (Specify)"])

        date = st.text_input("Date of Incident in the format of 'YYYY-MM-DD'(Optional)")

        description = st.text_area("Description of Incident *")

        witnesses = st.text_area("Witness Information (if applicable)")

        actions_taken = st.text_area("Immediate Actions Taken (Optional)")

        additional_comments = st.text_area("Additional Comments/Notes (Optional)")
        submitted = st.form_submit_button("Submit")
        if submitted and (college_name == "Choose an Option" or issue_type == "Choose an Option" or location == "Choose an Option" or not description):
            # You can add code here to handle the form submission
            alert = st.warning("Fill the form completely.")
            time.sleep(2)
            alert.empty()
        elif phone and not validate_phone_number(phone):
            alert = st.warning("Enter Valid Phone Number.")
            time.sleep(2)
            alert.empty()
        elif date and not validate_date(date):
            alert = st.warning("Enter Valid Date in the format of 'YYYY-MM-DD'.")
            time.sleep(2)
            alert.empty()
        elif submitted:
            # api call
            r_data = f"""{{
                        "actions_taken": "{actions_taken}",
                        "additional_comments": "{additional_comments}",
                        "college_name": "{college_name}",
                        "date": "{date}",
                        "description": "{description}",
                        "email": "{email}",
                        "fullname": "{user}",
                        "issue_type": "{issue_type}",
                        "location": "{location}",
                        "phone": "{phone}",
                        "witnesses": "{witnesses}"
                        }}"""

            # api call
            response = requests.post(url="http://127.0.0.1:8000/api/submit", data=r_data, headers={'Content-Type': 'application/json'})
            print(response)
            alert = st.success("Thank you! Your report has been submitted.")
            time.sleep(2)
            alert.empty()


if __name__ == "__main__":
    st.set_page_config(
        page_title="NU Assist",
        page_icon=":handshake",
        layout="wide"
    )

    st.sidebar.title("NU Assist")
    page = st.sidebar.selectbox(
        "Select a page",
        ["Login","Register","Report a Social Issue", "View Reports", "Ask Me Anything!"]
    )

    if page == "Login":
        login()
    elif page == "Register":
        register()
    elif page == "Report a Social Issue":
        social_issue_report_form()
    elif page == "View Reports":
        st.subheader("View Reports")
        data_reports()
    else:
        chatbot()


