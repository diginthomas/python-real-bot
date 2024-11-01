
import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os
 
load_dotenv()
 
genai.configure(api_key=os.getenv("GEMINI_API"))
 
#defining the function
def get_gemini_response(input):
    try:
        model = genai.GenerativeModel('gemini-pro')
        response = model.generate_content([input])
        return response.text
    except Exception as e:
        print("err in gemini ai connection",e)

 
## streamlit app
st.title("Gemini Response")
input_text = st.text_area("Input for search: ", key="input_one")
submit1 = st.button("Search")
 
if submit1 :
    try :
        response = get_gemini_response(input_text)
        st.write(response)
    except Exception as e :
        print('err in submit data ====> ',e)