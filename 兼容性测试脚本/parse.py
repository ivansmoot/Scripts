#!/usr/bin/env python
# encoding: utf-8

import sh
import glob
import re
import numpy as np
import pandas as pd
import openpyxl
from FormatTime import finalformatTime


def without_last(s):
    return s[:-len(s.split()[-1])].strip()


def get_last_time(s):
    return int(s.split(':')[-1])


zips = sorted(glob.glob('logs/*.zip'))
dic = {}
for z in zips:
    name = z[5:-4]
    print()
    print(f'Unzip {z}')
    sh.rm(['-rf', 'log.log'])
    sh.rm(['-rf', './__MACOSX'])
    sh.unzip(z)
    print(f'RE {name}')

    ll = open('log.log','r').readlines()

    device = ''
    cpuinfo = ''
    hardware = ''
    judgeDevices = ''
    PreviewParameters = ''
    CreateEngine_CONV2D_FILTER_Error = ''
    ModelName = ''
    time = []
    for i in ll:
        if 'VersaAiInitData' in i:
            device = i.strip().split(":")[-3][0:3]
            cpuinfo = i.strip().split(":")[-2][0:-8]
            hardware = i.strip().split(":")[-1]
        if 'VersaAiJudgeDevices' in i:
            judgeDevices = i.strip().split(':')[-1]
        if 'VersaAiPreviewSize' in i:
            PreviewParameters = ''.join(i.strip().split(':')[-3:])
        if 'CreateEngine CONV2D_FILTER Error' in i:
            CreateEngine_CONV2D_FILTER_Error = i
        if 'VersaAiModelName' in i:
            ModelName = i.strip().split(':')[-1]

    l = [float(i.strip().split(':')[-1][:-2]) for i in ll if 'apiCost' in i]
    l1 = np.mean(l[5:]) if len(l) > 30 else 0
    print('apicost', l1)

    dic[name] = {
        'device': device,
        'cpuinfo': cpuinfo,
        'hardware': hardware,
        'judgeDevices': judgeDevices,
        'PreviewParameters': PreviewParameters,
        'CreateEngine CONV2D_FILTER Error': CreateEngine_CONV2D_FILTER_Error,
        'ModelName': ModelName,
        'apicost': l1
    }

sh.rm(['-rf', 'log.log'])
sh.rm(['-rf', './__MACOSX'])

df = pd.DataFrame.from_dict(dic)
df.T.to_excel('human.xlsx')

wb = openpyxl.load_workbook('human.xlsx')
ws = wb.active

thin = openpyxl.styles.Side(border_style="thin", color=openpyxl.styles.colors.BLACK)
border = openpyxl.styles.Border(top=thin, left=thin, right=thin, bottom=thin)
alignment = openpyxl.styles.Alignment(horizontal='left', vertical='center')

for row in ws.rows:
    for cell in row:
        cell.border = border
        cell.alignment = alignment

ws.column_dimensions['A'].width = 15
ws.column_dimensions['B'].width = 8
ws.column_dimensions['C'].width = 36
ws.column_dimensions['D'].width = 10
ws.column_dimensions['E'].width = 13
ws.column_dimensions['F'].width = 19
ws.column_dimensions['G'].width = 33
ws.column_dimensions['H'].width = 40
ws.column_dimensions['I'].width = 13

wb.save('human.xlsx')