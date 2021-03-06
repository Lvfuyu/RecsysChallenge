# define mode
# 1 for online; 0 for offline validation
#isOnline=0
isOnline=1

# define all potential directory
root=.

data=${root}/data
train_data=${data}/train
local_train_data=${train_data}/local
online_train_data=${train_data}/online

feature=${root}/feature_p
local_feature=${feature}/local
online_feature=${feature}/online

model=${root}/model
local_model=${model}/local
online_model=${model}/online

samples=${root}/samples
local_samples=${samples}/local
online_samples=${samples}/online

submit=${root}/submit
local_submit=${submit}/local
online_submit=${submit}/online
