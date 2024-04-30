#Importing the necessary libraries

import glob
!pip install scikit-learn
from sklearn.feature_extraction.text import tfidVectorizer
from sklearn.metrics.pairwise import cosine_similarity

#Importing all the files and vectorizing them

folder_path = "/path/to/folder"

student_files = glob.glob(os.path.join(folder_path, "*.txt"))

# student_files=[doc for doc in os.listdir() if doc.endswith(.txt)]

student_notes=[open(_file,encoding='utf-8').read() for _file in student_files]

vectors=vectorize(student_notes)
s_vectors=list(zip(student_files,vectors))


#Function for vectorizing the file contents

def vectorize(text):
    return TfidVectorizer().fit_transform(text).toarray()

#Function for finding similarity between two file contents

def similarity(doc1,doc2):
    return cosine_similarity([doc1,doc2])

#Function for finding the plagiarism percentage in one file comparing with all the files in the database

plagiarism_results=set()
def check_plagiarism():
    global s_vectors
    for student_a,text_vector_a in s_vectors:
        new_vectors=s_vectors.copy() #all changes to be made in copy
        current_index=new_vectors.index([student_a,text_vector_a)]) #storing index from the values
        del new_vectors[current_index] #to avoid compare same files
        for student_b,text_vector_b in new_vectors: #compare 1 file with every
            sim_score=similarity(text_vector_a,text_vector_b)[0][1] #range 0-1
            student_pair=(student_a,student_b) #storing filenames from above comparison
            score=(student_pair[0],student_pair[1],sim_score)
            plagiarism_results.add(score)
        return plagiarism_results

#Displaying the results

for data in check_plagiarism():
    print(data)
