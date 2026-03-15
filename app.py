import streamlit as st
import requests
# from agno.agent import Agent
# from agno.models.google import Gemini
# from reddit import get_post_comments
# from instructions import instructions

# --- For CLI ---
# import os
# from dotenv import load_dotenv
# load_dotenv()

# GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# model = Gemini(
#     id="gemini-1.5-flash",
#     api_key=GEMINI_API_KEY
# )

# reddit_tools = [get_post_comments]

# agent = Agent(
#     name="RedditAI",
#     model=model,
#     instructions=instructions,
#     tools=reddit_tools,
#     show_tool_calls=True,
#     read_chat_history=True,
#     markdown=True,
#     debug_mode=True
# )

# # CLI
# while True:
#     prompt = input("You: ")
#     if prompt.lower().strip() == 'exit':
#         break

#     response = agent.run(prompt)
#     print(response.content)
# --- For CLI ---

# GEMINI_API_KEY = st.secrets["GEMINI_API_KEY"]

def send_alert():
    webhook_url = st.secrets["WEBHOOK_URL"]
    payload = {
                "username": "Reddit AI",
                "embeds": [
                    {
                    "title": "Redirect Successful",
                    "description": "User was successfully redirected to RedditAI v2.0",
                    "color": 65328
                    }
                ]
            }
    res = requests.post(webhook_url, json=payload)
    if res.status_code == 204:
        print("Alert sent successfully")
    else:
        print("Failed to send alert")

def main():
    # model = Gemini(
    #     id="gemini-2.5-flash",
    #     api_key=GEMINI_API_KEY
    # )

    # reddit_tools = [get_post_comments]

    # agent = Agent(
    #     name="RedditAI",
    #     model=model,
    #     instructions=instructions,
    #     tools=reddit_tools,
    #     show_tool_calls=True,
    #     read_chat_history=True,
    #     markdown=True,
    #     debug_mode=True
    # )

    st.set_page_config(
        page_icon="🎃",
        page_title="RedditAI"
    )

    st.title("RedditAI")
    prompt = st.text_input(
        "Reddit Post URL", placeholder="https://www.reddit.com/r/...", disabled=True)
    button = st.button("Summarize", disabled=True)

    if st.button("Redirect me to new version"):
        st.link_button(label="👉 RedditAI v2.0", url="https://reddit-ai-one.vercel.app/", type="primary", use_container_width=True, help="Click here to check out the new version")
        send_alert()

    # if prompt and button:
        # with st.spinner("Fetching comments and summarizing post..."):
        #     response = agent.run(prompt)
        #     st.markdown(response.content)
    # elif button:
    #     st.info("Reddit post link pls 😑")


if __name__ == "__main__":
    main()
