. ../../config.sh
root_dir=../..

# data file 
# user.csv ${root_dir}/${online_train_data}/users.csv
# items.csv ${root_dir}/${online_train_data}/items.csv
# out_feature: ../


python get_basic_item_feature.py ${root_dir}/${online_train_data}/items.csv ../basic_items_features
python get_basic_user_feature.py ${root_dir}/${online_train_data}/users.csv ../basic_users_features
