# ##### Copyright 2019 The TensorFlow Authors.

#@title Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import tensorflow as tf

import numpy as np
import os
import time
import urllib
from http.server import BaseHTTPRequestHandler,HTTPServer

path_to_file = tf.keras.utils.get_file('KTSlgmXCNv.txt', 'https://storage.googleapis.com/file-in.appspot.com/files/KTSlgmXCNv.txt')

text = open(path_to_file, 'rb').read().decode(encoding='utf-8')

vocab = sorted(set(text))


char2idx = {u:i for i, u in enumerate(vocab)}
idx2char = np.array(vocab)

text_as_int = np.array([char2idx[c] for c in text])

seq_length = 100
examples_per_epoch = len(text)//(seq_length+1)

char_dataset = tf.data.Dataset.from_tensor_slices(text_as_int)

sequences = char_dataset.batch(seq_length+1, drop_remainder=True)


def split_input_target(chunk):
    input_text = chunk[:-1]
    target_text = chunk[1:]
    return input_text, target_text

dataset = sequences.map(split_input_target)

# Batch size
BATCH_SIZE = 64

BUFFER_SIZE = 10000

dataset = dataset.shuffle(BUFFER_SIZE).batch(BATCH_SIZE, drop_remainder=True)

dataset

vocab_size = len(vocab)

embedding_dim = 256

rnn_units = 1024


# In[92]:


def build_model(vocab_size, embedding_dim, rnn_units, batch_size):
  model = tf.keras.Sequential([
    tf.keras.layers.Embedding(vocab_size, embedding_dim,
                              batch_input_shape=[batch_size, None]),
    tf.keras.layers.GRU(rnn_units,
                        return_sequences=True,
                        stateful=True,
                        recurrent_initializer='glorot_uniform'),
    tf.keras.layers.Dense(vocab_size)
  ])
  return model


# In[93]:


model = build_model(
  vocab_size = len(vocab),
  embedding_dim=embedding_dim,
  rnn_units=rnn_units,
  batch_size=BATCH_SIZE)

for input_example_batch, target_example_batch in dataset.take(1):
  example_batch_predictions = model(input_example_batch)


sampled_indices = tf.random.categorical(example_batch_predictions[0], num_samples=1)
sampled_indices = tf.squeeze(sampled_indices,axis=-1).numpy()

def loss(labels, logits):
  return tf.keras.losses.sparse_categorical_crossentropy(labels, logits, from_logits=True)

example_batch_loss  = loss(target_example_batch, example_batch_predictions)


model.compile(optimizer='adam', loss=loss)

checkpoint_dir = './training_checkpoints'
print(checkpoint_dir)
checkpoint_prefix = os.path.join(checkpoint_dir, "ckpt_{epoch}")

checkpoint_callback=tf.keras.callbacks.ModelCheckpoint(
    filepath=checkpoint_prefix,
    save_weights_only=True)

EPOCHS=30
tf.train.latest_checkpoint(checkpoint_dir)



model = build_model(vocab_size, embedding_dim, rnn_units, batch_size=1)

model.load_weights(tf.train.latest_checkpoint(checkpoint_dir))

model.build(tf.TensorShape([1, None]))

def generate_text(model, start_string, num_chars):
  num_generate = num_chars
  print('line 125')
  # Converting our start string to numbers (vectorizing)
  input_eval = [char2idx[s] for s in start_string]
  input_eval = tf.expand_dims(input_eval, 0)

  # Empty string to store our results
  text_generated = []

  # Low temperatures results in more predictable text.
  # Higher temperatures results in more surprising text.
  # Experiment to find the best setting.
  temperature = 0.3
  print('line 137')

  # Here batch size == 1
  model.reset_states()
  print('line 141')
  print(input_eval)
  for i in range(num_generate):
      # print('line 143 i='+str(i))
      predictions = model(input_eval)
      # print('line 145 i='+str(i))
      predictions = tf.squeeze(predictions, 0)
      # print('line 147 i='+str(i))

      # using a categorical distribution to predict the character returned by the model
      predictions = predictions / temperature
      predicted_id = tf.random.categorical(predictions, num_samples=1)[-1,0].numpy()
      # print('line 152 i='+str(i))

      # We pass the predicted character as the next input to the model
      # along with the previous hidden state
      input_eval = tf.expand_dims([predicted_id], 0)
      # print('line 157 i='+str(i))

      text_generated.append(idx2char[predicted_id])

  return (start_string + ''.join(text_generated))

def get_and_return(request):
  # start = request.args['text']
  start = u"i think 1231231231231232213312"
  print(start)
  start = urllib.parse.unquote(start)
  generated = generate_text(model, start_string=str(start), num_chars=50)

  print(generated)

  generated = generated.replace('\\n', '\n')
  generated = generated.replace('\\x', ' ')

  #really bad words
  generated = generated.replace('retard', 'r****d')
  generated = generated.replace('cunt', 'c**t')
  generated = generated.replace('nigg', 'n***')
  generated = generated.replace('fag', 'f*g')

  print(generated)
  return (generated)

# get_and_return('')
