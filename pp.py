# professional_profile.py

import streamlit as st
from PIL import Image

# ----- CONFIG -----
st.set_page_config(page_title="Professional Profile", layout="wide")

# ----- LOAD ASSETS -----
profile_pic = Image.open("purushoth.jpg")  # Place this image in the same folder

# ----- HEADER -----
with st.container():
    col1, col2 = st.columns([1, 3])
    with col1:
        st.image(profile_pic, width=150)
    with col2:
        st.title("Purushothaman")
        st.subheader("Senior Specialist in Data Analytics")
        st.write("📍 Chennai | 📧 purushothamanpalani@outlook.com | 🌐 www.yourwebsite.com")

# ----- ABOUT -----
with st.container():
    st.markdown("## About Me")
    st.write("""
        Successful Data Analytics and Automation Professional with over 7 years of experience in data analysis, data visualization, database management, statistical analysis, project management and automation.
        Highly skilled in utilizing advanced analytics tools and programming languages such as Databricks, SQL, PySpark, Pandas, Python, Power BI, VBA Macro and Advanced Excel.
        Proficient in all phases of data processing, including data collection, cleaning, transformation, integration, exploration, and interpretation, to support comprehensive business reporting.
        Demonstrated expertise in developing automation solutions that streamline data processing and reporting, significantly enhancing efficiency and accuracy.
    """)

# ----- WORK EXPERIENCE -----
with st.container():
    st.markdown("## Work Experience")
    st.write("---")
    st.write("**Senior Specialist in Data Analytics - Adidas**")
    st.write("📅 Apr 2023 - Present")
    st.write("""

        - Comprehensive Reporting: I deliver the financial data analytical reports on a daily, weekly, and monthly basis using advanced tools such as Databricks, SQL, PySpark, Python, Pandas, Power BI, VBA Macro, and Advanced Excel. This ensures precise and actionable insights that drive informed decision-making.
        - Technical Training: I am responsible for providing technical training to new joiners, ensuring they well-equipped to perform their tasks effectively. My efforts enhance their proficiency and contribute to the overall productivity of the team.
        - Project Management: I lead project management activities, including gathering project requirements, evaluating timelines, coordinating with stakeholders, providing weekly status updates, and securing project closure confirmation from stakeholders.
        - Quality Assurance: I perform quality checks across various projects, ensuring accurate data sourcing, identifying and resolving data gaps, cleansing data, implementing necessary structural modifications and calculations to meet specific requirements. This guarantees the generation of accurate and reliable reports.
        - Automation Ownership: Proficient in identifying automation opportunities and implementing solutions to improve productivity and reduce errors with the aid of technologies like Databricks, SQL, PySpark, Python, Pandas, Power BI, and VBA Macro. Which result in very minimal manual intervention, increased accuracy and efficiency. 
        - Team Leadership: I handle team management responsibilities, fostering a collaborative and productive environment by providing support on creating the prototype for solutions. My leadership ensures that the team operates efficiently and achieves its objectives.
    """)

    st.write("**Senior Data Analyst - NielsenIQ**")
    st.write("📅 Oct 2021 - Apr 2023")
    st.write("""
        - Data-Driven Reporting: Consistently prepare reliable reports to support data driven business decisions using advanced tools such as SQL, Power BI, Python,Pandas, VBA Macro, and Advanced Excel.
        - Market Research Analysis: Effectively cater to client requirements by providing comprehensive market research analysis, and delivering sales actual and forecast reports through various analytical methods.
        - Data Structuring: Ensure data is structured accurately, completely, adequately, and user-friendly to facilitate further analysis and reporting, while guiding and supporting the team in these processes.
        - Technical Training: Responsible for delivering technical training to new joiners, ensuring they are well-prepared to perform their assigned tasks efficiently.
        - Automation Ownership: Proficient in identifying automation opportunities and implementing solutions to improve productivity and reduce errors with the aid of technologies like Python, Pandas, SQL, Power BI, VBA Macro. Which result in very minimal manual intervention, increased accuracy and efficiency. 
        - Team Leadership: I handle team management responsibilities, fostering a collaborative and productive environment by providing support on creating the prototype for solutions. My leadership ensures that the team operates efficiently and achieves its objectives.
    """)

# ----- SKILLS -----
with st.container():
    st.markdown("## Skills")
    skills = ["Data Analysis", "Power BI", "SQL", "Databricks", "Python", "PySpark", "Pandas", "VBA Macro", "Advanced Excel"]
    cols = st.columns(3)
    for i, skill in enumerate(skills):
        cols[i % 3].markdown(f"- {skill}")

# ----- PROJECTS -----
with st.container():
    st.markdown("## Projects")
    st.write("### 🔍 Project Title 1")
    st.write("Short description of the project. [GitHub](https://github.com/yourhandle/project1)")

    st.write("### 📊 Project Title 2")
    st.write("Brief explanation and what tech was used. [Demo](https://yourwebsite.com/demo)")

# ----- SOCIAL LINKS -----
with st.container():
    st.markdown("## Connect with Me")
    st.write("[LinkedIn](https://linkedin.com/in/yourhandle) | [GitHub](https://github.com/yourhandle) | [Portfolio](https://yourwebsite.com)")

# Optional footer
st.markdown("---")
st.caption("Made with ❤️ using Streamlit")
