# Pandas experiments with LangChain and plugins

Combine Langchain with ChatGPT plugins.

[langchain_plugin.py](https://github.com/ryanmark1867/langchain-pandas/blob/main/langchain_pandas.py):
- loads required libraries
- reads set of question from a yaml config file
- answers the question using hardcoded, standard Pandas approach
- uses Vertex AI Generative AI + LangChain to answer the same questions

`langchain_pandas.py` assumes:
- there is a yaml config file called `langchain_plugin.yml` in the same directory with the following format:

```
general:
   openai_key: 'AB_NYC_2019.csv'
```

