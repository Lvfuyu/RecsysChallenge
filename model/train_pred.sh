#isOnline=1
. ../config.sh
cur_dir=..

if [ "$isOnline" == "0" ] ; then
# train model
python train_xgboost.py ${cur_dir}/${local_feature}/local_train_features.p \
						${cur_dir}/${local_feature}/local_test_features.p \
						./local/pred.txt

# generate submit result
python gen_submit.py ${cur_dir}/${local_samples}/local_test_samples.csv \
					 ./local/pred.txt \
					 ${cur_dir}/${local_submit}/pred.csv

# evaluation offline
cd ${cur_dir}/${submit}
python score.py

else

# train model
python train_xgboost.py ${cur_dir}/${online_feature}/train_features.p \
						${cur_dir}/${online_feature}/test_features.p \
						./online/pred.txt

# generate submit result
python gen_submit.py ${cur_dir}/${online_samples}/test_samples.csv \
					 ./online/pred.txt \
					 ${cur_dir}/${online_submit}/pred.csv

fi