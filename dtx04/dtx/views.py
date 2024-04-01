
import requests
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.contrib.auth.hashers import check_password
from requests.adapters import Retry, HTTPAdapter
from requests import Session

# 0602 login 기능 구현
# 0912 login 기능 DB연결
# 상담사 로그인 함수
@method_decorator(csrf_exempt,name='dispatch')
def Login(request):
    try:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            print('API Post 요청을 통해 전달된 데이터', request.body.decode())

            res_data = {}
            login_info = {'id': username, 'pw': password}
            print(login_info) 

            api_url = 'http://127.0.0.1:19075/dtx/Login'

            retry_strategy = Retry(
                total=5,
                backoff_factor=1,
                status_forcelist=[500, 502, 503, 504],
                connect=5
            )
            adapter = HTTPAdapter(max_retries=retry_strategy)
            session = Session() 
            session.mount('http://', adapter)
            session.mount('https://', adapter)

            try:
                response = session.post(api_url, json=login_info)
                response.raise_for_status()
                response_data = response.json()
                print("response_data(47): ", response_data)
                print(response_data['message'])
                # 성공적인 응답 처리
            except requests.exceptions.RequestException as e:
                print(f"Error1: {e}")
                # 실패한 경우 예외 처리
                
            res_data = {}
            if response_data['message'] =='success':
                print("dtx04_view: success")
                return render(request, 'dtx/Counselor_CBT.html')
            else:
                res_data['error'] = "아이디/비밀번호를 다시 입력해 주세요"
                return render(request, 'dtx/Login.html', context=res_data)
        else:
            print("세번째else")
            # GET 요청에 대한 응답
            return render(request, 'dtx/Login.html')
    except Exception as e:
        print(f"Error2: {e}")
        return render(request, 'dtx/Login.html')

    
# 0912 login 기능 DB연결
# medical 로그인 함수
@method_decorator(csrf_exempt,name='dispatch')
def Login_Medi(request):
    try:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            print('API Post 요청을 통해 전달된 데이터', request.body.decode())

            res_data = {}
            login_info = {'id': username, 'pw': password}
            print(login_info) 

            api_url = 'http://127.0.0.1:19075/dtx/Login_Medi'

            retry_strategy = Retry(
                total=5,
                backoff_factor=1,
                status_forcelist=[500, 502, 503, 504],
                connect=5
            )
            adapter = HTTPAdapter(max_retries=retry_strategy)
            session = Session() 
            session.mount('http://', adapter)
            session.mount('https://', adapter)

            try:
                response = session.post(api_url, json=login_info)
                response.raise_for_status()
                response_data = response.json()
                print("response_data(47): ", response_data)
                print(response_data['message'])
                # 성공적인 응답 처리
            except requests.exceptions.RequestException as e:
                print(f"Error1: {e}")
                # 실패한 경우 예외 처리
                
            res_data = {}
            if response_data['message'] =='success':
                print("dtx04_view: success")
                return render(request, 'dtx/Medical_Service.html')
            else:
                res_data['error'] = "아이디/비밀번호를 다시 입력해 주세요"
                return render(request, 'dtx/Login_Medi.html', context=res_data)
        else:
            print("세번째else")
            # GET 요청에 대한 응답
            return render(request, 'dtx/Login_Medi.html')
    except Exception as e:
        print(f"Error2: {e}")
        return render(request, 'dtx/Login_Medi.html')


