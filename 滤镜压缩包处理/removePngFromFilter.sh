# 滤镜文件解压后，删除里面的png文件，再重新压缩
# 没有传路径当参数了，先把脚本文件放到滤镜文件目录中，然后执行即可
# 读取当前文件夹下所有的.zip文件
for tar in *.zip;
do
# 解压zip文件
unzip $tar;
# 获取zip文件长度-4（因为结尾是.zip，减4后就是文件名长度）
len=${#tar}-4
# 依据这个文件名长度，截取该zip文件的文件名，即只要.zip前面的部分
name=${tar:0:$len}
# 把png文件删掉
rm -rf ./*.png
# 删除原来的zip文件
rm -rf $tar
# 重新打包
zip ./$tar ./$name.animatedsticker ./$name.lic
# 删除剩余的两个文件
rm -rf ./$name.animatedsticker ./$name.lic
done
