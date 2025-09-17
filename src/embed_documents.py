from pathlib import Path
import json
DATA_DIR = Path('data')
DATA_DIR.mkdir(exist_ok=True)
docs = ['Return policy: You can return within 30 days.','Refunds take 5-7 business days.','Shipping: standard shipping is 5-10 days.']
out = DATA_DIR/'faqs.json'
faqs = [{'id':i,'text':t} for i,t in enumerate(docs)]
with open(out,'w') as f:
    json.dump(faqs,f,indent=2)
print('Wrote', out)
