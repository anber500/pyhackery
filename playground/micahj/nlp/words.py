from sklearn.model_selection import train_test_split
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
import os

# sentences = """
# When you work with machine learning, one important step is to define a baseline model. This usually involves a simple model, which is then used as a comparison with the more advanced models that you want to test. In this case, you’ll use the baseline model to compare it to the more advanced methods involving (deep) neural networks, the meat and potatoes of this tutorial.
#
# First, you are going to split the data into a training and testing set which will allow you to evaluate the accuracy and see if your model generalizes well. This means whether the model is able to perform well on data it has not seen before. This is a way to see if the model is overfitting.
#
# Overfitting is when a model is trained too well on the training data. You want to avoid overfitting, as this would mean that the model mostly just memorized the training data. This would account for a large accuracy with the training data but a low accuracy in the testing data.
# """.split(".")
# sentences = [s.strip() for s in sentences]

# print(sentences)
curr_dir = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(curr_dir, 'sentiment labelled sentences',
                    'yelp_labelled.txt')
df = pd.read_csv(path, names=['sentence', 'label'], sep='\t')
print(df)

sentences = df['sentence'].values
y = df['label'].values

res = train_test_split(
    sentences,
    y,
    test_size=0.25,
    random_state=1000)
sentences_train, sentences_test, y_train, y_test = res
vectorizer = CountVectorizer()
vectorizer.fit(sentences_train)
X_train = vectorizer.transform(sentences_train)
X_test = vectorizer.transform(sentences_test)
print(X_train)
