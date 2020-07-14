import qrcode
import subprocess
import sys
import os

"""
    暴露本地文件夹并生成二维码
    使用方式：
        1.python [脚本名] [暴露文件夹路径] [暴露端口号]
        2.python [脚本名] [暴露文件夹路径]   # 即暴露默认端口号
        3.python [脚本名] [暴露端口号]   # 即暴露当前文件夹
        4.python [脚本名]  # 即暴露当前文件夹 and 使用默认端口号
    ctrl + c 结束进程
    建议在shell配置中增加函数：
    vim ~/.zshrc  # 因为我使用的是zsh，就修改zshrc这个配置文件
    添加：
    function httpserver(){
        python3 ~/Desktop/httpServer.py ${1} ${2}
    }
    这样可以在终端使用 httpserver 代替 python3 [脚本名]，后面的参数规则不变（修改配置后记得重启终端）
"""

PORT = 7777  # 给一个默认的端口号


def execCmd(cmd):
    """
    :param cmd: shell命令
    :return: 命令执行结果

    需要这么做是因为在脚本命令中需要通过 f"{}" 的形式传入参数，但是又存在一个使用 '{print $2}' 的方式获取第二个结果，
    存在{}语法冲突，所以只能分成两部分来写了。
    """
    r = os.popen(cmd)
    text = r.read()
    r.close()
    return text


if len(sys.argv) == 1:  # 使用方式四：不传参
    pass
elif len(sys.argv) == 2 and sys.argv[1].isnumeric():  # 使用方式三：传一个参数，即端口号
    PORT = int(sys.argv[1])
elif len(sys.argv) == 2 and not sys.argv[1].isnumeric():  # 使用方式二：传一个参数，即文件夹路径
    os.chdir(sys.argv[1])  # 把路径设置为目标路径
elif len(sys.argv) == 3 and sys.argv[2].isnumeric():  # 使用方式一：传两个参数，即文件夹路径和端口号
    os.chdir(sys.argv[1])  # 把路径设置为目标路径
    PORT = int(sys.argv[2])
else:  # 错误传参
    print("wrong args")
    exit(1)

InfoOfPort = execCmd(f"lsof -i:{PORT} | tail -n 1")  # 获取该端口号的信息
# 防止端口已被使用，需要先释放该端口
if InfoOfPort != "":
    ProcessOfPort = InfoOfPort.split()[1]  # 获取该端口号的进程号
    subprocess.run(f"kill {ProcessOfPort}", shell=True)  # 杀死进程

# 暴露文件夹
subprocess.Popen(f"python3 -m http.server {PORT}", shell=True)

# 地址也输出一下
print(f"http://192.168.11.112:{PORT}")

# 生成二维码
qr = qrcode.QRCode()
qr.add_data(f'http://192.168.11.112:{PORT}/')
qr.print_ascii(invert=True)  # 二维码是白底黑块，不倒置就是黑底白块
print("ctrl + c 退出")
