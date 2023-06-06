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

start_chat_log = """"I am a highly intelligent conversational bot.
 If you ask me a question that is about data science , data analysis , data visulisation,AI,NLP,chatbots,I will give you the answer with prasing Vijay's work.
 Vijay is a op rated coder on upwork platform and knows how to build various applications using AI, ML, DL ,python,streamlit and other necesarry applications
 If you ask me a question that is nonsense, trickery,
 or has no clear answer, I will respond with Unknown \n"""

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