# 회원가입
@method_decorator(csrf_exempt,name='dispatch')
def Signup(request):
    try:
        if request.method == 'POST':
            business_num = request.POST.get('business_num')
            business_file = request.POST.get('business_file')
            file_pass = request.POST.get('file_pass')
            chkAll = request.POST.get('chkAll')
            chk1 = request.POST.get('chk1')
            chk2 = request.POST.get('chk2')
            chk3 = request.POST.get('chk3')
            chk4 = request.POST.get('chk4')
            chk5 = request.POST.get('chk5')
            username = request.POST.get('username')
            pw = request.POST.get('pw')
            name = request.POST.get('name')
            inst = request.POST.get('inst')
            phone = request.POST.get('phone')
            mail = request.POST.get('mail')


            print('business_num: ', business_num)
            print('business_file: ', business_file)
            print('file_pass: ', file_pass)
            print('chkAll: ', chkAll)
            print('chk1: ', chk1)
            print('chk2: ', chk2)
            print('chk3: ', chk3)
            print('chk4: ', chk4)
            print('chk5: ', chk5)
            print('username: ', username)
            print('pw: ', pw)
            print('name: ', name)
            print('inst: ', inst)
            print('phone: ', phone)
            print('mail: ', mail)
            
            print('API Post 요청을 통해 전달된 데이터', request.body.decode())

            res_data = {}
            login_info = {'business_num': business_num, 'business_file':business_file, 'file_pass':file_pass,
                          'chkAll': chkAll, 'chk1':chk1, 'chk2':chk2, 'chk3':chk3, 'chk4':chk4, 'chk5':chk5, 
                          'username': username, 'pw':pw, 'name':name, 'inst':inst, 'phone':phone, 'mail':mail}
            
            print('login_info: ', login_info) 
            
            api_url = 'http://127.0.0.1:19075/dtx/Signup'
            
            retry_strategy = Retry(
                total=5,
                backoff_factor=1,
                status_forcelist=[500, 502, 503, 504],
                connect=5
            )
            adapter = HTTPAdapter(max_retries=retry_strategy)
            session = Session() 
            session.mount('http://', adapter)
            session.mount('https://', adapter)
            
            try:
                response = session.post(api_url, json=login_info)
                response.raise_for_status()
                response_data = response.json()
                print("response_data(47): ", response_data)
                print(response_data['message'])
                # 성공적인 응답 처리
            except requests.exceptions.RequestException as e:
                print(f"Error1: {e}")
                # 실패한 경우 예외 처리
                
            res_data = {}
            if response_data['message'] =='success':
                print("dtx04_view: success")
                return render(request, 'dtx/login.html')
            if response_data['message'] =='fail1':
                res_data['error'] = "아이디를 확인하세요"
                return render(request, 'dtx/Signup.html', context=res_data)
            if response_data['message'] =='fail2':
                res_data['error'] = "비밀번호를 확인하세요"
                return render(request, 'dtx/Signup.html', context=res_data)
            if response_data['message'] =='fail3':
                res_data['error'] = "휴대폰 번호를 확인하세요"
                return render(request, 'dtx/Signup.html', context=res_data)
            if response_data['message'] =='fail4':
                res_data['error'] = "약관 동의를 확인하세요"
                return render(request, 'dtx/Signup.html', context=res_data)
        else:
            print("세번째else")
            # GET 요청에 대한 응답
            return render(request, 'dtx/Signup.html')
    except Exception as e:
        print(f"Error2: {e}")
        return render(request, 'dtx/Signup.html')
    
    

#0515 페이지 연결
#0518 get/post 작성 
def Counselor_CBT(request):
    counsel = {
        "con":[
            {
            "환자명":"김혁",
            "상담일자":"2022.01.13",
            "상담구분":"심리상담",
            "상담유형":"원격상담",
            "측정일자":"2022.01.16",
            "측정구분":"고혈압",
            "측정항목":"혈압",
            "정상치":"120/140",
            "상담내역":"우울증 심화",
            "실행목표":"우울증 완화",
            "실행계획":"CBT 상담 진행",
            "실행평가":"심각한 우울증"
            },
            {
            "환자명":"이혁",
            "상담일자":"2022.01.16",
            "상담구분":"CBT상담",
            "상담유형":"대면상담",
            "측정일자":"2022.01.16",
            "측정구분":"고혈압",
            "측정항목":"혈압",
            "정상치":"120/140",
            "상담내역":"가벼운 우울증",
            "실행목표":"우울증 완화",
            "실행계획":"대면 상담 진행",
            "실행평가":"가벼운 우울증"
            }
        ]
    }
    
    if request.method == 'POST':
        name = request.POST.get('name')
        date = request.POST.get('date')
        coun = request.POST.get('coun')
        print("post받아온값:", date)
        print("post받아온값:", coun)
        temp_dict = {}
        for one_dict in counsel['con']:
            # print("더미데이터 하나씩 돌린 값:", one_dict)
            b = one_dict['환자명']
            # print("더미데이터에서 환자명만 출력:", b)
            if b == name:
                temp_dict['bb'] = one_dict
                # print(temp_dict)
                
        return render(request, 'dtx/Counselor_CBT.html', context=temp_dict)
    else:
        return render(request, 'dtx/Counselor_CBT.html')

    
        

