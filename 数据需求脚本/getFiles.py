from os import listdir, path
from re import match


def file_name(target_dir):
    """拿到目录下所有需要文件名

    匹配示例：供应商-产品名-渠道-广告形式.xlsx，其中广告形式可能是a-b这种形式

    :arg
        target_dir:目标目录，将只返回该目录下的文件名，不包括子目录

    :return
        file_list:包含所有符合规则的文件名list(拼接绝对路径)

    :raise
        ValueError:目标目录内没有符合规则的文件
    """
    file_list = []
    file_and_dir_list = listdir(target_dir)
    for each_file in file_and_dir_list:
        # 注意要去掉～开头的临时文件
        if match(r'^[^~][\S]+?-[\S]+?-[\S]+?-[\S]+?-[\S]+?.(xlsx)', each_file) or \
                match(r'^[^~][\S]+?-[\S]+?-[\S]+?-[\S]+?.(xlsx)', each_file):
            each_file = path.abspath(target_dir) + "/" + each_file
            file_list.append(each_file)
    if file_list:
        return file_list
    else:
        raise ValueError("未找到符合规则的文件！")
