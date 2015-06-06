# AutoCompletion
Project is to complete a given sentence 
3 Files are provided.
1. Model.py - This will train the model with training tweets and dump the model in pickel files. Should be run with utility.py
2. utility.py contains important functions for text cleaning, and predictions. Better algos can be further integrated without touching Model.py and Predict. 
3. Predict.py uses utility.py functions and predict the new statement. First it load the model from picke. Make sure the saving and loding directory are same. 
Then it takes new statement from command line and then give 1-2 words for prediction. 

Performance:

For 10000 tweets, it take 40 second to train the model on i3, 2GHz processor. 

For prediction, it takes 15 mili-sec on an average on same system. 
