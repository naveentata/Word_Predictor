# Word Predictor

A simple LSTM network to predict next word in a given sequential list of words from a sentence.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

Dependencies

```
Tensorflow 
Keras (Backend Tensorflow)
```
### Model Summary
```
_________________________________________________________________
Layer (type)                 Output Shape              Param #   
=================================================================
lstm_1 (LSTM)                (None, 3, 400)            643200    
_________________________________________________________________
dropout_1 (Dropout)          (None, 3, 400)            0         
_________________________________________________________________
lstm_2 (LSTM)                (None, 400)               1281600   
_________________________________________________________________
dropout_2 (Dropout)          (None, 400)               0         
_________________________________________________________________
dense_1 (Dense)              (None, 142)               56942     
=================================================================
```

### Installing

A step by step series of examples that tell you how to get a development env running

Run the Main network

```
python lstm_word.py
```

Tuneable seeds and parameters

```
Update seed_length to custom length
Update Data corpus to requisite data, ie Conversational dialogues are great starter packs.
```


## And coding style 

All code is UTF 8 encoded 
(Built in a Pycharm Virtual Env)


## Built With

* [Tensorflow](https://www.tensorflow.org/) - A Machine learning framework
* [Keras](https://keras.io/) - Higher level library to use tensorflow based models.


## Contributing
Pull requests are always welcome. Current focus is to improve the LSTM layers to get better accuray over randomized data set. Tests to carry out to check if the data is overfitting in this case, as a result of which the model accuracy is higher than expected. All other pull requests can focus on Issues from the repo. 

## Versioning
Git

## Authors

* **Rahul Krishnan** - *Programmer* - [Rahul Krishnan](https://github.com/rahulkrishnan98)
* **Naveen Tata** - *Programmer* - [Naveen Tata](https://github.com/naveentata)
* **Venkat Gopalakrishnan** - *Programmer* - [Venkat](https://github.com/gvenkat07)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details


