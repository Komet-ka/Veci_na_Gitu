import pickle


list = ["Lenka", "Honza", "Kamil", "Petra", "Lora"]

print(list)

with open('list.pickle', 'wb') as f:
    pickle.dump(list, f)

with open('list.pickle', 'rb') as f:
    list = pickle.load(f)

with open('list_text', 'w') as f:
    for line in list:
        f.write(line + '\n')
