# <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Travel%20and%20places/Star.png" alt="Star" width="25" height="25" /> **Deployed Vercel App:** [reddit-ai-one.vercel.app](https://reddit-ai-one.vercel.app) <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Hand%20gestures/Backhand%20Index%20Pointing%20Left.png" alt="Backhand Index Pointing Left" width="25" height="25" />

# RedditAI

**RedditAI** is a ***prototype*** Streamlit web app that leverages Google Gemini and the Reddit API to fetch Reddit post comments and generate AI-powered summaries or insights. It is designed for easy exploration and summarization of Reddit discussions.

## Features

- 🔍 Fetches Reddit post comments using the Reddit API (via [PRAW](https://praw.readthedocs.io/)).
- 🤖 Summarizes or analyzes Reddit threads using Google Gemini (via [agno](https://github.com/agnodice/agno)).
- 🖥️ Simple, interactive web interface built with Streamlit.
- 🛠️ Modular design for easy extension and debugging.

## How It Works

1. **User Input:** Enter a Reddit post URL in the app.
2. **Fetching Comments:** The app retrieves all comments for the post using the Reddit API.
3. **AI Summarization:** Comments are passed to a Gemini-powered agent, which generates a summary or insight.
4. **Display:** The result is shown in markdown format in the app.

## Setup

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/reddit-ai.git
cd reddit-ai
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

Dependencies include:

- `streamlit`
- `praw`
- `agno`
- `google-genai`

### 3. Configure Secrets

Create a `.streamlit/secrets.toml` file with your API keys:

```toml
CLIENT_ID = "your_reddit_client_id"
CLIENT_SECRET = "your_reddit_client_secret"
GEMINI_API_KEY = "your_gemini_api_key"
```

You can obtain Reddit API credentials from [Reddit Apps](https://www.reddit.com/prefs/apps) and Gemini API keys from Google.

### 4. Run the App

```bash
streamlit run app.py
```

## Usage

1. Open the app in your browser (Streamlit will provide a local URL).
2. Paste a Reddit post URL (e.g., `https://www.reddit.com/r/Python/comments/xxxxxx/...`).
3. Click **Summarize**.
4. View the AI-generated summary or analysis.

## Project Structure

```
reddit-ai/
├── app.py           # Streamlit app entry point
├── reddit.py        # Reddit API utilities
├── instructions.py  # (Custom instructions for the agent)
├── requirements.txt
└── README.md
```

## Code Overview

### `reddit.py`

- Handles Reddit API authentication and data fetching.
- `get_subreddit_posts`: Fetches posts from a subreddit.
- `get_post_comments`: Fetches all comments for a given post.

### `app.py`

- Sets up the Streamlit UI.
- Initializes the Gemini model and agent.
- Handles user input and displays results.

## Customization

- **Instructions:** Modify `instructions.py` to change how the agent summarizes or analyzes posts.
- **Tools:** Add more tools to the agent for extended functionality.

## Notes

- The app runs in read-only mode for Reddit.
- Ensure your API keys are kept secret and not committed to version control.

## License

MIT License. See [LICENSE](LICENSE) for details.

---

**Enjoy exploring Reddit with AI!**
