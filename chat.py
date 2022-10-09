import random
import json
import pickle
import torch
import numpy as np
from model import NeuralNet
from nltk_utils import bag_of_words, tokenize

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

with open('intents.json', 'r') as json_data:
    intents = json.load(json_data)

FILE = "data.pth"
data = torch.load(FILE)

input_size = data["input_size"]
hidden_size = data["hidden_size"]
output_size = data["output_size"]
all_words = data['all_words']
tags = data['tags']
model_state = data["model_state"]

model = NeuralNet(input_size, hidden_size, output_size).to(device)
model.load_state_dict(model_state)
model.eval()
filename = 'finalized_model.sav'
bot_name = "PharmDroid"
rf = pickle.load(open(filename, 'rb'))



q_counter=0
flag=0
q_list = [
    "Are you having any shivering?",
    "Are you feeling itchy in your body?",
    "Do you have cough?",
    "Are you feeling like vomiting or had to vomit?",
    "Do you have acidity?",
    "Do you have fever?",
    "Are you feeling fatigued?",
    "Are you having digestion issues?",
    "Do you feel weakness in your limbs?",
    "have you suffered with unnatural weight gain?",
    "Is your skin yellow in colour?",
    "Is your urine dark in colour?",
    "Are you having discomfort in your bladder?"    
]

a=[]
def dis_conv(s):
	if s==1:
		return "Common Cold"
	if s==2:
		return "Allergies"
	if s==3:
		return "Jaundice"
	if s==4:
		return "Malaria"
	if s==5:
		return "Chicken Pox"
	if s==6:
		return "Dengue"
	if s==7:
		return "Tuberculosis"
	if s==8:
		return "Thyroid"
	if s==9:
		return "Fungal"


def get_response_(sentence):
    global q_counter
    global q_list
    global a
    global flag
    if(q_counter==0):
        flag=1
        q_counter+=1
        return "I will ask you a few symptoms.Answer me if you are having it \n"+q_list[q_counter-1]
    if(q_counter==1):
        res=1 if sentence.lower()=="yes" else 0
        a.append(res)
        q_counter+=1
        if a[0]=="bad":
            flag=0
        return q_list[q_counter-1]
    if(q_counter==2):
        res=1 if sentence.lower()=="yes" else 0
        a.append(res)
        q_counter+=1
        return q_list[q_counter-1]
    if(q_counter==3):
        res=1 if sentence.lower()=="yes" else 0
        a.append(res)
        q_counter+=1
        return q_list[q_counter-1]
    if(q_counter==4):
        res=1 if sentence.lower()=="yes" else 0
        a.append(res)
        q_counter+=1
        return q_list[q_counter-1]
    if(q_counter==5):
        res=1 if sentence.lower()=="yes" else 0
        a.append(res)
        q_counter+=1
        return q_list[q_counter-1]
    if(q_counter==6):
        res=1 if sentence.lower()=="yes" else 0
        a.append(res)
        q_counter+=1
        return q_list[q_counter-1]
    if(q_counter==7):
        res=1 if sentence.lower()=="yes" else 0
        a.append(res)
        q_counter+=1
        return q_list[q_counter-1]
    if(q_counter==8):
        res=1 if sentence.lower()=="yes" else 0
        a.append(res)
        q_counter+=1
        return q_list[q_counter-1]
    if(q_counter==9):
        res=1 if sentence.lower()=="yes" else 0
        a.append(res)
        q_counter+=1
        return q_list[q_counter-1]
    if(q_counter==10):
        res=1 if sentence.lower()=="yes" else 0
        a.append(res)
        q_counter+=1
        return q_list[q_counter-1]
    if(q_counter==11):
        res=1 if sentence.lower()=="yes" else 0
        a.append(res)
        q_counter+=1
        return q_list[q_counter-1]
    if(q_counter==12):
        res=1 if sentence.lower()=="yes" else 0
        a.append(res)
        q_counter+=1
        flag=2
        return q_list[q_counter-1]
    if(flag==2):
        res=1 if sentence.lower()=="yes" else 0
        a.append(res)
        q_counter+=1
        flag=0
        a=np.array(a)
        print(a)
        a=a.reshape(1, -1)
        result=rf.predict(a)
        print(result)
        return dis_conv(result[0])


def bot_response(sentence):
    sentence = tokenize(sentence)
    X = bag_of_words(sentence, all_words)
    X = X.reshape(1, X.shape[0])
    X = torch.from_numpy(X).to(device)

    output = model(X)
    _, predicted = torch.max(output, dim=1)

    tag = tags[predicted.item()]

    probs = torch.softmax(output, dim=1)
    prob = probs[0][predicted.item()]
    if prob.item() > 0.25:
        for intent in intents['intents']:
            if tag == intent["tag"]:
                return f"{random.choice(intent['responses'])}"
    else:
        return f"I do not understand..."

import regex as re
def chatter(sentence):
    global flag
    match = re.search(r'test', sentence)
    if sentence == "quit":     
        res="Byye!"
    elif match or flag>=1:
        res=get_response_(sentence)
    else:
        res=bot_response(sentence)
    return res