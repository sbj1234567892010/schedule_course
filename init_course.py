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
 'C++ programming'] * 2 #,'Java programming','C language programming', 'Python programming', 'data structure'
 #,'Artificial Intelligence', 'web development', 'Computer Architecture', 'College English'
 #, 'Complex Analysis' ,'Computational Method','Computer Graphics'#,'computer organization' ,
 #'computer architecture' , 'Digital Image Processing']
Classroom_name_list = ['East1A-301','West2B-203'] * 2
teacher_name_list = ['Wang Xiaoming', 'Han meimei', 'Li Lei']


def create_courses():
    i = 0
    for class_name in Class_name_list:
        class_obj = Classtable(course_name = class_name)
        class_obj.teacher_name = teacher_name_list[random.randrange(3)]
        class_obj.identity = i
        class_obj.course_identity = i
        class_obj.course_capacity = random.randrange(6,11,2) * 10
        class_obj.course_period = random.randrange(1,3)
        class_obj.course_time_1 = random.randrange(1,14)
        class_obj.course_time_2 = random.randrange(1,14)
        class_obj.classroom_identity_1 = random.randrange(1,3)
        class_obj.classroom_identity_2 = random.randrange(1,3)
        class_obj.classroom_name_1 = Classroom_name_list[random.randrange(2)]
        class_obj.classroom_name_2 = Classroom_name_list[random.randrange(2)]
        class_obj.classroom_capacity_1 = random.randrange(6,11,2) * 10
        class_obj.classroom_capacity_2 = random.randrange(6,11,2) * 10
        class_obj.save()
        i += 1


def main():
    Classtable.objects.all().delete()
    create_courses()
    print("Init done!")

if __name__ == '__main__':
    main()
    