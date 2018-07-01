from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.conf.urls import url, include
from Web.models import *
# Create your views here.

def home_page(request):
    return render(request, 'home.html')

def ui_elements_page(request):
    return render(request, 'ui-elements.html')

def chart_page(request):
    return render(request, 'form1.html')

def table_ts_page(request):
    return render(request, 'table_ts.html')

def tab_panel_page(request):
    if request.method=='GET':
        print(request.GET.keys())
        if 'course_id' not in request.GET.keys():
            return render(request,'classtablemodify.html')
    in_list = get_class_tuple2(request,GET=True)
    update_result = db_update_classtable(in_list)
    if update_result:
        return render(request,'classtablemodify.html',{'script':'alert','wrong':'修改成功'})
    else:
        return render(request,'classtablemodify.html',{'script':'alert','wrong':'更改失败'})

def table_page(request):
    classtable = get_classtable_table()
    return render(request, 'table.html',{'classtable_list':classtable})

def get_class_tuple2(request,GET=True):
    if GET:
        print(request.GET.keys())
        course_id = request.GET.get('course_id', '')
        teacher = request.GET.get('teacher', '')
        period = request.GET.get('period','')
        classroom = request.GET.get('classroom','')
    else:
        print(request.POST.keys())
        course_id = request.GET.get('course_id', '')
        teacher = request.GET.get('teacher', '')
        period = request.GET.get('period', '')
        classroom = request.GET.get('classroom', '')
    return course_id,teacher,period,classroom


def modify_classroom(request):
    if request.method=='GET':
        print(request.GET.keys())
        if 'classroom_id' not in request.GET.keys():
            return render(request,'modify.html')
    in_list = get_class_tuple(request,GET=True)
    update_result  = db_update_classroom(in_list)
    if update_result:
        return render(request,'modify.html',{'script':'alert','wrong':'修改成功'})
    else:
        return render(request,'modify.html',{'script':'alert','wrong':'更改失败，请检查是否已输入此间教室'})

def show_classroom_table(request):
    table = get_classroom_table()
    return render(request,'classroom_table.html',{'classroom_list':table})

def get_class_tuple(request,GET=True):
    if GET:
        #print(request.GET.keys())
        classroom_id = request.GET.get('classroom_id', '')
        classroom_location = request.GET.get('classroom_location', '')
        classroom_capacity = request.GET.get('classroom_capacity', '')
        classroom_multimedia = request.GET.get('classroom_multimedia','')
        classroom_campus = request.GET.get('classroom_campus','')
        classroom_remark = request.GET.get('classroom_remark','')
    else:
        #print(request.POST.keys())
        classroom_id = request.POST.get('classroom_id', '')
        classroom_location = request.POST.get('classroom_location', '')
        classroom_capacity = request.POST.get('classroom_capacity', '')
        classroom_multimedia = request.POST.get('classroom_multimedia','')
        classroom_campus = request.POST.get('classroom_campus','')
        classroom_remark = request.POST.get('classroom_remark','')
    return classroom_id,classroom_location,classroom_capacity,classroom_multimedia,classroom_campus,classroom_remark

def form_page(request):
    return input_classroom(request)

def input_classroom(request):
    if request.method == 'GET': ##插入
        classroom_id, classroom_location, classroom_capacity, classroom_multimedia, classroom_campus, classroom_remark = get_class_tuple(request,True)
        is_submit = request.get_full_path().find('?') != -1
        if classroom_id == '' and is_submit:
            return render(request, 'input.html', {'script': "alert", 'wrong': '没有教室编号，请重新填写'})
        elif classroom_location == '' and is_submit:
            return render(request, 'input.html', {'script': "alert", 'wrong': '没有教室位置，请重新填写'})
        elif classroom_capacity == '' and is_submit:
            return render(request, 'input.html', {'script': "alert", 'wrong': '没有教室容量信息，请重新填写'})
        elif is_submit:  #输入数据库
            res = db_insert_classroom(classroom_id,classroom_location,classroom_capacity,classroom_multimedia,classroom_campus,classroom_remark)
            info = ''
            if res:
                info = '输入成功： '
            else:
                info = '输入失败： '
            table = get_classroom_table()
            return render(request, 'input.html', {'script': "alert", 'wrong': info+classroom_id})
        else:
            return render(request, 'input.html')

def get_table(request):
    p_type = request.GET.get('p_type')
    p_name = request.GET.get('p_name')
    data1 = getData(p_type,p_name)
    data_f = ""
    for i in data1:
        for j in i:
            place = str(j)
            data_f = data_f + place + '*'
    #print(data_f)
    return HttpResponse(data_f)

urlpatterns = [
    url(r'^$',   home_page),
    url(r'^ui-elements/$',   ui_elements_page),
    url(r'^chart/$',   chart_page),
    url(r'^tab-panel/$',   tab_panel_page),
    url(r'^table/$',   table_page),
    url(r'^form/$',   form_page),
    url(r'^modify/',modify_classroom),
    url(r'^classroom_table/',show_classroom_table),
    url(r'^input/',input_classroom),
    url(r'^table/abc/',scheduler),
    url(r'^table_ts/$',table_ts_page),
    url(r'^get_table/',get_table)
]