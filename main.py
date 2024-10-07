from agent import agent_executor
from langchain_core.messages import AIMessage, HumanMessage

from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.chat_history import BaseChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory

store = {}
def get_session_history(session_id: str) -> BaseChatMessageHistory:
    if session_id not in store:
        store[session_id] = ChatMessageHistory()
    return store[session_id]

agent_with_chat_history = RunnableWithMessageHistory(
    agent_executor,
    get_session_history,
    input_messages_key="input",
    history_messages_key="chat_history",
)

def main():
    while(True):
        question = input("Enter your query \n")
        if question.lower() == "exit":
            print("Happy to end!!")
            break
        # res = agent_executor.invoke({"input":question})
        res = agent_with_chat_history.invoke(
                {"input": question},
                config={"configurable": {"session_id": "<foo>"}},
            )
        print(res)
        
if __name__ == "__main__":
    main()