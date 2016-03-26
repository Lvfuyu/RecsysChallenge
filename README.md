# RecsysChallenge
2016 Recsys Challenge - Job recommendation

##Code structure

* ./data *store online and offline train & test data*

* ./smaples *create train samples and test samples*

* ./feature_p *extract features according to sample files*

* ./model *train and test*

* ./submit *store submit file and offline evaluate function*

* predata.sh *线下数据划分脚本*

* config.sh *指定offline和online 定义路径*

* run_all.sh *训练和测试*

* 各个目录下的online和local文件夹分别对应线上线下的处理数据

* ./InitDat useless

##初始化Project

* git clone https://github.com/Lvfuyu/RecsysChallenge.git

* 解压后的5个csv文件放于project根目录下

* 在project根目录下sh predata.sh，启动预处理脚本，放置csv文件到相应目录位置并进行线下数据划分

* 线下local_interactions.csv位于./data/train/local/，线下ground_truth.csv和线下测试用户local_target_users.csv位于./submit/local/

##数据说明

**interaction.csv**

* 大约8,826,678条交互数据
* 时间戳范围[1439966982, 1447023598]
* UTC时间范围[2015/8/19 06:49:42, 2015/11/8 22:59:58] *11/8为周日*
