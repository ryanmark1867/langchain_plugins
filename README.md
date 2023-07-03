# Pandas experiments with LangChain and plugins

Combine Langchain with ChatGPT plugins.

[langchain_plugin.py](https://github.com/ryanmark1867/langchain-pandas/blob/main/langchain_pandas.py):
- does some things to be specified later

`langchain_pandas.py` assumes:
- there is a yaml config file called `langchain_plugin.yml` in the same directory with the following format:

```
general:
   openai_key: 'your_openai_key'
```

Uses as input [LangChain documentation](https://python.langchain.com/docs/modules/agents/tools/integrations/chatgpt_plugins).

