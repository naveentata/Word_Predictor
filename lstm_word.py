import re
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout
from keras.layers import LSTM
from keras.utils import np_utils
import numpy as np

def predictor(seed_input):
    seed_len = 3 #seed length
    data = """All the world's a stage,
    And all the men and women merely players;
    They have their exits and their entrances,
    And one man in his time plays many parts,
    His acts being seven ages. At first, the infant,
    Mewling and puking in the nurse's arms.
    Then the whining schoolboy, with his satchel
    And shining morning face, creeping like snail
    Unwillingly to school. And then the lover,
    Sighing like furnace, with a woeful ballad
    Made to his mistress' eyebrow. Then a soldier,
    Full of strange oaths and bearded like the pard,
    Jealous in honor, sudden and quick in quarrel,
    Seeking the bubble reputation
    Even in the cannon's mouth. And then the justice,
    In fair round belly with good capon lined,
    With eyes severe and beard of formal cut,
    Full of wise saws and modern instances;
    And so he plays his part. The sixth age shifts
    Into the lean and slippered pantaloon,
    With spectacles on nose and pouch on side;
    His youthful hose, well saved, a world too wide
    For his shrunk shank, and his big manly voice,
    Turning again toward childish treble, pipes
    And whistles in his sound. Last scene of all,
    That ends this strange eventful history,
    Is second childishness and mere oblivion,
    Sans teeth, sans eyes, sans taste, sans everything. """

    dict={}
    words=re.findall(r"[\w']+|[.,!?;]", data) #split sentence to words
    index=0
    all = []
    for k in words:
        all.append(k.lower())
    del words [:]
    words = all

    for i in words:
        if(i==',' or i=='.' or i=='!' or i=='?' or i==';'):
            words[index]=0
        index+=1
    words=(list(filter(lambda a: a != 0, words)))

    uniq = list(set(words))

    word_2_num = {}
    num_2_word = {}
    for index, item in enumerate(uniq):
        word_2_num[item]=index
        num_2_word[index]= item

    x = []
    y = []
    allw = []
    for i  in words:
        allw.append(word_2_num[i])
    del words[:]
    words = allw
    for i in range(len(words)-seed_len):
        x.append(words[i:i+seed_len])
        y.append(words[i+seed_len])

    X = np.array(x)
    X = np.reshape(X,(len(x),seed_len,1))
    y = np_utils.to_categorical(y)
    model = Sequential()
    model.add(LSTM(400, input_shape=(X.shape[1], X.shape[2]), return_sequences=True))
    model.add(Dropout(0.2))
    model.add(LSTM(400))
    model.add(Dropout(0.2))
    model.add(Dense(y.shape[1], activation='softmax'))

    model.compile(loss='mean_squared_error' , optimizer='adam',metrics=["accuracy"])

    # history=model.fit(X, y, epochs=500, batch_size=100,shuffle=True,verbose=1)

    #model.save_weights('SavedModelMa.h5')

    model.load_weights('SavedModelMa.h5')
    encoded = seed_input
    encoded=encoded.split("+")
    for i in range(len(encoded)):
        encoded[i]=(word_2_num[encoded[i]])
    enc = np.array(encoded)
    encoded = np.reshape(enc,(1,3,1))
    y_pred = np.argmax(model.predict(encoded, verbose=0))
    return (num_2_word[y_pred])
