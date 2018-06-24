# Repository Structure
data: training data for this repo. 
Outputs: Processed Data
src: Source code

# Src Code functional overview
addContent.py extract Audio2Text data from xaml files and export to txt files, with text length filter applied
generateModel.py load files from local dataset and generate a Gensim Word2Vec model
keywordExtraction.py extract keywords from 
Levenshtein.py Calculate similarity between sentences based on Levenshtein distance and cosine distance from Word2Vec model
