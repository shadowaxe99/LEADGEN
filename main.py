
# Streamlit code for a Fun and Intuitive Lead Generation App

# Import required modules for utility features
import pandas as pd
import random

# Title and description
st.title("Fun & Intuitive Lead Generation App 🎉")
st.write("Discover business opportunities in the most delightful way! 🚀")

# Instructions
st.write("### How to Use 🤔")
st.write("Just fill in the search criteria below and hit the **Search** button. For a surprise, try the **I'm Feeling Lucky** button! 🍀")

# Basic Input fields with placeholder text
st.write("### Let's Find Some Leads! 🎯")
industry_type = st.selectbox("Industry Type 🏭", ["", "Technology 🖥", "Healthcare 🏥", "Finance 💰", "Education 📚"])
location = st.text_input("Location 🗺", placeholder="e.g., New York")
company_size = st.selectbox("Company Size 👥", ["", "1-10 👨‍💻", "11-50 👩‍💼", "51-200 👩‍🔬", "201-500 👨‍🚀", "500+ 👩‍✈️"])

# Fun Feature: I'm Feeling Lucky Button
if st.button("I'm Feeling Lucky 🍀"):
    st.write("Finding you a random lead... 🎲")
    # Implement your random lead logic here (Example provided below)
    random_lead = {
        "Name": "Lucky Company",
        "Location": "Neverland",
        "Size": "1-10",
        "Industry": "Fun & Games"
    }
    st.write(f"### Here's Your Lucky Lead! 🌟")
    st.write(random_lead)

# Search Button and Validation
elif st.button("Search 🔍"):
    if not industry_type:
        st.warning("Please select an Industry Type. 🚫")
    elif not location:
        st.warning("Please enter a Location. 🚫")
    else:
        st.write(f"Searching for leads in the {industry_type} industry, located in {location}, with a company size of {company_size}. 🕵️‍♀️")
        # Implement your search logic here (Example provided below)
        example_leads = pd.DataFrame({
            "Name": ["Company A", "Company B"],
            "Location": ["New York", "San Francisco"],
            "Size": ["1-10", "11-50"],
            "Industry": ["Technology", "Healthcare"]
        })
        st.write("### Search Results 📋")
        st.write(example_leads)

# Reset Button to Clear Fields
if st.button("Reset 🔄"):
    industry_type = ""
    location = ""
    company_size = ""
    st.experimental_rerun()

# Search History (Example)
st.write("### Search History 🕰")
st.write("1. Technology, San Francisco, 11-50")
st.write("2. Healthcare, New York, 51-200")

# Fun GIF for engagement
st.write("### Having Fun Yet? 😄")
st.image("https://media.giphy.com/media/3oEjI6SIIHBdRxXI40/giphy.gif")
