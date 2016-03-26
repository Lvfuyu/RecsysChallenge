
# start the entire train procedure
cd ./samples
echo 'Sampling...'
# 生成 训练样本（user,item,target） 和 测试样本(user,item)
sh run_samples.sh
echo 'Sample End'
cd -

cd ./feature_p
echo 'Generating Feature File...'
# 根据样本提取特征，生成特征文件
sh run_gen_feature.sh
echo 'Generate Feature End'
cd -

cd ./model
echo 'Training and Testing...'
# 读取特征文件，线下调参和线上提交
# 最终的预测文件位于./submit/local 或者 ./submit/online
sh run_train_pred.sh
echo 'Over'