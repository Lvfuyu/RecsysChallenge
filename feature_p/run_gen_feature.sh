#isOnline=1

. ../config.sh
cur_dir=..

if [ "$isOnline" == "0" ] ; then
# train features
python generate_features.py ./basic_users_features \
							./basic_items_features \
							${cur_dir}/${local_samples}/local_samples.csv \
							./local/local_train_features.p \
							train

# test features
python generate_features.py ./basic_users_features \
							./basic_items_features \
							${cur_dir}/${local_samples}/local_test_samples.csv \
							./local/local_test_features.p \
							test

else

# train features
python generate_features.py ./basic_users_features \
							./basic_items_features \
							${cur_dir}/${online_samples}/samples.csv \
							./online/train_features.p \
							train

# test features
python generate_features.py ./basic_users_features \
							./basic_items_features \
							${cur_dir}/${online_samples}/test_samples.csv \
							./online/test_features.p \
							test

fi