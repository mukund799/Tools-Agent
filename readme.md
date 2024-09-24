This project demonstrates the use of an agent that answers user queries by invoking predefined tools using the LangChain framework. The agent is configured to only use the available tools and will not provide answers outside of their scope.

Prerequisites

Before running the project, make sure you have the following:

	•	Python 3.8 or higher installed.
	•	API key for the Cohere LLM.



Project Structure

	•	agent.py: Defines the agent and its execution flow.
	•	llm.py: Loads the language model from Cohere.
	•	tools.py: Defines the tools that the agent can invoke.
	•	main.py: Main entry point to run the application, where the user interacts with the agent.

Setup Instructions

Step 1: unzip the file

Step 2: Open the file in Vs-code.

Step 3: You can install the required dependencies by running:
    ```python
    pip install -r requirements.txt
    ```

Step 4: Replace the API key in `.env` with your actual Cohere API

Step 5: Run the `main.py` and start asking your question. To ##stop the execution enter `exit`.