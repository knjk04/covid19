import streamlit as st

app_title = "COVID-19 Dashboard"
st.set_page_config(page_title=app_title)
st.title(app_title)

st.map()

st.divider()


st.markdown("Disclaimer: this is for education purposes only and the data may "
            "not be accurate. Please corroborate all information here with "
            "the official source in your country.")

st.markdown("If you spot a bug, create an issue on the "
            "[GitHub repo](https://github.com/knjk04/covid19/)")
