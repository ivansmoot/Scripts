#!/bin/bash
# 进入需要处理的目录，改目录作为第一个参数传给脚本
cd ${1}
# 获取到所有的日志名，去掉.log后面的空格(手机型号的空格不去掉)
# 将手机型号中间的空格用@占位(否则后面会被当成分割符)
LISTOFLOG=`ls | sed 's/.log /.log/g' | sed 's/ /@/g'`
# 以所有的".log"作为分割符进行分割
NAMEARRAY=(${LISTOFLOG//.log/})
for (( i=0; i < ${#NAMEARRAY[@]}; i++ ))
do
    # 把结尾的".log"去掉
    NAMEARRAY[$i]=${NAMEARRAY[$i]%.log}
done
for var in ${NAMEARRAY[@]}
do
    # 把占位符@重新转换成空格
    var=`echo ${var} | sed 's/@/ /g'`
    # 把"手机名.log"重命名成"log.log"
    mv "$var.log" log.log
    # 把"log.log"压缩成"手机名.zip"
    # 这两步必须要加上双引号，否则机型名中间有空格的话，会报错
    zip "$var.zip" log.log
    # 删除log.log
    rm -rf log.log
done

# 这个脚本是为了与兼容日志脚本配合，做前期的log处理工作的。
# 兼容处理脚本需要的格式是在一个文件夹下，存在多个"手机名.zip"的压缩包，
# 所有压缩包打开，都是名为"log.log"的日志文件
# 而在testin平台下载的文件会被重命名成"手机名.log"
# 这就存在一个从"手机名.log"---->"log.log"---->"log.log.zip"---->"手机名.zip"的过程
# 本脚本即完成这个过程
# 给脚本一个文件夹路径作为参数，即可自动将文件夹下所有
# "手机名.log"的文件转成"手机名.zip"的文件
# 不需要每个log手动设置
