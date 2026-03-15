import streamlit as st
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

    st.button(label="👉 RedditAI v2.0", type="primary", use_container_width=True, on_click=lambda: st.page_link("https://reddit-ai-one.vercel.app/"), help="Click here to check out the new version")

    # if prompt and button:
        # with st.spinner("Fetching comments and summarizing post..."):
        #     response = agent.run(prompt)
        #     st.markdown(response.content)
    # elif button:
    #     st.info("Reddit post link pls 😑")


if __name__ == "__main__":
    main()
