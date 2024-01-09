markdown
Copy code
<!-- Project Title -->
<h1 align="center">WebQA using Large Language Models and FAISS</h1>

<!-- Project Description -->
<p align="center">
  A project that leverages large language models from OpenAI to answer questions based on the content of given websites. The system utilizes FAISS for efficient similarity search, allowing users to ask questions related to the provided URLs.
</p>

<!-- GIF Showcase -->
<p align="center">
  <img src="path/to/your/gif.gif" alt="GIF Showcase" width="80%">
</p>

<!-- Project Features -->
<h2 align="center">Features</h2>

- **WebQA:** Utilizes large language models to answer questions based on the content of provided websites.
- **Efficient Search:** Employs FAISS for efficient similarity search among the processed data.
- **User-Friendly Interface:** Accepts URLs as input and provides answers to user queries.
- **Streamlit Output:** Utilizes Streamlit to showcase the output of the project in an interactive and visually appealing manner.

<!-- Getting Started -->
<h2 align="center">Getting Started</h2>

### Installation

Clone the repository:
```bash
$ git clone https://github.com/karthiknair-19/LLM_text_summariser.git
$ cd LLM_text_summariser
```
Create a virtual environment (optional but recommended):

```bash
$ python -m venv venv
$ source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

Install the necessary dependencies:
```bash
$ pip install -r requirements.txt
```

Create a .env file in the project root and paste your API key:
```bash
OPENAI_API_KEY=your_openai_api_key
```
Replace your_openai_api_key with your actual OpenAI API key.

Install the python-dotenv library (if not already installed):
```bash
$ pip install python-dotenv
```
Load the virtual environment (if not already activated) and run the application:
```bash
$ source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
$ streamlit run app.py
```

Visit http://localhost:8501 in your web browser to interact with the project output.

<!-- Libraries Used -->
<h2 align="center">Libraries Used</h2>
<p align="center">
  <img alt="OpenAI Logo" src="https://upload.wikimedia.org/wikipedia/commons/4/4d/OpenAI_Logo.svg" height="50" />
  <img alt="FAISS Logo" src="https://github.com/facebookresearch/faiss/blob/master/faiss-logo.png?raw=true" height="50" />
  <img alt="Streamlit Logo" src="https://assets.streamlit.io/images/brand/streamlit-logo-secondary-colormark-darktext.png" height="50" />
  <img alt="Langchain Logo" src="https://example.com/langchain_logo.png" height="50" />
  <!-- Add more libraries as needed -->
</p>
<!-- License -->
<h2 align="center">License</h2>
<p align="center">
  This project is licensed under the [GNU General Public License v3.0](LICENSE).
</p>
```
