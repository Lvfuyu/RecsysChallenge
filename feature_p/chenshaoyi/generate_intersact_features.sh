. ../../config.sh
root_dir=../..

# data file 
# user.csv ${root_dir}/${online_train_data}/users.csv
# items.csv ${root_dir}/${online_train_data}/items.csv
# out_feature: ../

if [ "$isOnline" == "0" ] ; then
python get_word_intersaction.py ../basic_users_features ../basic_items_features ${root_dir}/${local_samples}/local_samples.csv ../local/local_train_features.p 
python get_word_intersaction.py ../basic_users_features ../basic_items_features ${root_dir}/${local_samples}/local_test_samples.csv ../local/local_test_features.p 

else

python get_word_intersaction.py ../basic_users_features ../basic_items_features ${root_dir}/${online_samples}/online_samples.csv ../online/online_train_features.p 
python get_word_intersaction.py ../basic_users_features ../basic_items_features ${root_dir}/${online_samples}/online_test_samples.csv ../online/online_test_features.p

fi
