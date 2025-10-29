import streamlit as st

# Set the title and icon for the page
st.set_page_config(
    page_title="Program Apprentice 3u1i@FHPK", #untuk header taskbar
    page_icon="🎓", #untuk header taskbar
)

genetic = st.Page('gen_algo.py', title='Genetic Algorithm', icon=":material/business:")
travelling = st.Page('tsp.py', title='Travelling Salesman', icon=":material/business:")
home = st.Page('home.py', title='Homepage', default=True, icon=":material/home:")

pg = st.navigation(
        {
            "Menu": [home,travelling,genetic]
        }
    )

pg.run()
