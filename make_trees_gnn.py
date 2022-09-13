import Constants
import json
import spacy

nlp = spacy.load("en_core_web_sm")

ROOT_DIR = Constants.ROOT_DIR
SPLIT_TO_PROGRAMMED_QUESTION_PATH_TABLE = {
     'train_unbiased': str(ROOT_DIR / 'GraphVQA/questions/backup/train_balanced_programs.json'),
     'val_unbiased': str(ROOT_DIR / 'GraphVQA/questions/backup/val_balanced_programs.json'),
     'testdev': str(ROOT_DIR / 'GraphVQA/questions/backup/testdev_balanced_programs.json'),
}

programmed_question_path = SPLIT_TO_PROGRAMMED_QUESTION_PATH_TABLE["testdev"]

with open (programmed_question_path)as f:
    questions = json.load(f)

def get_dependency_tree(question):
    triples = []
    doc = nlp(question)
    #print(f"{'Node (from)-->':<15} {'Relation':^10} {'-->Node (to)':>15}\n")
    for token in doc:
        # print("{:<15} {:^10} {:>15}".format(str(token.head.text), str(token.dep_), str(token.text)))
        triples.append([str(token.head.text), str(token.dep_), str(token.text)])
    # displacy.render(doc, style='dep')
    return triples


new_questions = []
for index, row in enumerate(questions):
     question = row[1]
     dep_tree_triples = get_dependency_tree(question)
     row.append(dep_tree_triples)
     new_questions.append(row)

questions = json.dumps(new_questions)
questions_file = open(str(ROOT_DIR / "GraphVQA/questions/testdev_balanced_programs.json"), "w")
questions_file.write(questions)
questions_file.close()

