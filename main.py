from agent import agent_executor

def main():
    while(True):
        question = input("Enter your query")
        if question.lower() == "exit":
            break
        res = agent_executor.invoke({"input":question})
        print(res['output'])
if __name__ == "__main__":
    main()