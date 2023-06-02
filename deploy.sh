#!/bin/bash

# 获取脚本所在目录
script_dir=$(dirname "$(readlink -f "$0")")

# 将工作目录更改为脚本所在目录
cd "$script_dir" || exit

# 检查Git仓库是否有更新
git remote update
pwd


AWS_URl="406687643298.dkr.ecr.ap-northeast-2.amazonaws.com/quizmate-academic"
RELATEST_TIME=$(date '+%Y%m%d%H%M%S')
IMAGE_NAME=quizmate-academic:$RELATEST_TIME

REMOTE_URL="${AWS_URl}:${RELATEST_TIME}"
docker build -t $IMAGE_NAME .
echo "${IMAGE_NAME}"
echo "${REMOTE_URL}"
docker tag $IMAGE_NAME $REMOTE_URL
docker push $REMOTE_URL



