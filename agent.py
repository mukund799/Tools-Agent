from langchain.agents import (AgentExecutor, create_tool_calling_agent, AgentType)
from langchain_core.prompts import ChatPromptTemplate
from tools import tools
from llm import load_llm
llm = load_llm()
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You can only respond using the provided tools. if you can't find answer using the tools, then only response back to user that 'Sorry, I cannot answer that.'\n"),
        ("human", "{input}"),
        # Placeholders fill up a **list** of messages
        ("placeholder", "{agent_scratchpad}")
    ]
)
agent = create_tool_calling_agent(llm,tools,prompt)
agent_executor = AgentExecutor(agent=agent,tools=tools,handle_parsing_errors=True, return_intermediate_steps=True)