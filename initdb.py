#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import random
import time
import numpy as np

import os, django
os.environ["DJANGO_SETTINGS_MODULE"] = "Schedule_Course.settings"
django.setup()

from Web.models import Class, Classroom, Classtable
from Web.models import scheduler, db_insert_classroom, db_delete_all, get_classroom_info, get_classroom_table

Class_name_list = ['Discrete Mathematics ', 'advanced mathematics', 'Database', 'Software Engineering',
 'C++ programming','Java programming','C language programming', 'Python programming', 'data structure'
 ,'Artificial Intelligence'] #, 'web development', 'Computer Architecture', 'College English'
 #, 'Complex Analysis' ,'Computational Method','Computer Graphics'#,'computer organization' ,
 #'computer architecture' , 'Digital Image Processing']
Classroom_name_list = ['East1A-301','West2B-203'] * 2
teacher_name_list = ['Wang Xiaoming', 'Han meimei', 'Li Lei', 'Zhang San', 'Li Si']

N_CLASSROOM = 4

def create_classes():
    i = 0
    for class_name in Class_name_list:
        class_obj = Class(name = class_name)
        class_obj.teacher_name = teacher_name_list[random.randrange(3)]
        class_obj.identity = i
        class_obj.capacity = random.randrange(6,11,2) * 10
        class_obj.period = random.randrange(1,3)
        class_obj.save()
        i += 1
'''
def create_classrooms():
    i = 0
    for classroom_name in Classroom_name_list:
        classroom = Classroom(name = classroom_name)
        classroom.identity = i
        classroom.capacity = random.randrange(8,19,2) * 10
        classroom.save()
        i += 1
'''
def create_classrooms():
    classroom_info = get_classroom_table()
    print(classroom_info)
    i = 0
    for class_dict in classroom_info:
        classroom_obj = Classroom(name = class_dict['loc'])
        classroom_obj.identity = class_dict['id']
        classroom_obj.capacity = class_dict['cap']
        classroom_obj.save()
        i += 1

def init_w_classrooms():
    loc_direc = ['South','West','East','North']
    building_num = [1,2,3,4]
    building_div = ['A','B','C','D']

    #capacity = [30,60,90,120,180,250]
    capacity = [80, 100, 120, 140, 160, 180]
    classrooms = []

    m_media = ['projector','LED','nothing']
    camp = ['Yuquan','Zijingang','Huajiachi','Xixi','Z_jiang']
    remarks = ['May fall water','far from toilet','seats are old','']

    step = 20
    ori = 0

    for i in range(N_CLASSROOM):
        classroom = ''
        id = i
        ori = id+1
        loc = np.random.choice(loc_direc)+str(np.random.choice(building_num))+np.random.choice(building_div) +'-' + str(np.random.randint(0,1000))
        cap = np.random.choice(capacity)
        mmedia = np.random.choice(m_media)
        campus = np.random.choice(camp)
        rmk = np.random.choice(remarks)
        #one_entry = '%08d %20s %3d %10s %10s %10s' % (id,loc,cap,mmedia,campus,rmk)
        if db_insert_classroom(id,loc,cap,mmedia,campus,rmk):
            print(i)
        else:
            print('failed')


def main():
    Class.objects.all().delete()
    Classroom.objects.all().delete()
    Classtable.objects.all().delete()
    db_delete_all()
    create_classes()
    init_w_classrooms()
    create_classrooms()
    print("Init done!")

    i = time.time()
    #scheduler()
    j = time.time()
    print("cost time" + str(j - i))
 
if __name__ == '__main__':
    main()
    