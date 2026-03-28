import streamlit as st
from utils import get_chat_response
from langchain_core.messages import AIMessage
st.title("💬 克隆豆包")
with st.sidebar:
    openai_api_key = st.text_input("请输入API Key：", type="password")
    st.markdown("[火山引擎 API Key](https://console.volcengine.com/ark/region:ark+cn-beijing/model?groupType=ModelGroups&vendor=Bytedance&view=DEFAULT_VIEW)")
if "memory" not in st.session_state:
    st.session_state["memory"] = []
if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {
            "role": "ai",
            "content": "你好，我是你的 AI 助手，有什么可以帮你的吗？"
        }
    ]
    st.session_state["memory"].append(
        AIMessage(content="你好，我是你的 AI 助手，有什么可以帮你的吗？")
    )
for message in st.session_state["messages"]:
    st.chat_message(message["role"]).write(message["content"])
prompt = st.chat_input()
if prompt:
    if not openai_api_key:
        st.info("请输入你的 API Key")
        st.stop()
    st.session_state["messages"].append(
        {"role": "human", "content": prompt}
    )
    st.chat_message("human").write(prompt)
    with st.spinner("AI 正在思考中，请稍等..."):
        response = get_chat_response(prompt, st.session_state["memory"])
    st.session_state["messages"].append(
        {"role": "ai", "content": response}
    )
    st.chat_message("ai").write(response)