def Counselor_perform(request):
    return render(request, 'dtx/Counselor_perform.html')


def Medical_Service(request):
    a = {
    "aa": [
    {
    "지역":"서울 마포구",
    "기관명":"기관명1",
    "환자명":"김혁",
    "성별":"남",
    "연령":21,
    "교육방식_의사대면교육":"우울증/불안",
    "비대면_심리상담센터_의뢰":"우울증",
    "교육_상담_실행건수":2,
    "비대면_실행건수":1,
    "총_실행건수":3,
    "개인정보동의":"동의함",
    "graph":"/images/donut_chart.jpg",
    "profile":"/images/user_profile1.png"
    },
    {
    "지역":"",
    "기관명":"기관명1",
    "환자명":"이혁",
    "성별":"남",
    "연령":29,
    "교육방식_의사대면교육":"우울증",
    "비대면_심리상담센터_의뢰":"우울증",
    "교육_상담_실행건수":3,
    "비대면_실행건수":2,
    "총_실행건수":5,
    "개인정보동의":"동의함",
    "메모":"2020' CFS: polyp removal 세파계열 anti S/E 있음. 설사",
    "graph":"/images/donut_chart2.jpg",
    "profile":"/images/user_profile2.png"
    },
    {
    "지역":"",
    "기관명":"기관명1",
    "환자명":"장혁",
    "성별":"남",
    "연령":35,
    "교육방식_의사대면교육":"불안",
    "비대면_심리상담센터_의뢰":"불안",
    "교육_상담_실행건수":3,
    "비대면_실행건수":0,
    "총_실행건수":3,
    "개인정보동의":"동의함",
    "graph":"/images/donut_chart3.jpg",
    "profile":"/images/user_profile3.png"
    },
    {
    "지역":"",
    "기관명":"기관명2",
    "환자명":"이덕수",
    "성별":"남",
    "연령":50,
    "교육방식_의사대면교육":"우울증/불안",
    "비대면_심리상담센터_의뢰":"불안",
    "교육_상담_실행건수":1,
    "비대면_실행건수":3,
    "총_실행건수":4,
    "개인정보동의":"동의함",
    "graph":"/images/donut_chart4.jpg",
    "profile":"/images/user_profile4.png"
    },
    {
    "지역":"경기도 성남시",
    "기관명":"기관명1",
    "환자명":"이혜원",
    "성별":"여",
    "연령":37,
    "교육방식_의사대면교육":"불안",
    "비대면_심리상담센터_의뢰":"불안",
    "교육_상담_실행건수":2,
    "비대면_실행건수":1,
    "총_실행건수":3,
    "개인정보동의":"동의함",
    "graph":"/images/donut_chart5.jpg",
    "profile":"/images/user_profile5.png"
    }
    ]
    }
    
    # 프론트 김혁 검색, 프론트에서 검색한 이름과 같은 데이터를 백엔드 데이터에서 선택해서 보여준다
    # view에서 특정 front 타겟으로 데이터를 넘겨주는 방법(classView, JSon) 필요

    if request.method == 'POST':
        search = request.POST.get('search')
        name = request.POST.get('name')
        temp_dict = {}
        for one_dict in a['aa']:
            b = one_dict['환자명']
            if b == search or b == name:
                temp_dict['bb'] = one_dict
                
                
        temp_dict['aa'] = a['aa']
        temp_dict['cc'] = [temp_dict['bb']]
        return render(request, 'dtx/Medical_Service.html', context=temp_dict)
    else:
        print('실패')
        return render(request, 'dtx/Medical_Service.html', context=a)


