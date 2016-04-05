
. ../config.sh
root_dir=..

if [ "$isOnline" == "0" ] ; then

echo 'Training...'

./liblinear/train -s 0 ${root_dir}/${local_feature}/local_train_features.p lr.model
./liblinear/predict -b 1 ${root_dir}/${local_feature}/local_test_features.p lr.model ./local/pred.txt

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


fi
