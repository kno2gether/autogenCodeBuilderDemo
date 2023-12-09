# AgentBuilder Using Autogen to create AI Agents autonomously

Prerequisites
Basic AI knowledge.
Software: VS Studio, Anaconda or similar, Python 3.11.
Step 1: Import Necessary Modules
Start by importing required modules:

python
Copy code
import autogen
from autogen.agentchat.contrib.agent_builder import AgentBuilder

Step 2: Create Necessary Configurations
Set your LLM configurations:

python
Copy code
config_path = 'OAI_CONFIG_LIST.json'
config_list = autogen.config_list_from_json(config_path)
default_llm_config = {'temperature': 0}

Step 3: Initialize The Agent Builder
Set up the Agent Builder:

python
Copy code
builder = AgentBuilder(config_path=config_path, builder_model='gpt-4-1106-preview', agent_model='gpt-4-1106-preview')

Step 4: Define The Task for AutoBuilder
Ensure the task is generic with an example:

python
Copy code
building_task = "Find a paper on arxiv by programming, and analyze its application in some domain. For example, find a latest paper about gpt-4 on arxiv and find its potential applications in software."

Step 5: Building Agents
Define agent configurations and specify coding ability:

python
Copy code
agent_list, agent_configs = builder.build(building_task, default_llm_config, coding=True)

Step 6: Create Multi-Agent Group Chat
Facilitate communication among agents:

python
Copy code
group_chat = autogen.GroupChat(agents=agent_list, messages=[], max_round=12)

Step 7: Create Manager for Group Chat
Set up a manager for the group chat:

python
Copy code
manager = autogen.GroupChatManager(groupchat=group_chat, llm_config={"config_list": config_list, **default_llm_config})

Step 8: Initiate the Chat
Start the task execution:

python
Copy code
agent_list[0].initiate_chat(manager, message="find top 4 latest Paper about GPT4 and its implication on Cybersecurity")