# 6/20
def Medical_Patient(request):
    a = {
        "aa": [
    {
    "지역":"서울 마포구",
    "기관명":"기관명1",
    "환자명":"김혁",
    "성별":"남",
    "연령":21,
    "교육방식_의사대면교육":"우울증/불안",
    "비대면_심리상담센터_의뢰":"우울증",
    "교육_상담_실행건수":2,
    "비대면_실행건수":1,
    "총_실행건수":3,
    "개인정보동의":"동의함",
    "graph":"/images/donut_chart.jpg",
    "profile":"/images/user_profile1.png"
    },
    {
    "지역":"",
    "기관명":"기관명1",
    "환자명":"이혁",
    "성별":"남",
    "연령":29,
    "교육방식_의사대면교육":"우울증",
    "비대면_심리상담센터_의뢰":"우울증",
    "교육_상담_실행건수":3,
    "비대면_실행건수":2,
    "총_실행건수":5,
    "개인정보동의":"동의함",
    "메모":"2020' CFS: polyp removal 세파계열 anti S/E 있음. 설사",
    "graph":"/images/donut_chart2.jpg",
    "profile":"/images/user_profile2.png"
    },
    {
    "지역":"",
    "기관명":"기관명1",
    "환자명":"장혁",
    "성별":"남",
    "연령":35,
    "교육방식_의사대면교육":"불안",
    "비대면_심리상담센터_의뢰":"불안",
    "교육_상담_실행건수":3,
    "비대면_실행건수":0,
    "총_실행건수":3,
    "개인정보동의":"동의함",
    "graph":"/images/donut_chart3.jpg",
    "profile":"/images/user_profile3.png"
    },
    {
    "지역":"",
    "기관명":"기관명2",
    "환자명":"이덕수",
    "성별":"남",
    "연령":50,
    "교육방식_의사대면교육":"우울증/불안",
    "비대면_심리상담센터_의뢰":"불안",
    "교육_상담_실행건수":1,
    "비대면_실행건수":3,
    "총_실행건수":4,
    "개인정보동의":"동의함",
    "graph":"/images/donut_chart4.jpg",
    "profile":"/images/user_profile4.png"
    },
    {
    "지역":"경기도 성남시",
    "기관명":"기관명1",
    "환자명":"이혜원",
    "성별":"여",
    "연령":37,
    "교육방식_의사대면교육":"불안",
    "비대면_심리상담센터_의뢰":"불안",
    "교육_상담_실행건수":2,
    "비대면_실행건수":1,
    "총_실행건수":3,
    "개인정보동의":"동의함",
    "graph":"/images/donut_chart5.jpg",
    "profile":"/images/user_profile5.png"
    }
    ]
    }
    
    # 프론트 김혁 검색, 프론트에서 검색한 이름과 같은 데이터를 백엔드 데이터에서 선택해서 보여준다
    # view에서 특정 front 타겟으로 데이터를 넘겨주는 방법(classView, JSon) 필요

    if request.method == 'POST':
        search = request.POST.get('search')
        name = request.POST.get('name')
        temp_dict = {}
        for one_dict in a['aa']:
            b = one_dict['환자명']
            if b == search or b == name:
                temp_dict['bb'] = one_dict
                
                
        temp_dict['aa'] = a['aa']
        temp_dict['cc'] = [temp_dict['bb']]
        return render(request, 'dtx/Medical_Patient.html', context=temp_dict)
    else:
        print('실패')
        return render(request, 'dtx/Medical_Patient.html', context=a)


#0516 admin 개발
def Admin_page(request):
    return render(request, 'dtx/Admin_page.html')

def Web_member(request):
    return render(request, 'dtx/Web_member.html')

def App_member(request):
    return render(request, 'dtx/App_member.html')

def Permission(request):
    return render(request, 'dtx/Permission.html')

def Region_status(request):
    return render(request, 'dtx/Region_status.html')