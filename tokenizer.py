import os
import re 
import string
from nltk.stem import PorterStemmer
from bs4 import BeautifulSoup

def tokenizer(folder_path):
    doc_dict = {}
    pattern = "[" + re.escape(string.punctuation) + "]" 
    for filename in sorted(os.listdir(folder_path)):                    #reading directory
        with open(os.path.join(folder_path, filename), 'r') as f:
            doc = f.read()
            soup = BeautifulSoup(doc, "html.parser")
            title = soup.find('title').text.strip()                     #extracting TEXT from SGML tags
            text = soup.find('text').text.strip()                       #extracting TITLE from SGML tags
            doc_no = soup.find('docno').text.strip()                    #extracting DOCNO from SGML tags
            doc_extract = ''.join([title,text])
            punctuation_removal = re.sub(pattern, "", str(doc_extract)) #removing punctuation 
            remove_num = re.sub(r'[~^0-9]', '', punctuation_removal)    #removing numbers
            whitespace_removal = remove_num.split()                     #splitting on whitespaces
            doc_dict.update({doc_no:whitespace_removal})                #dictionary {DocNO:[pre-preprocessed tokens]}
    return doc_dict     