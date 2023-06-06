import streamlit as st
from streamlit_chat import message
from streamlit_extras.colored_header import colored_header
import os
from langchain.vectorstores import Chroma
from langchain.embeddings.openai import OpenAIEmbeddings
from streamlit_lottie import st_lottie
import cfa_bot_library_openai_prod_ccinsights
import json
from langchain.text_splitter import RecursiveCharacterTextSplitter
import requests
import openai
from langchain.llms import OpenAI
from langchain.chains import RetrievalQA
import PyPDF2
from langchain.document_loaders import PyPDFLoader

global qa
qa=None
#image = Image.open('C:\\Users\\Rideema Malji\\OneDrive\\Desktop\\Others\\Upwork\\openAI-chatbot\\ChatBot-main\\images\\Upwork-Top rated.png')
path_lotti=r'lottie\business-analysis.json'
start_text=''



def get_embeddings(total_data):
    # text=''.join(total_data)
    #documents=Document(page_content=text) ####This can be used when you want to craete just one document from the string you have
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=180)
    texts = text_splitter.create_documents(total_data)
    print(texts[0])
    embeddings = OpenAIEmbeddings()
    db = Chroma.from_documents(texts, embeddings,persist_directory='local_db')
    db.persist()
    return(db)

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style.css")

#with open (path_lotti,"r") as file:
#    json_lotti = json.load(file)
    
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
    lotti_sidebar=load_lottieurl("https://assets7.lottiefiles.com/packages/lf20_aa0wy04q.json")
    st_lottie(lotti_sidebar,reverse=True,height=300,  width=300,speed=1,  loop=True,quality='high')
    st.title("Vijay B.'s tech portfolio")
    
    st.markdown('''You can meet my AI assistant chatbot Powered by the OpenAI's advanced fine tunned models
                Want to make one for your business?
    ''')
    st.markdown('''These applications are developed and managed by -Vijay B. (vijay.b@ccinsights.com)
    ''')
    st.markdown("**Unleash the Power of AI: Upskill your business!**")
    #st.image(image, caption='AI Application System')
    
tab1,tab2,tab_qa_docs,tab3, tab4 = st.tabs(["Vijay B.-Upwork top rated :star:","Try my AI Assistant","Q&A on documents" ,"Summary maker-TBD", "Text Classifier-TBD"])



with tab1:
    lottie_coding = load_lottieurl("https://assets2.lottiefiles.com/packages/lf20_iv4dsx3q.json")
    
    #st.image(image, caption='Last Updated : 01-06-2023')
    # ---- HEADER SECTION ----
    with st.container():
        st.title("An Upwork Top rated Data Scientist and MLops Engineer From India")
        st.write(
            "I am passionate about finding ways to use AI to be more efficient and effective in business settings."
        )

    # ---- WHAT I DO ----
    with st.container():
        st.write("---")
        left_column, right_column = st.columns(2)
        with left_column:
            st.header("How do I make Impact on businesses:")
            st.write("##")
            st.write(
                """
                I have been working as a Techie since past 6 years and I have deep interests in AI , I can help businesses who:
                - Want to leverage Large language models (LLMs) to enhance their productivity and reduce the cost. 
                - Are looking for a way to leverage the power of AI in their day-to-day work.
                - Are struggling with repetitive tasks which can be Automated easily using AI.
                - Want to know how Data can have impact on their processes .
                If this sounds interesting to you, consider subscribing below, so you don’t miss any content.
                """
            )
        with right_column:
            st_lottie(lottie_coding, height=300, key="coding")

    # ---- PROJECTS ----

    # ---- CONTACT ----
    with st.container():
        st.write("---")
        st.header("Get In Touch-To Read endless blogs on tech and life lessons!")
        st.write("##")

        # Documention: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
        contact_form = """
        <form action="https://formsubmit.co/vijaybudhewar4@gmail.com" method="POST">
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
        st.session_state['generated'] = ["I'm Vijay's AI Assistant, How may I help you?"]
    
    if 'past' not in st.session_state:
        st.session_state['past'] = ['Hi!']
        
    #print(st.session_state)
        
    
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
        
       

with tab_qa_docs:
    
    if 'chroma_db' not in st.session_state:
        st.session_state['chroma_db']=''
    
    if 'start_text' not in st.session_state:
        st.session_state['start_text']=''
        
    if 'generated_qa' not in st.session_state:
        #print('Inside')
        st.session_state['generated_qa'] = ["Please upload the pdf above and then ask me questions"]
    
    if 'past_qa' not in st.session_state:
        st.session_state['past_qa'] = ['I want to ask some questions regarding my pdfs']

    def get_text_qa():    
        input_text_qa = st.text_input("Your Question: ", "", key="input_text_qa_1")
        return(input_text_qa)
    

    
    def resp_qa():
        with response_container_qa:
            if user_input_qa:
                print('getting response')
                print('User input is :',user_input_qa)
                print('The qa is ',qa)
                response_qa = qa.run(user_input_qa)
                #print(response_qa)
                st.session_state.past_qa.append(user_input_qa)
                st.session_state.generated_qa.append(response_qa)
                
            if st.session_state['generated_qa']:
                for i in range(len(st.session_state['generated_qa'])):
                    message(st.session_state['past_qa'][i], is_user=True, key=str(i) + '__user')
                    message(st.session_state['generated_qa'][i], key=str(i)+'g')
                    
                    
    st.write("*This application only uses first 5 (or less) pages of your PDF*")
    
    
    uploaded_file = st.file_uploader('Upload pdf', type='pdf', accept_multiple_files=False, on_change=None, args=None, kwargs=None, disabled=False, label_visibility="visible")
    response_container_qa = st.container()
    colored_header(label='', description='', color_name='yellow-30')
    
    print('upload file first:',uploaded_file)
    if "uploaded_file_s" not in st.session_state:
        st.session_state.uploaded_file_s = False

    if uploaded_file or st.session_state.uploaded_file_s:
        st.session_state.uploaded_file_s = True
       # data=PyPDFLoader(uploaded_file.getvalue())
        if uploaded_file is not None:
            total_data=[]
            pdf_reader = PyPDF2.PdfReader(uploaded_file)
            if len(pdf_reader.pages)>20:
                len_read=20
            else:
                len_read=len(pdf_reader.pages)
            
            for page_num in range(len(pdf_reader.pages)):
                page = pdf_reader.pages[page_num]
                text = page.extract_text()
                total_data.append(text)
            if st.session_state['start_text']!=total_data:
                print('The condition on start_text is True',start_text)
                print('data read')
                st.session_state['start_text']=total_data
                print('start_text')
                chroma_db=get_embeddings(total_data)
                st.session_state['chroma_db']=chroma_db
                print('db created')
            vectordb_openai = Chroma(persist_directory='local_db', embedding_function=OpenAIEmbeddings())
            retriever_openai = vectordb_openai.as_retriever(search_kwargs={"k": 2})
            qa = RetrievalQA.from_chain_type(llm=OpenAI(model_name="text-davinci-003",max_tokens=400), chain_type="stuff", retriever=retriever_openai)
            print('qa generated is',qa)
    input_container_qa = st.container()
    with input_container_qa:
        user_input_qa = get_text_qa()
        print('I got the input text as :',user_input_qa)
        resp_qa()
    
    st.write(
        """
        -- This application is working using following techstack
        - Python
        - Langchain
        - OpenAI's GPT model
        - Chromadb
        - Streamlit
        
        This is just an overview..alot of things are cooking inside'
        """
    )

            
            
            
            
