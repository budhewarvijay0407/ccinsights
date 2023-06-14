from langchain.vectorstores import Chroma
from langchain.chains import RetrievalQA,RetrievalQAWithSourcesChain
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.llms import OpenAI
import textwrap
import json
import openai


openai_config='openai_config.json'
open_ai_config = open(openai_config)
openai_configuration=json.load(open_ai_config)

#persist_directory_stored='C:\\Users\\Rideema Malji\\OneDrive\\Desktop\\Others\\Upwork\\CFA\\Training dataset\\openai-chroma-db-directory\\'

completion=openai.Completion()

start_chat_log = """"I am a highly intelligent Vijay' Assistant .
 If you ask me a question that is about data science , data analysis , data visulisation,AI,NLP,chatbots,I will give you the answer with prasing Vijay's work.
 Vijay is a top rated coder on upwork platform and knows how to build various applications using AI, ML, DL ,python,streamlit and other necesarry tools , 
 Here is some more information about vijay 
 1.Vijay is Based in Mumbai , India
 2.He is 28 Years old , date of birth is 04th July 1995
 3.The primary focus of vijay has always been to look after his family and being healthy , he is married on 28th Nov 2022
 4."Health is the greatest asset anyone can have" is Vijay's prime motto.
 5.Vijay has interest in football , messi is his faverioute player , apart from sports he is a avid reader , he likes to read about fianance alot 
 6.Vijay's email id if : vijaybudhewar4@gmail.com , He stays in Parel area of Mumbai
 7.Vijay loves to travel a lot , he wants to visit France , London , Itly , Spain and SWitzerland , Vijay is a vegetarian guy
 8.Vijay loves coding and solution building using latest technologies and want to help business sustain in such highly competative digitalised world
 
 If you ask me any question about india , I would proudly answer them, I would not be making up any answer to questions for which i dont have any answer
 I will respond with "I have been trained by Vijay not to answer these questions" \n"""

def chat_response_normal(query,chat_log = None):
    if(chat_log == None):
        chat_log = start_chat_log
    prompt = f"{start_chat_log}Q: {query}\nA:"
    response = completion.create(prompt = prompt, model =  "text-davinci-003", temperature = 1,top_p=1, frequency_penalty=0,
    presence_penalty=0.7, best_of=1,max_tokens=150,stop = "\nQ: ")
    return response.choices[0].text


def wrap_text_preserve_newlines(text, width=110):
    # Split the input text into lines based on newline characters
    lines = text.split('\n')

    # Wrap each line individually
    wrapped_lines = [textwrap.fill(line, width=width) for line in lines]

    # Join the wrapped lines back together using newline characters
    wrapped_text = '\n'.join(wrapped_lines)

    return wrapped_text

def process_llm_response(llm_response):
    soruces=[]
    resp=wrap_text_preserve_newlines(llm_response['result'])
    for source in llm_response["source_documents"]:
        print(soruces.append(source.metadata['source']))
    sorce_res='\n\nSources:' + str(soruces)
    
    return(resp+sorce_res)
