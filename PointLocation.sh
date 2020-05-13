# 本来的想法是，获取设备分辨率，然后根据分辨率去算按钮的位置，但是由于安卓手机底部导航栏高度不同，dpi也不一致等问题，
# 导致这样计算是无法统一按钮位置的，所以注释掉了，改成了统一设置手机的分辨率、dpi和导航栏
## 分辨率
#ResolutionX=`adb shell wm size | grep 'Override size' | awk -F " " '{print $3}' | awk -F "x" '{print $1}'`
#ResolutionY=`adb shell wm size | grep 'Override size' | awk -F " " '{print $3}' | awk -F "x" '{print $2}'`
#if [ ! -n "${ResolutionX}" ]
#then
#    ResolutionX=`adb shell wm size | grep 'Physical size' | awk -F " " '{print $3}' | awk -F "x" '{print $1}'`
#    ResolutionY=`adb shell wm size | grep 'Physical size' | awk -F " " '{print $3}' | awk -F "x" '{print $2}'`
#fi

## 协议同意按钮 729 1422
#ProtocolAgreementX=`echo "scale=0;($ResolutionX*0.6731)/1" | bc `
#ProtocolAgreementY=`echo "scale=0;($ResolutionY*0.6603)/1" | bc `

# 协议同意按钮
ProtocolAgreementX=729
ProtocolAgreementY=1422

# 标签跳过按钮
LabelSkipX=972
LabelSkipY=141

# 主页"我的"按钮
MyX=967
MyY=1851

# "点击登陆"按钮
TapLoginX=877
TapLoginY=510

# 用户协议"我知道了"按钮
IKnowItX=534
IKnowItY=1524

# "请输入手机号"文本框
InputPhoneNumberX=265
InputPhoneNumberY=583

# "前进"按钮
GoForwardX=919
GoForwardY=865

# "请输入密码"文本框
InputPasswordX=215
InputPasswordY=620

# 登陆账号密码
Account=17863977623
Password=miss1186285865

# 首页加号
IndexPlusX=545
IndexPlusY=1813

# 所有图片
AllPhotoX=969
AllPhotoY=342

# 样片一
FirstSampleX=414
FirstSampleY=333

# 样片一Inpainting起始位置
FirstSampleInpaintingStartX=562
FirstSampleInpaintingStartY=1016

# 样片一Inpainting终点位置
FirstSampleInpaintingEndX=760
FirstSampleInpaintingEndY=860

# 一级菜单换背景
ChangeBGIn1X=352
ChangeBGIn1Y=1570

# 第一张背景缩略图
BGThumbnail1X=875
BGThumbnail1Y=1623

# 打勾确认的勾
NikeX=1007
NikeY=1850

# 右上角完成按钮
CompleteX=996
CompleteY=80

# 发布页发布按钮
PublishX=779
PublishY=1738
