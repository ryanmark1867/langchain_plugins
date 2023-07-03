# import libraries

import numpy as np
import pandas as pd
from langchain.llms import OpenAI
from langchain.llms import VertexAI
from langchain.chat_models import ChatOpenAI
from langchain.agents import load_tools, initialize_agent
from langchain.agents import AgentType
from langchain.tools import AIPluginTool
import os
import yaml

# get config values from config file
current_path = os.getcwd()
print("current directory is: "+current_path)
path_to_yaml = os.path.join(current_path, 'langchain_plugin.yml')
print("path_to_yaml "+path_to_yaml)
try:
    with open (path_to_yaml, 'r') as c_file:
        config = yaml.safe_load(c_file)
except Exception as e:
    print('Error reading the config file ', e)


# define tool
tool = AIPluginTool.from_plugin_url("https://www.klarna.com/.well-known/ai-plugin.json")

# use standard pandas approach to answer the questions

# set LLM type
os.environ["OPENAI_API_KEY"] = config['general']['openai_key']
llm = ChatOpenAI(temperature=0)
tools = load_tools(["requests_all"])
tools += [tool]

agent_chain = initialize_agent(
    tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True
)
agent_chain.run("what t shirts are available in klarna?") 







