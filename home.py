import streamlit as st
import base64

# ---------------------------------------------------------
# 1. Page Configuration
# (This must be the very first Streamlit command!)
# ---------------------------------------------------------
st.set_page_config(
    page_title="Boyan Zhang Portfolio",
    page_icon="📊",
)

# ---------------------------------------------------------
# 2. Define the Home Page Content
# ---------------------------------------------------------
def home_page():
    # ----- Sidebar Section -----
    with st.sidebar:
        # Since files are in the root, we just use the filename directly
        st.image("eae_img.png", width=200)
        
        st.header("Introduction to Programming Languages for Data")
        st.write("###")
        st.write("***Final Project - Dec 2025***")
        st.write("**Author:** [Boyan Zhang](https://www.linkedin.com/in/boyan-zhang-4b744798/) ")
        st.write("**Instructor:** [Enric Domingo](https://github.com/enricd)")


    # ----- Main Page Title -----
    st.html("""<div style="text-align: center;"><h1 style="text-align: center;">👋 Hi! My name is Boyan Zhang</h1></div>""")


    # ----- Profile Image Handling (Base64) -----
    # We read the file directly since it's now in the same folder
    try:
        with open("profile.png", "rb") as img_file:
            img_base64 = base64.b64encode(img_file.read()).decode()
        
        img_src = f"data:image/png;base64,{img_base64}"

        # Display Profile Image using HTML for circular style
        st.html(f"""
        <div style="display: flex; justify-content: center;">
            <img src="{img_src}" alt="Boyan Zhang" width="300" height="300" style="border-radius: 50%; object-fit: cover; margin-top: 40px; margin-bottom: 40px;">
        </div>
        """)
    except FileNotFoundError:
        st.error("Error: 'profile.png' not found. Please ensure the file is in the root directory.")


    # ----- Current Role -----
    current_role = "EAE Student"
    st.html(f"""<div style="text-align: center;"><h4><i>{current_role}</i></h4></div>""")

    st.write("##")  # Spacer


    # ----- About Me Section -----
    st.subheader("About Me")
    st.write("""
    - 🧑‍💻 I am a Student of EAE Business School, Master of Big Data.
    - 🛩️ Prev: SAP Consultant
    - 🎓 Education: Master of UPC & EAE Business School
    - 🏠 Barcelona
    """)


# ---------------------------------------------------------
# 3. Navigation Setup
# ---------------------------------------------------------
pg = st.navigation([
    st.Page(home_page, title="Home", icon="👋"),
    st.Page("pages/01_image_cropper.py", title="Image Cropper", icon="🖼️"),
    st.Page("pages/02_netflix_data_analysis.py", title="Netflix Data Analysis", icon="🎬"),
    st.Page("pages/03_temperatures_dashboard.py", title="Temperatures Dashboard", icon="🌦️"),
])

# Run the app
pg.run()