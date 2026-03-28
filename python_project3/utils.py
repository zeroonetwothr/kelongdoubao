from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, AIMessage
from dotenv import load_dotenv
import os
load_dotenv()
llm = ChatOpenAI(
    model=os.getenv("DOUBAO_MODEL"),
    api_key=os.getenv("DOUBAO_API"),
    base_url="https://ark.cn-beijing.volces.com/api/v3"
)
memory = []
def get_chat_response(prompt, memory):
    memory.append(HumanMessage(content=prompt))
    response = llm.invoke(memory)
    memory.append(AIMessage(content=response.content))
    return response.content
# print(get_chat_response("牛顿提出过哪些知名的定律？", memory))
# print(get_chat_response("我上一个问题是什么？", memory))
