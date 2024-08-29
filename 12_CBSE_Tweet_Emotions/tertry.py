# -*- coding: utf-8 -*-

import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import nlp
import random
from sklearn.metrics import confusion_matrix
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from datasets import load_dataset


# Function to show training history
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
    plt.xticks(list(range(0, 6)), labels=classes)
    plt.yticks(list(range(0, 6)), labels=classes)
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
def names_to_ids(labels):
    classes_to_index = dict((c, i) for i, c in enumerate(set(labels)))
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
train_labels = names_to_ids(labels)

# Create model
model = tf.keras.models.Sequential([
    tf.keras.layers.Embedding(10000, 16, input_length=50),
    tf.keras.layers.Bidirectional(tf.keras.layers.LSTM(20, return_sequences=True)),
    tf.keras.layers.Bidirectional(tf.keras.layers.LSTM(20)),
    tf.keras.layers.Dense(6, activation='softmax')
])

model.compile(
    loss='sparse_categorical_crossentropy',
    optimizer='adam',
    metrics=['accuracy']
)

# Train model
val_tweets, val_labels = get_tweets(val)
val_sequences = get_sequences(tokenizer, val_tweets)
val_labels = names_to_ids(val_labels)

history = model.fit(
    padded_train_sequences, train_labels,
    validation_data=(val_sequences, val_labels),
    epochs=5,
    callbacks=[
        tf.keras.callbacks.EarlyStopping(monitor='val_accuracy', patience=2)
    ]
)

# Evaluate model
test_tweets, test_labels = get_tweets(test)
test_sequences = get_sequences(tokenizer, test_tweets)
test_labels = names_to_ids(test_labels)

loss, accuracy = model.evaluate(test_sequences, test_labels)
print(f'Test loss: {loss:.3f}, Test accuracy: {accuracy:.3f}')

# Make predictions
predictions = model.predict(test_sequences)
predicted_labels = np.argmax(predictions, axis=1)

# Show confusion matrix
show_confusion_matrix(test_labels, predicted_labels, list(set(labels)))

print("Training history:")
print(history.history)
print("Test labels:", test_labels)
print("Predicted labels:", predicted_labels)
