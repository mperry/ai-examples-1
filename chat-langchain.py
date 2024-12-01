
# LangChain supports many other chat models. Here, we're using Ollama
from langchain_community.chat_models import ChatOllama
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

import time

start_time = time.perf_counter()

# supports many more optional parameters. Hover on your `ChatOllama(...)`
# class to view the latest available supported parameters
model_llama3 = "llama3"
model_llama2 = "llama2"
model_tiny = "tinyllama"

llm = ChatOllama(model=model_tiny)
prompt = ChatPromptTemplate.from_template("Tell me a short joke about {topic}")

# using LangChain Expressive Language chain syntax
# learn more about the LCEL on
# /docs/concepts/#langchain-expression-language-lcel
chain = prompt | llm | StrOutputParser()

# for brevity, response is printed in terminal
# You can use LangServe to deploy your application for
# production
print(chain.invoke({"topic": "Space travel"}))

end_time = time.perf_counter()
elapsed_time = round(end_time - start_time, 1)
print(f"Elapsed time {elapsed_time}s")


