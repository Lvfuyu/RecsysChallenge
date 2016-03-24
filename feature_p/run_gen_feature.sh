#isOnline=1

. ../config.sh

if [ "isOnline" == "0" ] ; then
# train features
python generate_features.py ./basic_users_features ./basic_items_features ../samples/local_samples.csv ./local_train_features.txt train

# test features
python generate_features.py ./basic_users_features ./basic_items_features ../samples/local_test_samples.csv ./local_test_features.txt test

else

# train features
python generate_features.py ./basic_users_features ./basic_items_features \
							../samples/online/samples.csv \
							./online/train_features.p train

# test features
python generate_features.py ./basic_users_features ./basic_items_features \
							../samples/online/test_samples.csv \
							./online/test_features.p test

fi