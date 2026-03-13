# SAGE
"SAGE (Smart Assistant for General Engineering) — A personalised AI engineering assistant built to help me learn, code, and solve problems. Side project + ML learning journey."

## Setup

### Clone the repo
git clone https://github.com/YOUR_USERNAME/SAGE.git
cd SAGE

### Create virtual environment
**Windows:** python -m venv venv
**Mac:** python3 -m venv venv

### Activate virtual environment
**Windows:** venv\Scripts\activate
**Mac:** source venv/bin/activate

### Install dependencies
pip install -r requirements.txt

### Add your API key
Create a .env file and add:
GEMINI_API_KEY=your_key_here

### Run SAGE
streamlit run app/main.py