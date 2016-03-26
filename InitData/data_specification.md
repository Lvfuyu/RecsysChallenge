预测目标
----
预测下周 用户会交互的工作，只要三种类型满足一种就ok

数据表说明
----
impression.csv
	用户id	
	年	
	周	
	推荐的职位

interaction.csv
	用户id
	职位id	
	交互类型	
	交互时间

	交互类型1 点击 2 收藏 3 回复
	用户的一些属性置为NULL或unknown

Users.csv
	id
	jobrole
	career_level
	...

items.csv
	id
	title
	career_level
	...
	active_during_test // 估计线上预测才会用

备注
--
线上测试数据的用户都包含在训练数据user表中
impression.csv week与interaction.csv create_at 对应
2015年[34,46]

interaction.csv 
8,826,678左右交互数据
时间最小值 1439966982 北京时间 2015/8/19 14:49:42 标准时间 2015/8/19 06:49:42
时间最大值 1447023598 北京时间 2015/11/9 6:59:58  标准时间 2015/11/8 22:59:58 周日 

User.csv 一共有1500000用户
item.csv 一共1358098职位
