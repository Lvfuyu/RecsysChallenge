# train features
python generate_features.py ./basic_users_features ./basic_items_features ../samples/local_samples.csv ./local_train_features.txt train

# test features
python generate_features.py ./basic_users_features ./basic_items_features ../samples/local_test_samples.csv ./local_test_features.txt test

