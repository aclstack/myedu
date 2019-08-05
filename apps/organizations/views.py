from django.shortcuts import render
from django.views.generic.base import View
from apps.organizations.models import CourseOrg, City
from apps.operation.models import UserAsk
# 分页模块
from django.shortcuts import render_to_response
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
from apps.organizations.forms import AddAskForm, AddAskForm2
from django.http import JsonResponse

class OrgView(View):
    def get(self, request, *args, **kwargs):
        all_orgs = CourseOrg.objects.all()
        all_citys = City.objects.all()
        hot_orgs = all_orgs.order_by('-click_nums')[:3]
        # 通过类别对课程机构进行筛选
        category = request.GET.get('ct', '')
        if category:
            all_orgs = all_orgs.filter(category=category)
        # 通过城市对课程机构进行筛选

        city_id = request.GET.get('city', '')
        if city_id:
            if city_id.isdigit():
                all_orgs = all_orgs.filter(city_id=int(city_id))

        # 对机构进行排序
        sort = request.GET.get('sort', '')
        if sort == "students":
            # 加上-则为倒序，否则为正序
            all_orgs = all_orgs.order_by("-students")
        elif sort == "courses":
            all_orgs = all_orgs.order_by("-course_num")

        # 对课程机构数据进行分页
        org_nums = all_orgs.count()
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        # per_page 每页显示数量
        p  = Paginator(all_orgs, per_page=5, request=request)
        orgs = p.page(page)




        return render(request, 'org-list.html',
                      {'all_orgs': orgs,
                       'org_nums': org_nums,
                       'all_citys': all_citys,
                       'category': category,
                       'city_id': city_id,
                       'sort': sort,
                       'hot_orgs': hot_orgs
                       })


class AddAskView(View):
    def post(self, request):
        # 处理用户咨询服务，采用modele.form方式
        userask_form = AddAskForm2(request.POST)
        if userask_form.is_valid():
            # commit=True 提交到数据库并执行
            # 返回的是userask的实例(数据库，而非form的)
            userask_form.save(commit=True)
            return JsonResponse({
                'status': 'success'
            })

        # 纯form方式实现
        # userask_form = AddAskForm(request.POST)
        # if userask_form.is_valid():
        #     add = UserAsk()
        #     add.name = userask_form.cleaned_data.get('name')
        #     add.mobile = userask_form.cleaned_data.get('mobile')
        #     add.course_name = userask_form.cleaned_data.get('course_name')
        #     add.save()
        #     return JsonResponse({
        #         'status': 'success'
        #     })
        else:
            for key, value in userask_form.errors.items():
                msg = value[0]
                break
            return JsonResponse({
                'status': 'fail',
                'msg': msg
            })
