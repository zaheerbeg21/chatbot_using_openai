import streamlit as st
import pandas as pd
import openai

# openai api
openai.api_key = "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"

# files format
uploaded_file = st.file_uploader("Upload file", type=["txt", "csv", "json"])

if uploaded_file is not None:
    if uploaded_file.type == "text/plain":
        df = pd.read_csv(uploaded_file)
    elif uploaded_file.type == "text/csv":
        df = pd.read_csv(uploaded_file)
    elif uploaded_file.type == "application/json":
        df = pd.read_json(uploaded_file)


if st.button("Ask"):
    question = st.text_input("Ask a question")
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=question,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    st.write(response.choices[0].text)




