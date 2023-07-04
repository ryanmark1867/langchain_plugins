# Experiments with LangChain and plugins

Combine Langchain with ChatGPT plugins.

[langchain_plugin.py](https://github.com/ryanmark1867/langchain-pandas/blob/main/langchain_pandas.py):
- does some things to be specified later

`langchain_pandas.py` assumes that there is a yaml config file called `langchain_plugin.yml` in the same directory as the Python file with the following format to specify your `openai_key` and the identifier of the plugin that is used to index the `plugin_url` that is used to define the `tool` object and the `plugin_prompt`.

```
general:
   openai_key: 'your_openai_key'
   plugin: 'klarna'
plugin_url:
   klarna: "https://www.klarna.com/.well-known/ai-plugin.json"
   wolframalpha: "https://www.wolframalpha.com/.well-known/ai-plugin.json"
   expedia: "https://www.expedia.com/.well-known/ai-plugin.json"
plugin_prompt:
   klarna: "what t shirts are available in klarna?"
   wolframalpha: "what is the square root of 169?"
   expedia: "What direct flights are available from Kitchener, Ontario to Vancouver, BC?"
```

Uses as input [LangChain documentation](https://python.langchain.com/docs/modules/agents/tools/integrations/chatgpt_plugins).

