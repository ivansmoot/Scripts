#!/bin/bash
# 将传入的第一个参数作为安装路径
INSTALLAPK=${1}
# 如果没有传入参数，则设置默认路径
if [ ! -n "${INSTALLAPK}" ]
then
    INSTALLAPK="/Users/yifan/Downloads/*.apk"
fi
# 将安装与写入log过程作为方法
getlog(){
    # 这些命令不要加反引号，否则会将命令输出执行一遍，即提示command not find
    adb install ${INSTALLAPK}
    echo "安装成功"
    cd /Users/yifan/Desktop
    rm -rf log.log
    echo "删除桌面log"
    touch log.log
    echo "创建log成功"
    # 这里的activity名问方达要
    adb shell am start com.versa/com.versa.ui.SplashActivity
    echo "启动成功"
    echo "正在记录日志"
    # >前不要有管道符，否则无法写入
    adb logcat | grep versa > log.log
}
HASDEVICES=`adb devices`
# 查看手机上有几个名称含有"com.versa"的包
HASINSTALL=`adb shell pm list packages com.versa ｜ grep versa | wc -l`
# 如果adb没有找到设备，给出提示
if [ "$HASDEVICES" == "List of devices attached" ]
then
    echo "请连接设备"
# 如果含有"com.versa"的包为4个，判定手机安装马卡龙，进行卸载操作，并进入方法步骤
elif [ "$HASINSTALL" -eq 4 ]
then
    adb shell pm uninstall com.versa
    echo "卸载成功"
    getlog ${INSTALLAPK}
# 手机未安装马卡龙则直接进入方法步骤
else
    getlog ${INSTALLAPK}
fi

# 自动卸载手机已安装的马卡龙app
# 安装apk文件，默认是"下载"文件夹下的.apk结尾的文件，也可以由脚本参数传入，指定安装
# 删除桌面的"log.log"日志文件，并重新创建一个"log.log"文件
# 记录日志，并将日志中所有包含"versa"的内容写入桌面的"log.log"文件
