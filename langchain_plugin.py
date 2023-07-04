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
print("plugin is: ",config['general']['plugin'])
print("plugin_url is: ",config['plugin_url'][config['general']['plugin']])
tool = AIPluginTool.from_plugin_url(config['plugin_url'][config['general']['plugin']])

# set LLM type
os.environ["OPENAI_API_KEY"] = config['general']['openai_key']
llm = ChatOpenAI(temperature=0)
#tools = load_tools(["requests_all"])
tools = load_tools(["requests"])
tools += [tool]

agent_chain = initialize_agent(
    tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True
)

# invoke the plugin with the prompt
print("plugin_prompt is: ",config['plugin_prompt'][config['general']['plugin']])
agent_chain.run(config['plugin_prompt'][config['general']['plugin']])






