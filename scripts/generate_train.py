# -*- coding:utf-8 -*-
import os

def main(src, dest):
    out_file = open(dest,'w')  #生成了在指定目录下的txt文件  
    with open(dest, 'w') as f:
        for name in os.listdir(src):
            base_name = os.path.basename(name)
            file_name = base_name.split('.')[0]
            f.write('%s\n' % file_name)

if __name__ == '__main__':
    TrainDir = 'VOCdevkit/VOC2007/JPEGImages'  #图片文件所在目录
    target = 'VOCdevkit/VOC2007/ImageSets/Main/train.txt'
    main(TrainDir, target)