import nltk
import numpy as np
import random
import string 
import json

#import torch
#import torch.nn as nn
#from torch.utils.data import Dataset, DataLoader

from nltk import word_tokenize, sent_tokenize
from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()

intents_json = json.loads(open('intents.json').read())

all_words = []
tags = [] 
xy = []
# loop through each sentence in our intents patterns
for intent in intents_json['intents']:
    tag = intent['tag']
    # add to tag list
    tags.append(tag)
    for pattern in intent['patterns']:
        # tokenize each word in the sentence
        w = nltk.word_tokenize(pattern)
        # add to our words list
        all_words.extend(w)
        # add to xy pair  
        xy.append((w, tag))

# stem and lower each word
ignore_words = ['?', '.', '!']
all_words = [lemmatizer.lemmatize(w.lower()) for w in all_words if w not in ignore_words]
# remove duplicates and sort
all_words = sorted(set(all_words))

tags = sorted(set(tags))

class ChatDataset(Dataset):
    def __init__(self):
        self.n_samples = len(xy)
        self.x_data = [x for x, y in xy]
        self.y_data = [tags.index(y) for x, y in xy]

    # support indexing such that dataset[i] can be used to get i-th sample
    def __getitem__(self, index):
        return self.x_data[index], self.y_data[index]

    # we can call len(dataset) to return the size
    def __len__(self):
        return self.n_samples

# create train and test datasets
dataset = ChatDataset()
train_size = int(len(dataset) * 0.8)
test_size = len(dataset) - train_size
train_dataset, test_dataset = torch.utils.data.random_split(dataset, [train_size, test_size])

# data loader
train_loader = DataLoader(train_dataset, batch_size=8, shuffle=True)
test_loader = DataLoader(test_dataset, batch_size=8, shuffle=True)

# model 
input_size = len(all_words)
hidden_size = 8
output_size = len(tags)

class NeuralNet(nn.Module):
    def __init__(self, input_size, hidden_size, num_classes):
        super(NeuralNet, self).__init__()
        self.l1 = nn.Linear(input_size, hidden_size) 
        self.l2 = nn.Linear(hidden_size, hidden_size) 
        self.l3 = nn.Linear(hidden_size, num_classes)
        self.relu = nn.ReLU()
    
    def forward(self, x):
        out = self.l1(x)
        out = self.relu(out)
        out = self.l2(out)
        out = self.relu(out)
        out = self.l3(out)
        # no activation and no softmax at the end
        return out

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

model = NeuralNet(input_size, hidden_size, output_size).to(device)

# loss and optimizer
criterion = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters(), lr=0.001)  

# training loop
num_epochs = 1000
for epoch in range(num_epochs):
    for (words, labels) in train_loader:
        words = words.to(device)
        labels = labels.to(dtype=torch.long).to(device)
        
        # forward
        outputs = model(words)
        loss = criterion(outputs, labels)
        
        #backward and optimizer 
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        
    if (epoch+1) % 100 == 0:
        print (f'Epoch [{epoch+1}/{num_epochs}], Loss: {loss.item():.4f}')


print(f'final loss: {loss.item():.4f}')

data = {
"model_state": model.state_dict(),
"input_size": input_size,
"hidden_size": hidden_size,
"output_size": output_size,
"all_words": all_words,
"tags": tags
}

FILE = "data.pth"
torch.save(data, FILE)

print(f'training complete. file saved to {FILE}')
