from langchain.agents import (AgentExecutor, create_tool_calling_agent)
from langchain_core.prompts import ChatPromptTemplate
from tools import tools
from llm import load_llm
llm = load_llm()
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant. Return the response as it is. Answer from the tools only. You have no right to give response from other source."),
        ("human", "{input}"),
        # Placeholders fill up a **list** of messages
        ("placeholder", "{agent_scratchpad}")
    ]
)
agent = create_tool_calling_agent(llm,tools,prompt)
agent_executor = AgentExecutor(agent=agent,tools=tools,handle_parsing_errors=True)
