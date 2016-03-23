
# extract samples(most are positive) from global interaction specified by time range 
#python generate_samples.py ../data/train/local/local_interactions.csv local_samples.csv 1445817600 1446422399 

# extract negative samples from impressions.csv specified by time range, samples from the last week of label week
# week time < specified time
#python generate_neg_impression.py ../data/train/online/impressions.csv local_samples.csv local_neg_samples.csv 1446422400

# concatenate two sample files
#cat local_neg_samples.csv >> local_samples.csv


# generate test file
python generate_local_test.py ../data/train/local/local_target_users.csv ../data/train/online/impressions.csv 45 local_samples.csv local_test_samples.csv
