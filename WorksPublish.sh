#!/bin/bash

# 将该测试用例的过程日志，写在当前文件夹下的WorksPublish.log文件中
rm -rf WorksPublish.log
touch WorksPublish.log
adb logcat "*:W" | grep versa > WorksPublish.log &

# 使用该脚本进入app主界面
source ./Get2MainInterface.sh
# 进行登陆操作
source ./LoginLogout.sh

# 点击首页加号
adb shell input tap $IndexPlusX $IndexPlusY
sleep 3
# 输入返回键操作
adb shell input keyevent 4
# 重新点击首页加号
adb shell input tap $IndexPlusX $IndexPlusY
sleep 2
# 点击相机icon
adb shell input tap $PhotoInTemplateRecommendationPageX $PhotoInTemplateRecommendationPageY
sleep 1
# 点击拍照
adb shell input tap $ShootButtonX $ShootButtonY
sleep 3
# 点击完成
adb shell input tap $CompleteX $CompleteY
sleep 5
# 点击发布
adb shell input tap $PublishX $PublishY
# 点击首页加号
adb shell input tap $IndexPlusX $IndexPlusY
sleep 2
# 点击"所有图片"
adb shell input tap $AllPhotoX $AllPhotoY
sleep 1
# 点击样片一
adb shell input tap $FirstSampleX $FirstSampleY
sleep 5
# 做一个Inpainting
adb shell input swipe $FirstSampleInpaintingStartX $FirstSampleInpaintingStartY $FirstSampleInpaintingEndX $FirstSampleInpaintingEndY 2000
sleep 5
# 点击换背景
adb shell input tap $ChangeBGIn1X $ChangeBGIn1Y
sleep 1
# 点击第一个背景
adb shell input tap $BGThumbnail1X $BGThumbnail1Y
sleep 1
# 打勾确认
adb shell input tap $NikeX $NikeY
sleep 1
# 点击完成
adb shell input tap $CompleteX $CompleteY
sleep 5
# 点击发布
adb shell input tap $PublishX $PublishY

# 清理刚刚写入日志的进程
ps | grep 'adb logcat' | grep -v 'grep' | awk -F " " '{print $1}' | xargs kill
sleep 10
# 恢复手机导航栏
adb shell wm overscan 0,0,0,-0
# 恢复手机分辨率
adb shell wm size reset
# 恢复手机dpi
adb shell wm density reset
