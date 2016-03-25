#isOnline=1
. ../config.sh

cur_dir=..

if [ "$isOnline" = "0" ] ; then

# extract samples(most are positive) from global interaction specified by time range 
python generate_samples.py ${cur_dir}/${local_train_data}/local_interactions.csv \
						   ./local/local_samples.csv \
						   ${cur_dir}/${online_train_data}/items.csv \
						   1446422399 28

# extract negative samples from impressions.csv specified by time range, samples from the last week of label week
# week time < specified time
python generate_neg_impression.py ${cur_dir}/${online_train_data}/impressions.csv \
								  ./local/local_samples.csv \
								  ./local/local_neg_samples.csv \
								  ${cur_dir}/${online_train_data}/items.csv \
								  1446422400

# concatenate two sample files
cat ./local/local_neg_samples.csv >> ./local/local_samples.csv
wc -l ./local/local_samples.csv

# generate test file
python generate_test.py ${cur_dir}/${local_submit}/local_target_users.csv \
						${cur_dir}/${online_train_data}/impressions.csv \
						./local/local_samples.csv \
						./local/local_test_samples.csv \
						${cur_dir}/${online_train_data}/items.csv \
						45

wc -l ./local/local_test_samples.csv

else

# positive sample
python generate_samples.py ${cur_dir}/${online_train_data}/interactions.csv \
						   ./online/samples.csv \
						   ${cur_dir}/${online_train_data}/items.csv \
						   1446422400 28
# negative sample
python generate_neg_impression.py ${cur_dir}/${online_train_data}/impressions.csv \
								  ./online/samples.csv \
								  ./online/neg_samples.csv \
								  ${cur_dir}/${online_train_data}/items.csv \
								  1447027200

# concatenate two sample files
cat ./online/neg_samples.csv >> ./online/samples.csv
wc -l ./online/samples.csv

# generate test file
python generate_test.py ${cur_dir}/${online_submit}/target_users.csv \
						${cur_dir}/${online_train_data}/impressions.csv \
						./online/samples.csv \
						./online/test_samples.csv \
						${cur_dir}/${online_train_data}/items.csv \
						46

wc -l ./online/test_samples.csv

fi