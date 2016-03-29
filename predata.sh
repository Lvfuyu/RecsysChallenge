# data preprocess
# when you fist start the project, run it

if [ ! -d ./data/train/online ]; then
mkdir -p ./data/train/online
fi

if [ ! -d ./data/train/local ]; then
mkdir -p ./data/train/local
fi

if [ ! -d ./feature_p/online ]; then
mkdir -p ./feature_p/online
fi

if [ ! -d ./feature_p/local ]; then
mkdir -p ./feature_p/local
fi

if [ ! -d ./model/online ]; then
mkdir -p ./model/online
fi

if [ ! -d ./model/local ]; then
mkdir -p ./model/local
fi

if [ ! -d ./samples/online ]; then
mkdir -p ./samples/online
fi

if [ ! -d ./samples/local ]; then
mkdir -p ./samples/local
fi

if [ ! -d ./submit/online ]; then
mkdir -p ./submit/online
fi

if [ ! -d ./submit/local ]; then
mkdir -p ./submit/local
fi

cd ./data
#sed -i '' '1d' interactions.csv # mac shell command if linux maybe sed -i '1d'
sed -i '1d' interactions.csv # mac shell command if linux maybe sed -i '1d'
mv impressions.csv interactions.csv items.csv users.csv ./train/online
mv target_users.csv ../submit/online
cd -

cd ./data/train/local
sh split.sh
cd -
