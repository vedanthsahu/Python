import requests #This is to make requess and get the data from endpoints
import json #This is to parse json which is basically the output of the most of the htttp requests
from langchain.agents import Agent #This is the latest Langchain module which can apparently make all in one package
from langchain_core.prompts import ChatMessagePromptTemplate #This is to pipeline and get the prompt to the LLM
import os #THis is to make use of loadenv
import time #This is log time of execution

from dotenv import load_dotenv 
from langchain.agents import create_openapi_agent
from langchain.tools import tool #THisis to annotate any function or tools. basically to get the LLM/agent to  find the  tool

from dataclasses import dataclass 
load_dotenv()
#Simple usage of tool

@tool('get_weather', description="This is the description. Use this to get weather of a city")

def get_weather(city:str):
    response = requests.get(f"https://wttr.in/{city}?format=j1")
    return response.json()

agent = create_openapi_agent(
    model = "gpt-4o",#use model which can support tool usage
    tools= [get_weather],
    system_prompt = "you are a weather expert"

)

response = agent.invoke(
    {
        "messages":[
            {"role": "user",
            "content": "What is the weather in India"
            }
        ]
    }
)
print(response)
print(response["messages"][-1])



#To interact with a model. Just basic interaction

from langchain.chat_models import init_chat_model

model = init_chat_model(
    model = "modelname",
    temperature = 0.1
)

response1= model.invoke("Hello, what is python")

print(response1)
print(response1.content)

from langchain.messages import HumanMessage