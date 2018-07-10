# Repository Structure
data: training data for this repo.

Outputs: Processed Data

src: Source code

# Src Code functional overview
'addContent.py' extract Audio2Text data from xaml files and export to txt files, with text length filter applied

'generateModel.py' load files from local dataset and generate a Gensim Word2Vec model

'keywordExtraction.py' extract keywords 

'Levenshtein.py' Calculate similarity between sentences based on Levenshtein distance and cosine distance from Word2Vec model

# Files not uploaded
Files Cannot be released:

Internal Audio2Text transcript file: 'data/audio_transcript'

Processed audio2text file: 'Outputs/Audio2Text'

Link Internal Audio2Text transcript with abstracts: 'Outputs/csv_Input', 'Outputs/csv_Output'

Files too large to be uploaded to Github, They can be found on Sogou Lab:

Gensim Word2Vec Model file: 'data/Model'

Sogou Corpus Data, 2.~ GB: 'data/Corpus/sogou_corpus.dat'

Processed Sogou Corpus Data: 'data/Sogou'

Filtered Sogou News Corpus, eliminated Ads: 'Outputs/sogou', 'Outputs/Training_Set,' 'Outputs/Revised_Corpus'

WiP: 'doc2vec_tg/'