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


from langchain.tools import tool

@tool
def search_database(query :str) -> None:
    """
    here we connect with the database"""
    pass
#We can give custom names for any tool
@tool("Web_search")
def search(query : str) -> None:
    return "This is the result of search"
print(search.name) #Prints : Web_search

#Now that we have created a tool and gave custom name, we can give custom description
@tool("calculator", description = "This is to perform arthemetic operations")
def calc(extression : str) -> None:
    pass
from pydantic import BaseModel, Field
from typing import Literal

class weatherInput(BaseModel):
    location : str = Field(description="This is the city name")
    units : Literal["celcious", "fahrenheit"] = Field(
        default="celcious",
        description="THis is the units of temperature"
    )
    include_forecast: bool = Field(
        default=False,
        description="Include 5 days of forcast"
    )

@tool(infer_schema=weatherInput)
def getweather(location: str, units="celcious", include_forecast=False):
    """Get current weather and optional forecast."""
    temp = 22 if units == "celsius" else 72
    result = f"Current weather in {location}: {temp} degrees {units[0].upper()}"
    if include_forecast:
        result += "\nNext 5 days: Sunny"
    return result