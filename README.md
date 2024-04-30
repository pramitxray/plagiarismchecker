# Plagiarism Checker

This project develops a plagiarism detection tool designed to analyze and compare textual content across multiple documents. The tool leverages natural language processing techniques to quantify the similarity between documents using a vector space model. The core functionality is built around extracting text features through TF-IDF vectorization and assessing document similarity with cosine similarity metrics. This allows for the identification of potential plagiarism by evaluating how closely the content of one document resembles another.

Technologies Used:

~ Python: The primary programming language used for implementing the plagiarism checker. <br>
~ scikit-learn: A machine learning library in Python utilized for feature extraction (TF-IDF) and similarity measurement (cosine similarity). <br>
~ Glob: A Python module used for file handling to dynamically read text files from a directory.
