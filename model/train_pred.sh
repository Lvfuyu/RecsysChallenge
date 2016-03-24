#isOnline=1
. ../config.sh

if [ "isOnline" == "0" ] ; then
# train model
python train_xgboost.py ../feature_p/local_train_features.txt ../feature_p/local_test_features.txt \
						./pred.txt

# generate submit result
python gen_submit.py ../samples/local_test_samples.csv ./pred.txt ../submit/pred.csv

# evaluation offline
cd ../submit
python score.py

else

# train model
python train_xgboost.py ../feature_p/online/train_features.p ../feature_p/online/test_features.p \
						./online/pred.txt

# generate submit result
python gen_submit.py ../samples/online/test_samples.csv ./online/pred.txt ../submit/online/pred.csv

fi