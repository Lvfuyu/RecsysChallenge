
# start the entire train procedure
cd ./samples
sh run_samples.sh
cd -
cd ./feature_p
sh run_gen_feature.sh
cd -
cd ./model
sh run_train_pred.sh
cd -