#1. Import Sections
import autogen
from autogen.agentchat.contrib.agent_builder import AgentBuilder

#2. Create Necessary Configs
config_path = 'OAI_CONFIG_LIST.json'
config_list = autogen.config_list_from_json(config_path)
default_llm_config = {
    'temperature': 0
}

#3. Initialize The Agent Builder
builder = AgentBuilder(config_path=config_path,builder_model='gpt-4-1106-preview', agent_model='gpt-4-1106-preview')

#4. Define The Task for AutoBuilder. Make sure the Task is Generic with an example.
building_task = "Find a paper on arxiv by programming, and analyze its application in some domain. For example, find a latest paper about gpt-4 on arxiv and find its potential applications in software."

#5. Building Agents
agent_list, agent_configs = builder.build(building_task, default_llm_config, coding=True)

#6. Create Multi-Agent Group Chat
group_chat = autogen.GroupChat(agents=agent_list, messages=[], max_round=12)

#7. Create Manager for Group Chat
manager = autogen.GroupChatManager(
        groupchat=group_chat, llm_config={"config_list": config_list, **default_llm_config}
    )

#8. Finally, Initiate the Chat by specifying the task.
agent_list[0].initiate_chat(manager, message="find top 4 latest Paper about GPT4 and it's implication on Cybersecurity") 
