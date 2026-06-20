import spacy

nlp = spacy.load("en_core_web_sm")

with open("Resume.txt") as file1:
  text1 = file1.read()

with open("Big_Projects\Big_Projects\Resume vs Job Macher\Job_Description.txt") as file2:
  text2 = file2.read()


print("\n".ljust(22, "="))
print(f"RESUME VS JOB MATCHER")
print("".center(21, "="))

skills = ["python","pandas","spacy","nltk","regex","git","github","sql","machine learning","named entity recognition","ner","sentiment analysis","pos tagging","natural language processing","nlp","data annotation","quality assurance","json","csv","text normalization","tokenization","lemmatization","information extraction","text datasets","numpy","textblob"
]  

doc1 = nlp(text1)
doc2 = nlp(text2)

found_skills = set()
for word in doc1:
  if word.text.lower() in skills:
    found_skills.add(word.text.lower())

required_skills = set()
for word in doc2:
  if word.text.lower() in skills:
    required_skills.add(word.text.lower())

# Finding the matching skills between the resume and the job_description:
matched_skills = found_skills & required_skills

print(f"\nMatched Skills:")
for skill in matched_skills:
  print(f".{skill}")

# Finding the missing skills in the resume:
missing_skills = required_skills - found_skills

print(f"\nMissing Skills:")
for skill in missing_skills:
  print(f".{skill}")


score = (len(matched_skills) / len(required_skills)) * 100
print(f"\nMatch Score: {score:.2f}%")
