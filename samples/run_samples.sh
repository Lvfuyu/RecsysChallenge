#isOnline=1
. ../config.sh

root_dir=..

if [ "$isOnline" = "0" ] ; then

echo 'Create samples from interactions...'
# extract samples(most are positive) from global interaction specified by time range 
python generate_samples.py ${root_dir}/${local_train_data}/local_interactions.csv \
						   ./local/local_samples.csv \
						   ${root_dir}/${online_train_data}/items.csv \
						   1446422399 28

echo 'Create samples from impressions...'
# extract negative samples from impressions.csv specified by time range, samples from the last week of label week
# week time < specified time
python generate_neg_impression.py ${root_dir}/${online_train_data}/impressions.csv \
								  ./local/local_samples.csv \
								  ./local/local_neg_samples.csv \
								  ${root_dir}/${online_train_data}/items.csv \
								  1446422399

# concatenate two sample files
cat ./local/local_neg_samples.csv >> ./local/local_samples.csv
echo 'Total Train Sample Number:' $(wc -l ./local/local_samples.csv)

echo 'Create test samples...'
# generate test file
python generate_test.py ${root_dir}/${local_submit}/local_target_users.csv \
						${root_dir}/${online_train_data}/impressions.csv \
						./local/local_samples.csv \
						./local/local_test_samples.csv \
						${root_dir}/${online_train_data}/items.csv \
						45

echo 'Total Test Sample Number:' $(wc -l ./local/local_test_samples.csv)

else

#echo 'Create samples from interactions...'
## positive sample
#python generate_samples.py ${root_dir}/${online_train_data}/interactions.csv \
#						   ./online/online_samples.csv \
#						   ${root_dir}/${online_train_data}/items.csv \
#						   1447027199 28
#
#echo 'Create samples from impressions...'
## negative sample
#python generate_neg_impression.py ${root_dir}/${online_train_data}/impressions.csv \
#								  ./online/online_samples.csv \
#								  ./online/online_neg_samples.csv \
#								  ${root_dir}/${online_train_data}/items.csv \
#								  1447027199
#
## concatenate two sample files
#cat ./online/online_neg_samples.csv >> ./online/online_samples.csv
#echo 'Total Train Sample Number:' $(wc -l ./online/online_samples.csv)
#
echo 'Create test samples...'
# generate test file
python generate_test.py ${root_dir}/${online_submit}/target_users.csv \
						${root_dir}/${online_train_data}/impressions.csv \
						${root_dir}/${online_train_data}/interactions.csv \
                        ./online/online_test_samples.csv \
						${root_dir}/${online_train_data}/items.csv \
						46
#./online/online_samples.csv \
echo 'Total Test Sample Number:' $(wc -l ./online/online_test_samples.csv)

fi
