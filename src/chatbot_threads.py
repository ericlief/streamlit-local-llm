from threading import current_thread
import streamlit as st
from openai import OpenAI
from streamlit.runtime.state.session_state_proxy import SessionStateProxy
import os
import json
import glob

def load_chat_history():
    history_file_dir = "/Users/liefe/Projects/ericlief/chatbot/history/"
    files = glob.glob(os.path.join(history_file_dir, "*.json"))
    threads = {"Default": []}
    # if os.path.exists(history_file):
    for file in files:
        with open(file, "r") as fp:
            thread = os.path.splitext(os.path.basename(file))[0]
            threads[thread] = json.load(fp)
 
    return threads

def save_thread_history(thread):
    history_file = f"/Users/liefe/Projects/ericlief/chatbot/history/{thread}.json"
    with open(history_file, "w") as fp:
        json.dump(st.session_state.threads[thread], fp)
 
client = OpenAI(
    base_url = "http://localhost:8080",
    api_key="local")

st.set_page_config(page_title="Local LLM Chatbot", layout="wide")
# st.title()
# -------------------------------
# Initialize session state
# ------------------------------
if "threads" not in st.session_state:
    st.session_state.threads = load_chat_history()

    # st.session_state.threads = {'Default': []}
if "current_thread" not in st.session_state:
    st.session_state.current_thread = "Default"
# if "history" not in st.session_state:
#     st.session_state.history = []

# -------------------------------
# Sidebar for thread navigation
# -------------------------------
with st.sidebar:
    st.title("🧵 Threads")
    for thread_name in st.session_state.threads.keys():
        if st.button(thread_name, key=f"load_{thread_name}"):
            st.session_state.current_thread = thread_name
    st.markdown("---")
    new_thread_name = st.text_input("➕ Create New Thread", key="new_thread_input")
    if st.button("Create"):
        if new_thread_name and new_thread_name not in st.session_state.threads:
            st.session_state.threads[new_thread_name] = []
            st.session_state.current_thread = new_thread_name
    st.markdown("---")
    st.caption("Selected thread: **" + st.session_state.current_thread + "**")        


st.title("🧠 Local Chat Interface")
current = st.session_state.current_thread
history = st.session_state.threads[current]
# with st.form("chat_form", clear_on_submit=True):
    # user_input = st.text_input("Type your message:", placeholder="Type and press Enter")
    # submitted = st.form_submit_button("Send")

if prompt := st.chat_input("Your message"):
    history.append({"role": "user", "content": prompt})

    # st.chat_message("user").write(prompt)

    # st.chat_message(name="user", message=user_input)
    # msg1 = st.chat_message("user")
    # msg1.write(user_input)
    # if submitted and user_input.strip():
    # messages = [{"role": "user", "content": prompt}]
    response = client.chat.completions.create(
        model="T3Q-qwen2.5.Q4_K_M.gguf",
        messages=history,
        temperature=2 # test
        # stream=True,
    )
    print(response)
    reply = response.choices[0].message.content
     # Add to state
    history.append({"role": "assistant", "content": reply})

    save_thread_history(current)

    # if reply:
    #     st.chat_message("assistant").write(reply)
    # msg2 = st.chat_message("assistant")
    # msg2.write(reply)

   
    # for chunk in response:
    #     if chunk.choices[0].delta.content is not None:

    # for chunk in client.chat.completions.create(
    #     model="llama3-8b-8192",
    #     messages=messages,
    #     stream=True,
    # ):
        # if chunk.choices[0].delta.content is not None:

# for role, msg in history:
#     st.markdown(f"**{role.title()}** \n{msg}", unsafe_allow_html=True)


for item in history:
    role = item["role"]
    message = item["content"]
    st.chat_message(role).write(message)
    # if "user" in msg:
    #     st.chat_message("user").write(msg["us"])
    # else:
    #     st.chat_message("assistant").write(msg[1])


# for prompt, reply in reversed(st.session_state.history):
#     st.markdown(f"**You:** {prompt}")
#     st.markdown(f"**Assistant:**: {reply}", unsafe_allow_html=True)

