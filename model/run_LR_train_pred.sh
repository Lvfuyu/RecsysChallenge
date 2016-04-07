
. ../config.sh
root_dir=..

if [ "$isOnline" == "0" ] ; then

echo 'Training...'

./liblinear/train -s 0 -c 0.6 -w1 5 ${root_dir}/${local_feature}/local_train_features.p ./liblinear/lr.model
./liblinear/predict -b 1 ${root_dir}/${local_feature}/local_test_features.p ./liblinear/lr.model ./liblinear/lr_pred.txt
python ./liblinear/conver2pred.py ./liblinear/lr_pred.txt ./local/pred.txt

echo 'Evaluating...'
# generate submit result
python gen_submit.py ${root_dir}/${local_samples}/local_test_samples.csv \
                     ./local/pred.txt \
                     ${root_dir}/${local_submit}/pred.csv
echo 'Predicted Users Number: '$(wc -l ${root_dir}/${local_submit}/pred.csv)

# evaluation offline
cd ${root_dir}/${submit}
python score.py

else

echo 'Testing...'

./liblinear/train -s 0 -c 0.6 -w1 5 ${root_dir}/${online_feature}/online_train_features.p ./liblinear/lr_online.model
./liblinear/predict -b 1 ${root_dir}/${online_feature}/online_test_features.p ./liblinear/lr_online.model ./liblinear/lr_pred.txt
python ./liblinear/conver2pred.py ./liblinear/lr_pred.txt ./online/pred.txt

echo 'Evaluating...'
# generate submit result
python gen_submit.py ${root_dir}/${online_samples}/online_test_samples.csv \
                     ./online/pred.txt \
                     ${root_dir}/${online_submit}/pred.csv
echo 'Predicted Users Number: '$(wc -l ${root_dir}/${online_submit}/pred.csv)


fi
