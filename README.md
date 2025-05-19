# TextLens - An NLP (Natural Language Processor) Text Analyzer
This app, using FastAPI, accepts raw text and returns the following: 
- Tokenized words
- POS tags
- Named entities

##Example input:
"In 2, Stanford University researchers studied climate trends in California." 

## To Run: 
uvicorn main:app --reload