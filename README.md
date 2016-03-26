# RecsysChallenge
2016 Recsys Challenge - Job recommendation

##Code structure

* ./data **store online and offline train & test data**
* ./smaples	**create train samples and test samples**
* ./feature_p	**extract features according to sample files**
* ./model	**train and test**
* ./submit	**store submit file and offline evaluate function**
* predata.sh	**线下数据划分脚本**
* config.sh	**指定offline和online 定义路径**
* run_all.sh	**训练和测试**
* 各个目录下的online和local文件夹分别对应线上线下的处理数据
* **暂时的只有题目给出的user和item属性特征，处理代码在毅博那**
* ./InitDat	**useless**

##初始化Project

* git clone https://github.com/Lvfuyu/RecsysChallenge.git
* 解压后的5个csv文件放于./data/目录下
* 在project根目录下sh predata.sh，启动预处理脚本，放置csv文件到相应目录位置并进行线下数据划分
* 线下local_interactions.csv位于./data/train/local/，线下ground_truth.csv和线下测试用户local_target_users.csv位于./submit/local/
* 处理后interactions.csv 和 local_interactions.csv 已删除第一行表头说明，直接从数据开始，其他表没作处理

##训练和测试

* ./config.sh指定运行模式0（offline）和1（online）
* sh run_all.sh
* 启动脚本会先后进入./samples, ./features_p, ./model目录执行相应目录下脚本
* 需要在./features_p/放入特征文件
* 需要在./model/放入xgboost可执行文件

##数据说明

**interaction.csv**

* 8,826,678条交互数据
* 时间戳范围[1439966982, 1447023598]
* UTC时间范围[2015/8/19 06:49:42, 2015/11/8 22:59:58] *11/8为周日*
* 周次范围[34, 45]

**impressions.csv**

* 周次[34, 46] *46为线上预测周，从1开始计数*
