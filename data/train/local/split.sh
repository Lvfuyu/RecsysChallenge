awk '$4>=1446422400{print}' ../raw_data/interactions.csv > local_ground_truth_interact.csv
awk '$4<1446422400{print}' ../raw_data/interactions.csv > local_interactions.csv
