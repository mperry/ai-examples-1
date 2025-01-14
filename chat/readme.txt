
Uses Python 3.12.8, Ollama 0.5.4

To create the virtual environment:
chat> python -m venv venv

To activate the environment:
chat> venv\Scripts\activate

(all in the chat directory)
pip install requests
pip install gradio

To get the full list of packages required, freeze using pip
pip freeze >requirements.txt

One can then install all the required libraries using pip
pip install -r requirements.txt

To run use:
python chat.py


