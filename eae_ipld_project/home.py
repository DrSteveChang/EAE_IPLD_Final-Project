import streamlit as st
import base64
import os

# ---------------------------------------------------------
# FIX: Use absolute path to locate the image
# ---------------------------------------------------------

# 1. Get the directory where this current script (home.py) is located
current_dir = os.path.dirname(os.path.abspath(__file__))

# 2. Construct the full path to the image file
#    This joins the directory path with the filename
image_path = os.path.join(current_dir, "eae_img.png")

# 3. Display the image
st.image(image_path, width=200)
    
# ----- Page configs (tab title, favicon) -----
st.set_page_config(
    page_title="<Your Name> Portfolio",
    page_icon="📊",
)


def home_page():
    # ----- Left menu -----
    with st.sidebar:
        st.image("eae_img.png", width=200)
        st.header("Introduction to Programming Languages for Data")
        st.write("###")
        st.write("***Final Project - Dec 2025***")
        st.write("**Author:** [Boyan Zhang](https://www.linkedin.com/in/boyan-zhang-4b744798/) ")
        st.write("**Instructor:** [Enric Domingo](https://github.com/enricd)")


    # ----- Top title -----
    st.html("""<div style="text-align: center;"><h1 style="text-align: center;">👋 Hi! My name is Boyan Zhang</h1></div>""")  # TODO: Add your name


    # ----- Profile image file -----
    profile_image_file_path = "profile.png"       # TODO: Upload your profile image to the same folder as this script and update this if it has a different name

    with open(profile_image_file_path, "rb") as img_file:
        img = "data:image/png;base64," + base64.b64encode(img_file.read()).decode()


    # ----- Your Profile Image -----
    st.html(f"""
    <div style="display: flex; justify-content: center;">
        <img src="{img}" alt="Your Name" width="300" height="300" style="border-radius: 50%; object-fit: cover; margin-top: 40px; margin-bottom: 40px;">
    </div>
    """)


    # ----- Personal title or short description -----
    current_role = "EAE Student"   # TODO: Change this

    st.html(f"""<div style="text-align: center;"><h4><i>{current_role}</i></h4></div>""")

    st.write("##")    # Adding some space


    # ----- About me section -----
    st.subheader("About Me")

    # TODO: Modify and adapt the following lines to your info, you can add or remove some details if you want
    st.write("""
    - 🧑‍💻 I am a Student of EAE Business School of Master of Bigdata now.

    - 🛩️ prev: SAP Consultant

    - 🎓 Education: Master of UPC& EAE Business School

    - 🏠 Barcelona
    """)

    # Feel free to add other points like your Linkedin, Github, Social Media, etc.


# This is ensambling the entire app with the different pages and the navigation menu
pg = st.navigation([
    st.Page(home_page, title="Home", icon="👋"),
    st.Page("pages/01_image_cropper.py", title="Image Cropper", icon="🖼️"),
    st.Page("pages/02_netflix_data_analysis.py", title="Netflix Data Analysis", icon="🎬"),
    st.Page("pages/03_temperatures_dashboard.py", title="Temperatures Dashboard", icon="🌦️"),
])
pg.run()