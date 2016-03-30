#isOnline=1
. ../config.sh
root_dir=..

if [ "$isOnline" == "0" ] ; then

echo 'Training...'
 train model
python train_xgboost.py ${root_dir}/${local_feature}/local_train_features.p \
						${root_dir}/${local_feature}/local_test_features.p \
						./local/pred.txt

echo 'Evaluating...'
# generate submit result
python gen_submit.py ${root_dir}/${local_samples}/local_test_samples.csv \
					 ./local/pred.txt \
					 ${root_dir}/${local_submit}/pred.csv
echo 'Predicted Users Number: '$(wc -l ${root_dir}/${local_submit}/pred.csv)

# evaluation offline
cd ${root_dir}/${submit}
python score.py

else

echo 'Training...'
# train model
python train_xgboost.py ${root_dir}/${online_feature}/online_train_features.p \
						${root_dir}/${online_feature}/online_test_features.p \
						./online/pred.txt

# generate submit result
python gen_submit.py ${root_dir}/${online_samples}/online_test_samples.csv \
					 ./online/pred.txt \
					 ${root_dir}/${online_submit}/pred.csv
echo 'Predicted Users Number: '$(wc -l ${root_dir}/${online_submit}/pred.csv)
echo 'Completed!!'

fi
