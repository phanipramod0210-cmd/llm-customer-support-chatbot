import json
from pathlib import Path
DATA_DIR = Path('data')
with open(DATA_DIR/'faqs.json') as f:
    faqs = json.load(f)

def answer(query):
    q = query.lower()
    candidates = [d for d in faqs if any(w in d['text'].lower() for w in q.split())]
    if candidates:
        return candidates[0]['text']
    return 'Sorry, I do not know the answer. (Set OPENAI_API_KEY for full LLM responses)'

if __name__ == '__main__':
    while True:
        q = input('Question> ').strip()
        if not q: break
        print('Answer:', answer(q))
