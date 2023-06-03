import streamlit as st
from streamlit_chat import message
from streamlit_extras.colored_header import colored_header
from streamlit_extras.add_vertical_space import add_vertical_space
import os
from streamlit_lottie import st_lottie
import cfa_bot_library_openai_prod_ccinsights
import json
from PIL import Image
import requests
import openai

#image = Image.open('C:\\Users\\Rideema Malji\\OneDrive\\Desktop\\Others\\Upwork\\openAI-chatbot\\ChatBot-main\\images\\Upwork-Top rated.png')
path_lotti=r'C:\Users\Rideema Malji\OneDrive\Desktop\Others\Upwork\openAI-chatbot\ChatBot-main\lottie\business-analysis.json'



def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")

with open (path_lotti,"r") as file:
    json_lotti = json.load(file)
    
openai_config='openai_config.json'  #give standard path
open_ai_config = open(openai_config)
openai_configuration=json.load(open_ai_config)
os.environ['OPENAI_API_KEY']=openai_configuration['key']
openai.api_key=openai_configuration['key']


# image_logo=Image.open('C:\\Users\\Rideema Malji\\OneDrive\\Desktop\\Others\\Upwork\\openAI-chatbot\\ChatBot-main\\images\\CCI-logo.png')
# image_logo=image_logo.resize((10,10))
#st.set_page_config(page_title="AI Assistance - An LLM-powered Streamlit app")


with st.sidebar:
    # st.image(image_logo, caption='CCI accounts for the projects undertaken by Vijay')
    st_lottie(json_lotti,reverse=True,height=350,  width=350,speed=1,  loop=True,quality='high')
    st.title("Vijay B.'s tech portfolio")
    
    st.markdown('''Meet my AI assistance chatbot Powered by the OpenAI's advanced fine tunned models
                Want to make one for your business?
    ''')
    st.markdown('''These applications are developed and managed by -Vijay B. (vijay.b@ccinsights.com)
    ''')
    st.markdown("**Unleash the Power of AI: Upskill your business!**")
    #st.image(image, caption='AI Application System')
    
tab1,tab2, tab3, tab4 = st.tabs(["Vijay B.-Upwork top rated :star:","Try my AI Assistance", "Summary maker", "Text Classifier/Anomaly Detection"])



with tab1:
    lottie_coding = load_lottieurl("https://assets2.lottiefiles.com/packages/lf20_iv4dsx3q.json")
    
    #st.image(image, caption='Last Updated : 01-06-2023')
    # ---- HEADER SECTION ----
    with st.container():
        st.title("A Upwork Top rated: Data Scientist and MLops Engineer From India")
        st.write(
            "I am passionate about finding ways to use AI to be more efficient and effective in business settings."
        )

    # ---- WHAT I DO ----
    with st.container():
        st.write("---")
        left_column, right_column = st.columns(2)
        with left_column:
            st.header("How do I Impact on businesses")
            st.write("##")
            st.write(
                """
                I have benn working as an entrepreneur since past 6 years and I have deep interests in Technology , I can help businesses who:
                - are looking for a way to leverage the power of AI in their day-to-day work.
                - are struggling with repetitive tasks which can be Automated easily using AI.
                - want to know how Data can have impact on their processes .
                If this sounds interesting to you, consider subscribing and turning on the notifications, so you don’t miss any content.
                """
            )
        with right_column:
            st_lottie(lottie_coding, height=300, key="coding")

    # ---- PROJECTS ----

    # ---- CONTACT ----
    with st.container():
        st.write("---")
        st.header("Get In Touch With Me!")
        st.write("##")

        # Documention: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
        contact_form = """
        <form action="https://formsubmit.co/YOUR@MAIL.COM" method="POST">
            <input type="hidden" name="_captcha" value="false">
            <input type="text" name="name" placeholder="Your name" required>
            <input type="email" name="email" placeholder="Your email" required>
            <textarea name="message" placeholder="Your message here" required></textarea>
            <button type="submit">Send</button>
        </form>
        """
        left_column, right_column = st.columns(2)
        with left_column:
            st.markdown(contact_form, unsafe_allow_html=True)
        with right_column:
            st.empty()


with tab2:
    
    if 'generated' not in st.session_state:
        print('Inside')
        st.session_state['generated'] = ["I'm your AI Assistant, How may I help you?"]
    
    if 'past' not in st.session_state:
        st.session_state['past'] = ['Hi!']
        
    print(st.session_state)
        
    
    def get_text():
        input_text = st.text_input("You: ", "", key="input")
        #st.session_state["You: "] = ""
        return input_text
    
    def generate_response(prompt):
        response = cfa_bot_library_openai_prod_ccinsights.chat_response_normal(prompt,openai_configuration['model'])
        #response = "Hi Im Vijay's Assistant , Im currenty under development and maintenance and cant answer your whole questions"
        return response
    
    def resp():
        with response_container:
            if user_input:
                response = generate_response(user_input)
                st.session_state.past.append(user_input)
                st.session_state.generated.append(response)
                
            if st.session_state['generated']:
                for i in range(len(st.session_state['generated'])):
                    message(st.session_state['past'][i], is_user=True, key=str(i) + '_user')
                    message(st.session_state['generated'][i], key=str(i))
                #st.session_state["text"] = ""
    
    response_container = st.container()
    user_input=None                
    input_container = st.container()
    colored_header(label='', description='', color_name='blue-30')
    with input_container:
        user_input = get_text()
        resp()

    
