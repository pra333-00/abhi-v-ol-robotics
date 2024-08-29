# -*- coding: utf-8 -*-

import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import random
from sklearn.metrics import confusion_matrix
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from datasets import load_dataset

# Function to show training history (if applicable)
def show_history(history):
    epochs_trained = len(history.history['loss'])
    plt.figure(figsize=(16, 6))

    plt.subplot(1, 2, 1)
    plt.plot(range(0, epochs_trained), history.history.get('accuracy'), label='Training')
    plt.plot(range(0, epochs_trained), history.history.get('val_accuracy'), label='Validation')
    plt.ylim([0., 1.])
    plt.xlabel('Epochs')
    plt.ylabel('Accuracy')
    plt.legend()

    plt.subplot(1, 2, 2)
    plt.plot(range(0, epochs_trained), history.history.get('loss'), label='Training')
    plt.plot(range(0, epochs_trained), history.history.get('val_loss'), label='Validation')
    plt.xlabel('Epochs')
    plt.ylabel('Loss')
    plt.legend()
    plt.show()

# Function to show confusion matrix
def show_confusion_matrix(y_true, y_pred, classes):
    cm = confusion_matrix(y_true, y_pred, normalize='true')

    plt.figure(figsize=(8, 8))
    sp = plt.subplot(1, 1, 1)
    ctx = sp.matshow(cm)
    plt.xticks(list(range(0, len(classes))), labels=classes)
    plt.yticks(list(range(0, len(classes))), labels=classes)
    plt.colorbar(ctx)
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
train_labels = names_to_ids(labels, classes_to_index)

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
i = random.randint(0, len(test_labels) - 1)
print('Sentence:', test_tweets[i])


know=list(classes)[test_labels[i]]
guess=list(classes)[predicted_labels[i]]
s=''
s1=''
if know==0:
  s='sadness'
elif know==1:
  s='joy'
elif know==2:
  s='love'
elif know==3:
  s='anger'
elif know==4:
  s='fear'
elif know==5:
  s='surprise'

if guess==0:
  s1='sadness'
elif guess==1:
  s1='joy'
elif guess==2:
  s1='love'
elif guess==3:
  s1='anger'
elif guess==4:
  s1='fear'
elif guess==5:
  s1='surprise'

print('True Emotion:', s)
print('Predicted Emotion:', s1)

# Show confusion matrix
show_confusion_matrix(test_labels, predicted_labels, list(classes))

lengths = [len(t.split(' ')) for t in tweets]

plt.hist(lengths, bins=len(set(lengths)))
plt.show()

plt.hist(labels, bins=11)
plt.show()
