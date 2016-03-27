#isOnline=1

. ../config.sh
root_dir=..

if [ "$isOnline" == "0" ] ; then

echo 'Generate train features...'
# train features
python merge_features.py ./basic_users_features \
						 ./basic_items_features \
						 ${root_dir}/${local_samples}/local_samples.csv \
						 ./local/local_train_features.p \
						 train

echo 'Generate test features...'
# test features
python merge_features.py ./basic_users_features \
						 ./basic_items_features \
						 ${root_dir}/${local_samples}/local_test_samples.csv \
						 ./local/local_test_features.p \
						 test

else

echo 'Generate train features...'
# train features
python merge_features.py ./basic_users_features \
						 ./basic_items_features \
						 ${root_dir}/${online_samples}/samples.csv \
						 ./online/train_features.p \
						 train

echo 'Generate test features...'
# test features
python merge_features.py ./basic_users_features \
						 ./basic_items_features \
						 ${root_dir}/${online_samples}/test_samples.csv \
						 ./online/test_features.p \
						 test

fi