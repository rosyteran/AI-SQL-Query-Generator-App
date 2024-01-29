import streamlit as st
import google.generativeai as generativeai

GOOGLE_API_KEY = "AIzaSyBQVdiPRhrZgNh8y6krN1CrafWHeE3RkgY"
generativeai.configure(api_key=GOOGLE_API_KEY)
model = generativeai.GenerativeModel("gemini-pro")


#st.set_page_config(page_title="Streamlit App")
st.set_page_config(
    page_title="Query Generator App",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'About': "# This is a Query Generator App"
    }
)
def main():
    st.markdown(
        """
            <div style="text-align: center;">
                 <h1>🤖AI SQL Query Generator App🧠</h1>
                 <h3>With this app, you can interact with a natural language interface to generate SQL queries, making it easier for both beginners and experienced SQL users to work with databases.</h3>
                 <h4>Made by <a href="https://www.linkedin.com/in/adad74/">Adad Al Shabab</a></h4>
                 <p>For more information, visit <a href="https://www.streamlit.io/">Streamlit</a></p>
            </div>

        """,
        unsafe_allow_html=True,
    )


text_input = st.text_input("Enter your query in Plain English")
submit = st.button("Generate SQL Query")
if submit:
    
    #st.write(response.text)
    with st.spinner("Generating SQL Query..."):
        template = """
            Created a SQL query snippet for the following text:

            ```
                {text_input}
            ```
            I just want a SQL Query.   



            """
        formatted_template = template.format(text_input=text_input)
        #st.write(formatted_template)
        response = model.generate_content(formatted_template)
        sql_query = response.text

        sql_query = sql_query.strip().lstrip("```sql").rstrip("```")
        #st.write(sql_query)

        expected_output = """
            What would be the expected response of this SQL Query snippet:
            ```
               {sql_query}
            ```
            Provide sample tabular response with no explanation:


"""

        expected_output_formatted = expected_output.format(sql_query=sql_query)
        eoutput = model.generate_content(expected_output_formatted)
        eoutput = eoutput.text
        #st.write(eoutput)

        explanation = """
            Explain this SQL Query snippet:
            ```
               {sql_query}
            ```
            Please provide with simplest of explanation with details in 1000 words with bullet points & exmaples:
    """
        explanation_formatted = explanation.format(sql_query=sql_query)
        explanation_output = model.generate_content(explanation_formatted)
        explanation_output = explanation_output.text
        #st.write(explanation_output)

        with st.container():
            st.success("The SQL Query snippet is generated successfully! Here is your Query below:")
            st.code(sql_query, language="sql")
            st.success("Expected output of this SQL Query will be:")
            st.markdown(eoutput)
            st.success("Explanation of the SQL Query:")
            st.markdown(explanation_output)

main()