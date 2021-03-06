NOTE: This is work-in-progress. Collaborative NLP project as part of FrauenLoop ML course in summer 2020

## Predicting the Helpfulness of Stackoverflow Answers

### Project & Objective

#### *What if Stack Overflow provided its users with a prediction of how helpful the user's answer is likely going to be to the community?*

Most aspiring developers, analysts, and data scientists depend on and owe much of their learning to **online fora** where experienced coders can answer questions posed by more junior professionals and learners. According to Stack Overflow’s annual Developer Survey 2019, each month, about **50 million people visit Stack Overflow** to learn, share, and build their careers. Stack Overflow, consequently, is a powerful tool to expand knowledge and self-improve. By extension, the **quality of the answers** provided by the Stack Overflow community makes a big difference to **users' progress**. 

The **purpose** of this project was to **develop a model** that would provide users on Stack Overflow with an **advance estimate** of how helpful their answer to a question is going to be to other users. Past questions, answers and answer scores were used to train a model that would predict if a new answer was likely to receive a **bad**, **good** or **great** score. 

Example of Stack Overflow question and tags |
:-------------------------:|
![](https://raw.githubusercontent.com/HDMax93/Predicting-Helpfulness-Of-Stackoverflow-Answers/master/reports/figures/StackOverflow_Question_Tag.jpg) |

Example of a downvoted Stack Overflow answer | Example of an upvoted Stack Overflow question
:-------------------------:|:-------------------------:
![](https://raw.githubusercontent.com/HDMax93/Predicting-Helpfulness-Of-Stackoverflow-Answers/master/reports/figures/StackOverflow_BadQuestion.png)  |  ![](https://raw.githubusercontent.com/HDMax93/Predicting-Helpfulness-Of-Stackoverflow-Answers/master/reports/figures/StackOverflow_GoodAnswer.jpg)

**The project objectives were to**:

- **Empower users** to edit and improve their answers before publishing them through live predictions, to **maximize their usefulness** to the community.
- **Improve the understanding** of what factors make a high quality answer, to **educate users** on being as helpful as possible to the community.

Beyond Stack Overflow, there are many use cases across online help fora that would benefit from such a live prediction/rating of answers.

### Key insights

1. Using **Gradient Boosting Classifier** for the **three-class classification**, an **accuracy of 0.51** was reached, leaving much room for improvement.
2. Contrary to intial assumptions, the text data consisting of answers, questions and answer tags could not sufficiently help differentiate between a bad, good and great answer.
3. **Additional data** and **features** are needed to provide **predictions** on the quality of user answers with a **high accuracy**.

### Data

- The data for this project was retrieved using **Google BigQuery API**. Based on a dataset containing all Stack Overflow questions and answers between **May 2019** and **May 2020**, an equal amount of bad (answer score < 0), good (answer score of 1-6) and great (answer score of 7+) answers were retrieved, resulting in a dataset with **30,0000 observations**.
- You can **learn more about the dataset** and explore it using SQL [here](https://console.cloud.google.com/marketplace/product/stack-exchange/stack-overflow?project=frauenloop-nlp-2020&folder=&organizationId=). 

### Navigating this repo

- [Requirements](https://github.com/HDMax93/Predicting-Helpfulness-Of-Stackoverflow-Answers/blob/master/requirements.txt): Before starting your project, make sure to set up a project environment and to install all the required packages for the project. 
- You will find the relevant code to execute in the [source folder](src/):
    - [data retrieval](src/data_retrieval_and_sampling.py): If you would like to go through the process of retrieving the original dataset yourself, you will find the code in this file. You will also need to follow these steps to set up a Google BigQuery:
        1. Set up an account on [Google Cloud Platform](https://console.cloud.google.com/).
        2. Follow [steps 1-4](https://cloud.google.com/bigquery/docs/quickstarts/quickstart-client-libraries#client-libraries-install-python) on using client libraries.
        3. Place the JSON file (see step b) with your key in your directory [here](data/raw) and name it "GoogleBigQuery_key.json".
    **Alternatively**, just download the **final sample** dataset [here](https://drive.google.com/file/d/1ve6gzOKgJhdESAv2MLImbqZRi4VsSL5q/view?usp=sharing) and place it [here](data/raw) in your repository. If you use this dataset, you will not need to execute the data_retrieval_and_sampling.py file, simply start by directly running the [preprocessing.py script](src/preprocessing.py) instead.
    - data exploration: The data was explored iteratively throughout the data retrieval, preprocessing and modeling process, so scripts to explore the data are contained throughout the py-scripts. Graphs are saved in the [reports/figures](reports/figures) folder.

    *Distribution of Stack Overflow answer scores*
    <p align="center">
    <img src="https://raw.githubusercontent.com/HDMax93/Predicting-Helpfulness-Of-Stackoverflow-Answers/master/reports/figures/stackoverflow_answerscore_distribution.png" width="450"/> </p>
    
    
    - [data manipulation](src/preprocessing.py): Run this script to preprocess the data you retrieved using Google BigQuery API or that you downloaded.
    - [feature extraction](src/feature_extraction.py): This file contains the script for testing if the features are extracted as desired, using the [feature extraction helper functions and classes](src/common_utils/feature_helpers) in the [common utils folder](src/common_utils). At the moment, the following features are used in the model:
        - **ngrams/TF-IDF**: A statistical measure that indicates how important a word is to a document in a corpus of text. The importance increases proportionally to the number of times a word appears in the document but is offset by the frequency of the word in the entire corpus.
        - a simple **wordcount** of the length of the Stack Overflow answer 
        - a **similarity score** that measures the extent to which the question asked and the answer provided are similar.
        - an indication of whether or not the answer asked contains one of the **top 50 tags** on Stack Overflow.
    - [model training](src/modeling.py): You will find the script for choosing, training and hypertuning the model here.
- [final model](models): If you execute the above scripts, your final model will be stored in this place. If you would like to download the final model directly, you can do so by clicking on [this link](DOWNLOAD LINK HERE).
- [notebooks](notebooks): This folder contains some exploratory notebooks created in the process of finding the model.

### Next steps

This project remains work-in-progress. Here are some of the next steps I will be working on:

1. **Enhancing the data quality**: Thinking about different sampling strategies as well as additional or better data to retrieve as the basis to train the model.
2. **Generating more features**: Trying additional techniques, such as using a pre-trained or self-trained models for word embeddings, to create additional features.
3. **Deploying the model**: Putting a pilot of the model into production.

### Giving feedback

Do you have questions, did you spot mistakes or would like to provide feedback on improving the model? Please [reach out to me](mailto:henriekemax@googlemail.com?subject=[Feedback-On-GitHub-Stackoverflow-Project]), I would love to hear and learn from you!

### Acknowledgements 

This project was part of a Machine Learning course hosted by [FrauenLoop](https://www.frauenloop.org/).
Huge thanks goes to the wonderful hosts and mentors of the course, [Samantha Edds](https://github.com/samanthaedds) and [Laura Fernández Gallardo](https://github.com/laufergall), who generously shared their time and expertise with us.
Many thanks also to my class mates, for creating a great atmosphere for co-learning and for asking many interesting questions that helped us grow, and of course to the brilliant FrauenLoop community!

![You rock](https://michellecarlslund.com/wp-content/uploads/2018/02/you-rock.jpg)