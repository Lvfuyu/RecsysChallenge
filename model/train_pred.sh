# train model
#python train_xgboost.py ../feature_p/local_train_features.txt ../feature_p/local_test_features.txt ./pred.txt

# generate submit result
#python gen_submit.py ../samples/local_test_samples.csv ./pred.txt ../submit/pred.csv

# evaluation offline
cd ../submit
python score.py
