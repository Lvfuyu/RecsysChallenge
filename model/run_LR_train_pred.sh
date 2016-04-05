
. ../config.sh
root_dir=..

if [ "$isOnline" == "0" ] ; then

echo 'Training...'

./liblinear/train -s 0 -c 1.3 ${root_dir}/${local_feature}/local_train_features.p

else

echo 'Testing...'


fi
