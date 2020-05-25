#!/bin/bash
# 获取按钮位置信息
source ./PointLocation.sh
HASDEVICES=`adb devices`
# 查看手机上有几个名称含有"com.versa"的包
HASINSTALL=`adb shell pm list packages com.versa ｜ grep versa | wc -l`
# 如果adb没有找到设备，给出提示
if [ "$HASDEVICES" == "List of devices attached" ]
then
    echo "请连接设备"
# 如果含有"com.versa"的包少于1个，判定手机未安装马卡龙
elif [ "$HASINSTALL" -lt 1 ]
then
    echo "请安装马卡龙"
else
    # 设置手机分辨率为1080x1920
    adb shell wm size 1080x1920
    # 设置手机dpi为480
    adb shell wm density 480
    # 去掉手机底部导航栏
    adb shell wm overscan 0,0,0,-126
    # 清除马卡龙缓存
    adb shell pm clear com.versa
    # 赋予马卡龙读存储权限
    adb shell pm grant com.versa android.permission.READ_EXTERNAL_STORAGE
    # 赋予马卡龙写存储权限
    adb shell pm grant com.versa android.permission.WRITE_EXTERNAL_STORAGE
    # 赋予马卡龙摄像头权限
    adb shell pm grant com.versa android.permission.CAMERA
    # 开启马卡龙app
    adb shell am start com.versa/com.versa.ui.SplashActivity
    # 等待app加载五秒
    sleep 5
    # 点击同意协议按钮
    adb shell input tap $ProtocolAgreementX $ProtocolAgreementY
    # 再等待十二秒，包括广告和加载时间
    sleep 12
    # 点击右上角的跳过按钮
    adb shell input tap $LabelSkipX $LabelSkipY
    # 此时已经进入主界面
fi

# 进入主界面，是其他自动化脚本的前提，需要被其他脚本引入
