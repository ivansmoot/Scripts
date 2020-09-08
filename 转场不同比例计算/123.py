import glob
import xml.dom.minidom

transitionsXmls = sorted(glob.glob('./*.xml'))  # 读所有xml的相对路径名

thisXmlName = transitionsXmls[0][2:-4]  # 截取第一个xml的文件名
_9to16Name = thisXmlName + '9v16.xml'  # 需要生成的新9比16文件名
_1to1Name = thisXmlName + '1v1.xml'  # 需要生成的新1比1文件名
_4to3Name = thisXmlName + '4v3.xml'  # 需要生成的新4比3文件名
_3to4Name = thisXmlName + '3v4.xml'  # 需要生成的新3比4文件名

DOMTree9to16 = xml.dom.minidom.parse(thisXmlName + ".xml")  # 将这个xml文件生成一棵dom树，因为后面要进行多次保存，否则会被覆盖
DOMTree1to1 = xml.dom.minidom.parse(thisXmlName + ".xml")
DOMTree4to3 = xml.dom.minidom.parse(thisXmlName + ".xml")
DOMTree3to4 = xml.dom.minidom.parse(thisXmlName + ".xml")
storyboard9to16 = DOMTree9to16.documentElement  # storyboard也创建多份，下方注释里有xml的格式，storyboard是其中一个节点名
storyboard1to1 = DOMTree1to1.documentElement
storyboard4to3 = DOMTree4to3.documentElement
storyboard3to4 = DOMTree3to4.documentElement

x = float(storyboard9to16.getAttribute("sceneWidth"))  # x必是1280，因为设计说给的都是这个版本的
y = float(storyboard9to16.getAttribute("sceneHeight"))  # y必是720
_9to16Width = "720"  # 预设一下不同比例的宽和高
_9to16Height = "1280"
_1to1Width = "720"
_1to1Height = "720"
_4to3Width = "960"
_4to3Height = "720"
_3to4Width = "720"
_3to4Height = "960"
_9to16X = round(int(_9to16Width) / x, 4)  # 计算不同比例要乘的系数，保留四位小数精确一点
_9to16Y = round(int(_9to16Height) / y, 4)
_1to1X = round(int(_1to1Width) / x, 4)
_1to1Y = round(int(_1to1Height) / y, 4)
_4to3X = round(int(_4to3Width) / x, 4)
_4to3Y = round(int(_4to3Height) / y, 4)
_3to4X = round(int(_3to4Width) / x, 4)
_3to4Y = round(int(_3to4Height) / y, 4)

animations9to16 = storyboard9to16.getElementsByTagName("animation")  # animation创建多份，不同比例区分开，这是个节点名
animations1to1 = storyboard1to1.getElementsByTagName("animation")
animations4to3 = storyboard4to3.getElementsByTagName("animation")
animations3to4 = storyboard3to4.getElementsByTagName("animation")
tracks9to16 = storyboard9to16.getElementsByTagName("track")  # track也创建多份，不同比例区分开，也是个节点名
tracks1to1 = storyboard1to1.getElementsByTagName("track")
tracks4to3 = storyboard4to3.getElementsByTagName("track")
tracks3to4 = storyboard3to4.getElementsByTagName("track")


def create9to16():
    storyboard9to16.setAttribute("sceneWidth", _9to16Width)  # 修改storyboard节点里的sceneWidth和sceneHeight
    storyboard9to16.setAttribute("sceneHeight", _9to16Height)
    for animation9to16 in animations9to16:  # 循环三个animation节点
        if animation9to16.getAttribute("paramName") == 'transX':  # 判断是X轴和Y轴
            keys = animation9to16.getElementsByTagName("key")  # 找到key节点
            for key in keys:  # 循环里面所有的key节点，三块分开的
                old_value = float(key.getAttribute("value"))  # 获取key节点里面value的值
                new_value = str(round(old_value * _9to16X, 1))  # 计算新值
                key.setAttribute("value", new_value)  # set这个值
        if animation9to16.getAttribute("paramName") == 'transY':  # transY同理
            keys = animation9to16.getElementsByTagName("key")
            for key in keys:
                old_value = float(key.getAttribute("value"))
                new_value = str(round(old_value * _9to16Y, 1))
                key.setAttribute("value", new_value)
    for track9to16 in tracks9to16:  # 修改track节点的width和height
        track9to16.setAttribute("width", _9to16Width)
        track9to16.setAttribute("height", _9to16Height)
    with open(_9to16Name, 'w') as f:  # 保存xml文件
        DOMTree9to16.writexml(f, encoding='utf-8')


