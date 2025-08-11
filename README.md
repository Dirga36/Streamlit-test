## **CurhatIn AI** is a Streamlit-based chatbot application designed to act as a friendly, empathetic listener for users to share their feelings and problems. It uses the **DeepSeek** language model through **OpenRouter** to generate human-like responses tailored to emotional support and empathy.

---

## Features
- Interactive chat interface powered by **Streamlit**
- Empathetic AI responses based on predefined conversational style
- Multiple modes of interaction (Best Friend, Close Friend, Psychologist)
- Chat history persistence using `st.session_state`
- Ability to reset conversations
- Privacy-focused — no data storage

---

## Requirements
- Python 3.8+
- Dependencies:
  - `streamlit`
  - `langchain-core`
  - `langchain-community`

Install dependencies:
```bash
pip install streamlit langchain-core langchain-community
```

---

## Configuration
This script uses **DeepSeek** via OpenRouter.  
You must configure:
- `DEEPSEEK_API_KEY` — Your API key
- `DEEPSEEK_API_BASE` — API base URL (`https://openrouter.ai/api/v1`)

---

## Usage
Run the Streamlit app:
```bash
streamlit run app.py
```

Once running:
1. Select a chat mode from the sidebar
2. Start typing your problem or story in the chat input
3. Receive empathetic responses from CurhatIn AI
4. Use the "Reset Percakapan" button to restart

---

Contributing
============
If you want to contribute to a project and make it better, your help is very welcome. Contributing is also a great way to learn more about social coding on Github, new technologies and and their ecosystems and how to make constructive, helpful bug reports, feature requests and the noblest of all contributions: a good, clean pull request.

### How to make a clean pull request

Look for a project's contribution instructions. If there are any, follow them.

- Create a personal fork of the project on Github.
- Clone the fork on your local machine. Your remote repo on Github is called `origin`.
- Add the original repository as a remote called `upstream`.
- If you created your fork a while ago be sure to pull upstream changes into your local repository.
- Create a new branch to work on! Branch from `develop` if it exists, else from `master`.
- Implement/fix your feature, comment your code.
- Follow the code style of the project, including indentation.
- If the project has tests run them!
- Write or adapt tests as needed.
- Add or change the documentation as needed.
- Squash your commits into a single commit with git's [interactive rebase](https://help.github.com/articles/interactive-rebase). Create a new branch if necessary.
- Push your branch to your fork on Github, the remote `origin`.
- From your fork open a pull request in the correct branch. Target the project's `develop` branch if there is one, else go for `master`!
- …
- If the maintainer requests further changes just push them to your branch. The PR will be updated automatically.
- Once the pull request is approved and merged you can pull the changes from `upstream` to your local repo and delete
your extra branch(es).

And last but not least: Always write your commit messages in the present tense. Your commit message should describe what the commit, when applied, does to the code – not what you did to the code.

---

## Notes
- This app is **not** designed to store user data
- For serious mental health issues, users are advised to seek **professional help**
- The AI is intended for casual, friendly conversation and emotional support only

---

## License
This project is licensed under the MIT License.
