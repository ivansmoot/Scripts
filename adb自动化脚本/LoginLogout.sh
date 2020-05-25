#!/bin/bash

# 点击右下角"我的"按钮进入个人主页
adb shell input tap $MyX $MyY
# 等待一秒，否则点击太快了，页面加载跟不上
sleep 1
# 点击"点击登陆"按钮
adb shell input tap $TapLoginX $TapLoginY
# 再等一秒
sleep 1
# 同意协议
adb shell input tap $IKnowItX $IKnowItY
# 输入正确账号
adb shell input tap $InputPhoneNumberX $InputPhoneNumberY
adb shell input text $Account
# 点击箭头按钮
adb shell input tap $GoForwardX $GoForwardY
sleep 2
# 输入正确密码
adb shell input tap $InputPasswordX $InputPasswordY
adb shell input text $Password
# 再点箭头按钮
adb shell input tap $GoForwardX $GoForwardY
sleep 2
# 此时应登陆成功
