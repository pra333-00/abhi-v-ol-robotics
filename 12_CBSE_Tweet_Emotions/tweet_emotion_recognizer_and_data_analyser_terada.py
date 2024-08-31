# -*- coding: utf-8 -*-

import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import random
from sklearn.metrics import confusion_matrix
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from datasets import load_dataset
import time

print("This project involves using a self-trained model to predict emotions in tweets or messages. Then, we intend to show its performance and effectiveness in the form of a confusion matrix after testing the model on data.")
print(".\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n")
time.sleep(15)
print("A confusion matrix would show the performance of our emotion prediction model by comparing predicted labels against actual labels in a grid, i.e. how certain or confused it is.")
print(".\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n")
time.sleep(20)
print("The confusion matrix will show a bar on the right, \nwhich is a guide to how certain the model is - 0.0 to 1.0 i.e. 0 to 100% - in some emotions. \nFor example, joy and love are mutual emotions in many cases, \nand thus can cause some confusion for not only the model, \nbut sometimes even us as humans.\nIn any case, given the training of our model, \nit is still accurate, as evidenced by the high certainty \nwhen comparing the rows of true emotions to columns of predicted emotions.")
print(".\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n")
time.sleep(25)
# Function to show confusion matrix
def show_confusion_matrix(y_true, y_pred, classes):
    cm = confusion_matrix(y_true, y_pred, normalize='true')
    emotion_labels = ['sadness', 'joy', 'love', 'anger', 'fear', 'surprise']
    plt.figure(figsize=(8, 8))
    sp = plt.subplot(1, 1, 1)
    ctx = sp.matshow(cm,cmap='cividis')
    plt.xticks(list(range(0, len(classes))), labels=emotion_labels)
    plt.yticks(list(range(0, len(classes))), labels=emotion_labels)
    plt.colorbar(ctx)
    plt.figtext(0.5, 0.01, "The bar on the right is a guide to how certain the model is - 0.0 to 1.0 - in some emotions. \nFor example, joy and love are mutual emotions in many cases, and thus can cause some confusion for not only the model, \nbut sometimes even us as humans.\nIn any case, given the training of our model, it is still accurate, as evidenced by the\n high certainty when comparing the rows of true emotions to columns of predicted emotions.", ha="center", fontsize=9)
    plt.show()

# Function to get tweets and labels from data
def get_tweets(data):
    tweets = [x['text'] for x in data]
    labels = [x['label'] for x in data]
    return tweets, labels

# Function to get sequences from tweets
def get_sequences(tokenizer, tweets):
    sequences = tokenizer.texts_to_sequences(tweets)
    padded_sequences = pad_sequences(sequences, truncating='post', maxlen=50, padding='post')
    return padded_sequences

# Function to convert text labels to numeric labels
def names_to_ids(labels, classes_to_index):
    return np.array([classes_to_index.get(x) for x in labels])

# Load dataset
dataset = load_dataset("dair-ai/emotion", "split")

# Split data into training, validation, and test sets
train = dataset['train']
val = dataset['validation']
test = dataset['test']

# Get tweets and labels from training data
tweets, labels = get_tweets(train)

# Create tokenizer and fit it to training tweets
tokenizer = Tokenizer(num_words=10000, oov_token='<UNK>')
tokenizer.fit_on_texts(tweets)

# Get sequences from training tweets
padded_train_sequences = get_sequences(tokenizer, tweets)

# Convert text labels to numeric labels
classes = set(labels)
classes_to_index = dict((c, i) for i, c in enumerate(classes))
index_to_classes = dict((v, k) for k, v in classes_to_index.items())
train_labels = names_to_ids(labels, classes_to_index)
print(classes_to_index,index_to_classes)

# Load the pre-trained model
model = tf.keras.models.load_model('emotion_model.h5')

# Evaluate model on the test set
test_tweets, test_labels = get_tweets(test)
test_sequences = get_sequences(tokenizer, test_tweets)
test_labels = names_to_ids(test_labels, classes_to_index)

loss, accuracy = model.evaluate(test_sequences, test_labels)
print(f'Test loss: {loss:.3f}, Test accuracy: {accuracy:.3f}')

# Make predictions
predictions = model.predict(test_sequences)
predicted_labels = np.argmax(predictions, axis=1)

# Example prediction
j = int(input(("1. Test from dataset\n2. Test using own sentence: \n")))
if j == 1:

    i = random.randint(0, len(test_labels) - 1)
    print('Sentence:', test_tweets[i])


    know=list(classes)[test_labels[i]]
    guess=list(classes)[predicted_labels[i]]
    s = ''
    s1 = ''
    if know == 0:
      s = 'sadness'
    elif know == 1:
      s = 'joy'
    elif know == 2:
      s = 'love'
    elif know == 3:
      s = 'anger'
    elif know == 4:
      s = 'fear'
    elif know == 5:
      s = 'surprise'

    if guess == 0:
      s1 = 'sadness'
    elif guess == 1:
      s1 = 'joy'
    elif guess == 2:
      s1 = 'love'
    elif guess == 3:
      s1 = 'anger'
    elif guess == 4:
      s1 = 'fear'
    elif guess == 5:
      s1 = 'surprise'

    print('True Emotion:', s)
    print('Predicted Emotion:', s1)
elif j == 2:
    s2 = input("enter a sentence: ")
    s2_sequence = tokenizer.texts_to_sequences([s2])
    s2_padded_sequence = pad_sequences(s2_sequence, truncating='post', maxlen=50, padding='post')
    predictions_s2 = model.predict(s2_padded_sequence)
    predicted_labels_s2 = np.argmax(predictions_s2, axis=1)
    guess=predicted_labels_s2[0]
    s1=''
    if guess == 0:
      s1 = 'sadness'
    elif guess == 1:
      s1 = 'joy'
    elif guess == 2:
      s1 = 'love'
    elif guess == 3:
      s1 = 'anger'
    elif guess == 4:
      s1 = 'fear'
    elif guess == 5:
      s1 = 'surprise'
    print('Predicted Emotion:', s1)
    

# Show confusion matrix
show_confusion_matrix(test_labels, predicted_labels, list(classes))

lengths = [len(t.split(' ')) for t in tweets]

plt.hist(lengths, bins=len(set(lengths)))
plt.show()

plt.hist(labels, bins=11)
plt.show()
