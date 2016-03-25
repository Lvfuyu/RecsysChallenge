#awk '$4>=1446422400{print}' ../online/interactions.csv > local_ground_truth_interact.csv
#awk '$4<1446422400{print}' ../online/interactions.csv > local_interactions.csv

. ../../../config.sh
root_dir=../../../

python generate_ground_truth.py local_ground_truth_interact.csv \
								${root_dir}/${local_submit}/ground_truth.csv \
								${root_dir}/${local_submit}/local_target_users.csv