def create1to1():
    storyboard1to1.setAttribute("sceneWidth", _1to1Width)
    storyboard1to1.setAttribute("sceneHeight", _1to1Height)
    for animation1to1 in animations1to1:
        if animation1to1.getAttribute("paramName") == 'transX':
            keys = animation1to1.getElementsByTagName("key")
            for key in keys:
                old_value = float(key.getAttribute("value"))
                new_value = str(round(old_value * _1to1X, 1))
                key.setAttribute("value", new_value)
        if animation1to1.getAttribute("paramName") == 'transY':
            keys = animation1to1.getElementsByTagName("key")
            for key in keys:
                old_value = float(key.getAttribute("value"))
                new_value = str(round(old_value * _1to1Y, 1))
                key.setAttribute("value", new_value)
    for track1to1 in tracks1to1:
        track1to1.setAttribute("width", _1to1Width)
        track1to1.setAttribute("height", _1to1Height)
    with open(_1to1Name, 'w') as f:
        DOMTree1to1.writexml(f, encoding='utf-8')


def create4to3():
    storyboard4to3.setAttribute("sceneWidth", _4to3Width)
    storyboard4to3.setAttribute("sceneHeight", _4to3Height)
    for animation4to3 in animations4to3:
        if animation4to3.getAttribute("paramName") == 'transX':
            keys = animation4to3.getElementsByTagName("key")
            for key in keys:
                old_value = float(key.getAttribute("value"))
                new_value = str(round(old_value * _4to3X, 1))
                key.setAttribute("value", new_value)
        if animation4to3.getAttribute("paramName") == 'transY':
            keys = animation4to3.getElementsByTagName("key")
            for key in keys:
                old_value = float(key.getAttribute("value"))
                new_value = str(round(old_value * _4to3Y, 1))
                key.setAttribute("value", new_value)
    for track4to3 in tracks4to3:
        track4to3.setAttribute("width", _4to3Width)
        track4to3.setAttribute("height", _4to3Height)
    with open(_4to3Name, 'w') as f:
        DOMTree4to3.writexml(f, encoding='utf-8')


def create3to4():
    storyboard3to4.setAttribute("sceneWidth", _3to4Width)
    storyboard3to4.setAttribute("sceneHeight", _3to4Height)
    for animation3to4 in animations3to4:
        if animation3to4.getAttribute("paramName") == 'transX':
            keys = animation3to4.getElementsByTagName("key")
            for key in keys:
                old_value = float(key.getAttribute("value"))
                new_value = str(round(old_value * _3to4X, 1))
                key.setAttribute("value", new_value)
        if animation3to4.getAttribute("paramName") == 'transY':
            keys = animation3to4.getElementsByTagName("key")
            for key in keys:
                old_value = float(key.getAttribute("value"))
                new_value = str(round(old_value * _3to4Y, 1))
                key.setAttribute("value", new_value)
    for track3to4 in tracks3to4:
        track3to4.setAttribute("width", _3to4Width)
        track3to4.setAttribute("height", _3to4Height)
    with open(_3to4Name, 'w') as f:
        DOMTree3to4.writexml(f, encoding='utf-8')


if __name__ == '__main__':
    create9to16()
    create1to1()
    create4to3()
    create3to4()


# <?xml version="1.0" encoding="UTF-8"?>
# <storyboard sceneWidth="1280" sceneHeight="720">
# 	<wipeSrcTrack>
# 		<effect name="transform">
# 			<animation paramName="transY">
# 				<key time="0" value="0"/>
# 				<key time="1000" value="720"/>
# 			</animation>
# 		</effect>
# 	</wipeSrcTrack>
# 	<wipeDstTrack>
# 		<effect name="transform">
# 			<animation paramName="transY">
# 				<key time="0" value="-720"/>
# 				<key time="1000" value="0"/>
# 			</animation>
# 		</effect>
# 	</wipeDstTrack>
# 	<track source="white_block.png" width="1280" height="720" clipStart="0" clipDuration="1000">
# 		<effect name="transform">
# 			<animation paramName="transY">
# 				<key time="0" value="-720"/>
# 				<key time="1000" value="0"/>
# 			</animation>
# 		</effect>
# 	</track>
# </storyboard>
