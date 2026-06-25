import streamlit as st

st.title("This is a title text")

st.title("_This_ is :blue[a title text] :speech_balloon:")


st. title('$E = mc^2$')

st.header("This is a header")

st.subheader("This is a subheader")

st.text("This is a plain text with no formatting")

st.markdown("# This is a header\n **This is bold text** \n- This a list item")

st.write("This a plain text using st.write")


data = {
    "Name": "Alice",
    "Age": 30,
    "Occupation": "Engineer"
}


st.write(data)