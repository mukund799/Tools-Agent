from langchain_cohere import ChatCohere
def load_llm():
    llm = ChatCohere(model="command-r", cohere_api_key="cd0X7DVXjVCyGcFXC1w3ps5dA6r00pVaQhADXfof")
    return llm