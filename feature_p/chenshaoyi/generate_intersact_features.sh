. ../config.sh
root_dir=..

# data file 
# user.csv ${root_dir}/${online_train_data}/users.csv
# items.csv ${root_dir}/${online_train_data}/items.csv
# out_feature: ../


python chenshaoyi/get_word_intersaction.py ./basic_users_features ./basic_items_features ${root_dir}/${local_samples}/local_samples.csv word_intesect.csv 
