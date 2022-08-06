from doctest import testmod
from multiprocessing import context
from venv import create
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import testModel
from django.http import HttpResponse
from django.contrib import messages

# Create your views here.

def home_view(request, *args, **kwargs):
    context = {}
    return render(request, 'home.html')


def dashboard_view(request, user, *args, **kwargs):
    if str(request.user) != user: # make sure the sure is logged in
        return redirect('../../signup')
    
    user = request.user
    user_tests = testModel.objects.filter(user=user)
        
    sections = []
    
    for test in user_tests:
        add = []
        all_sections = [[test.test, test.id, 'Test'],
                [test.reading_time_sat, 'Reading'],
                [test.break1_time_sat, 'Break 1'],
                [test.english_time_sat, 'English'],
                [test.math_ci_time_sat, 'Math (Inactive)'],
                [test.break2_time_sat, 'Break 2'],
                [test.math_ca_time_sat, 'Math (Active)'],
                [test.before_essay_break_time_sat, 'Break 3'],
                [test.essay_time_sat, 'Essay'],
                [test.reading_1_time_sat_acc, 'Reading (First Half)'],
                [test.break1_time_sat_acc, 'Break 1'],
                [test.reading_2_time_sat_acc, 'Reading (Second Half)'],
                [test.break2_time_sat_acc, 'Break 2'],
                [test.english_time_sat_acc, 'English'],
                [test.math_ci_time_sat_acc, 'Math (Inactive)'],
                [test.break3_time_sat_acc, 'Break 3'],
                [test.math_ca_time_sat_acc, 'Math (Active)'],
                [test.before_essay_break_time_sat_acc, 'Break 4'],
                [test.essay_time_sat_acc, 'Essay'],
                [test.english_time_act, 'English'],
                [test.math_ca_time_act, 'Math'],
                [test.break1_time_act, 'Break 1'],
                [test.reading_time_act, 'Reading'],
                [test.science_time_act, 'Science'],
                [test.before_essay_break_time_act, 'Break 2'],
                [test.essay_time_act, 'Essay'],
                [test.id, 'id']]

        for section in all_sections:
            if section[0] != '00:00':
                add.append(section)
        sections.append(add) 

    context = {
        'sections': sections,
    }
    if request.method == 'POST':
        print(request.POST['action'])
        request_name = request.POST['action'].split('-')[0]
        if request.POST['action'] == 'logout':
            logout(request)
            print(user)
            return redirect('../../signup')
        elif request.POST['action'] == 'create':
            return redirect('create_test/')
            print("create")
        request_id = request.POST['action'].split('-')[1]
        if request_name == 'execute':
            return redirect(f'{request_id}/execute_test/')
            print("execute")
        elif request_name == f'edit':
            return redirect(f'{request_id}/edit_test/')
        elif request_name == 'delete':
            testModel.objects.get(id=request_id).delete()
            return redirect(f'/{user}/dashboard')


    return render(request, 'dashboard.html', context)


def create_test_view(request, user, *args, **kwargs):
    if str(request.user) != user: # make sure the sure is logged in
        return redirect('../../../signup')

    # sat = ['Reading: ', 'Break 1: ', 'English: ', 'Math (Inactive): ', 'Break 2: ', 'Math (Active): ']
    sat = [
        ['Reading: ', 'reading_time_sat'], 
        ['Break 1: ', 'break1_time_sat'], 
        ['English: ', 'english_time_sat'], 
        ['Math (Inactive): ', 'math_ci_time_sat'], 
        ['Break 2: ', 'break2_time_sat'],  
        ['Math (Active): ', 'math_ca_time_sat']]
    sat_acc = [
        ['Reading (1st half): ', 'reading_1_time_sat_acc'],
        ['Break 1: ', 'break1_time_sat_acc'],
        ['Reading (2nd half)', 'reading_2_time_sat_acc'],
        ['Break 2: ', 'break2_time_sat_acc'],
        ['English: ', 'english_time_sat_acc'],
        ['Math (Inactive)', 'math_ci_time_sat_acc'],
        ['Break 3:', 'break3_time_sat_acc'],
        ['Math (Active)', 'math_ca_time_sat_acc']]
    act = [
        ['English: ', 'english_time_act'],
        ['Math (Active): ', 'math_ca_time_act'],
        ['Break 1: ', 'break1_time_act'],
        ['Reading: ', 'reading_time_act'],
        ['Science: ', 'science_time_act']]

    context = {
        'sat': sat,
        'sat_acc': sat_acc,
        'act' : act        
    }

    if request.method == 'POST':
        user = request.user
        test = request.POST.get('test')
        bool_values = lambda x: False if x == None else True 
        essay = bool_values(request.POST.get('essay'))
        accommodations = bool_values(request.POST.get('accommodations'))
        filter = lambda x: x if x != "" else '00:00'
        reading_time_sat = filter(request.POST.get('reading_time_sat'))
        break1_time_sat = filter(request.POST.get('break1_time_sat'))
        english_time_sat = filter(request.POST.get('english_time_sat'))
        math_ci_time_sat = filter(request.POST.get('math_ci_time_sat'))
        break2_time_sat = filter(request.POST.get('break2_time_sat'))
        math_ca_time_sat = filter(request.POST.get('math_ca_time_sat'))
        before_essay_break_time_sat = filter(request.POST.get('before_essay_break_time_sat'))
        essay_time_sat = filter(request.POST.get('essay_time_sat'))
        reading_1_time_sat_acc = filter(request.POST.get('reading_1_time_sat_acc'))
        break1_time_sat_acc = filter(request.POST.get('break1_time_sat_acc'))
        reading_2_time_sat_acc = filter(request.POST.get('reading_2_time_sat_acc'))
        break2_time_sat_acc = filter(request.POST.get('break2_time_sat_acc'))
        english_time_sat_acc = filter(request.POST.get('english_time_sat_acc'))
        math_ci_time_sat_acc = filter(request.POST.get('math_ci_time_sat_acc'))
        break3_time_sat_acc = filter(request.POST.get('break3_time_sat_acc'))
        math_ca_time_sat_acc = filter(request.POST.get('math_ca_time_sat_acc'))
        before_essay_break_time_sat_acc = filter(request.POST.get('before_essay_break_time_sat_acc'))
        essay_time_sat_acc = filter(request.POST.get('essay_time_sat_acc'))
        english_time_act = filter(request.POST.get('english_time_act'))
        math_ca_time_act = filter(request.POST.get('math_ca_time_act'))
        break1_time_act = filter(request.POST.get('break1_time_act'))
        reading_time_act = filter(request.POST.get('reading_time_act'))
        science_time_act = filter(request.POST.get('science_time_act'))
        before_essay_break_time_act = filter(request.POST.get('before_essay_break_time_act'))
        essay_time_act = filter(request.POST.get('essay_time_act'))
        type = ""
        print(essay)
        if test == "SAT":
            if accommodations == False:
                if essay == False:
                    type = "SAT"
                else:
                    type = "SAT With Essay"
            else:
                if essay == False:
                    type = "SAT With Accommodations"
                else:
                    type = "SAT With Accommodations and Essay"
        if test == "ACT":
            if accommodations == False:
                if essay == False:
                    type = "ACT"
                else:
                    type = "ACT With Essay"
            else:
                if essay == False:
                    type = "ACT With Accommodations"
                else:
                    type = "ACT With Accommodations and Essay"
        print(user, 
            type,
            accommodations,
            reading_time_sat,
            break1_time_sat,
            english_time_sat,
            math_ci_time_sat,
            break2_time_sat,
            math_ca_time_sat,
            before_essay_break_time_sat,
            essay_time_sat,
            reading_1_time_sat_acc,
            break1_time_sat_acc,
            reading_2_time_sat_acc,
            break2_time_sat_acc,
            english_time_sat_acc,
            math_ci_time_sat_acc,
            break3_time_sat_acc,
            math_ca_time_sat_acc,
            before_essay_break_time_sat_acc,
            essay_time_sat_acc,
            english_time_act,
            math_ca_time_act,
            break1_time_act,
            reading_time_act,
            science_time_act,
            before_essay_break_time_act,
            essay_time_act)
        if request.POST['action'] == 'Save':
            testModel.objects.create(
                user = user,
                test = type,
                accommodations = accommodations,
                reading_time_sat = reading_time_sat,
                break1_time_sat = break1_time_sat,
                english_time_sat = english_time_sat,
                math_ci_time_sat = math_ci_time_sat,
                break2_time_sat = break2_time_sat,
                math_ca_time_sat = math_ca_time_sat,
                before_essay_break_time_sat = before_essay_break_time_sat,
                essay_time_sat = essay_time_sat,
                reading_1_time_sat_acc = reading_1_time_sat_acc,
                break1_time_sat_acc = break1_time_sat_acc,
                reading_2_time_sat_acc = reading_2_time_sat_acc,
                break2_time_sat_acc = break2_time_sat_acc,
                english_time_sat_acc = english_time_sat_acc,
                math_ci_time_sat_acc = math_ci_time_sat_acc,
                break3_time_sat_acc = break3_time_sat_acc,
                math_ca_time_sat_acc = math_ca_time_sat_acc,
                before_essay_break_time_sat_acc = before_essay_break_time_sat_acc,
                essay_time_sat_acc = essay_time_sat_acc,
                english_time_act = english_time_act,
                math_ca_time_act = math_ca_time_act,
                break1_time_act = break1_time_act,
                reading_time_act = reading_time_act,
                science_time_act = science_time_act,
                before_essay_break_time_act = before_essay_break_time_act,
                essay_time_act = essay_time_act)
            return redirect('../')

        elif request.POST['action'] == 'Cancel': 
            return redirect('../')

    return render(request, 'create_test.html', context)


def edit_test_view(request, user, id, *args, **kwargs):
    if str(request.user) != user: # make sure the sure is logged in
        return redirect('../../../signup')
    
    user = request.user
    test = testModel.objects.get(user=user, id=id)
    # test = testModel.objects.get(user=user, id=id)
    # print(test.reading_time_sat)
    test_sections = []
    
    all_sections = [[test.test, 'Test', 'test'],
            [test.reading_time_sat, 'Reading', 'reading_time_sat'],
            [test.break1_time_sat, 'Break 1', 'break1_time_sat'],
            [test.english_time_sat, 'English', 'english_time_sat'],
            [test.math_ci_time_sat, 'Math (Inactive)', 'math_ci_time_sat'],
            [test.break2_time_sat, 'Break 2', 'break2_time_sat'],
            [test.math_ca_time_sat, 'Math (Active)', 'math_ca_time_sat'],
            [test.before_essay_break_time_sat, 'Break 3', 'before_essay_break_time_sat'],
            [test.essay_time_sat, 'Essay', 'essay_time_sat'],
            [test.reading_1_time_sat_acc, 'Reading (First Half)', 'reading_1_time_sat_acc'],
            [test.break1_time_sat_acc, 'Break 1', 'break1_time_sat_acc'],
            [test.reading_2_time_sat_acc, 'Reading (Second Half)', 'reading_2_time_sat_acc'],
            [test.break2_time_sat_acc, 'Break 2', 'break2_time_sat_acc'],
            [test.english_time_sat_acc, 'English', 'english_time_sat_acc'],
            [test.math_ci_time_sat_acc, 'Math (Inactive)', 'math_ci_time_sat_acc'],
            [test.break3_time_sat_acc, 'Break 3', 'break3_time_sat_acc'],
            [test.math_ca_time_sat_acc, 'Math (Active)', 'math_ca_time_sat_acc'],
            [test.before_essay_break_time_sat_acc, 'Break 4', 'before_essay_break_time_sat_acc'],
            [test.essay_time_sat_acc, 'Essay', 'essay_time_sat_acc'],
            [test.english_time_act, 'English', 'english_time_act'],
            [test.math_ca_time_act, 'Math', 'math_ca_time_act'],
            [test.break1_time_act, 'Break 1', 'break1_time_act'],
            [test.reading_time_act, 'Reading', 'reading_time_act'],
            [test.science_time_act, 'Science', 'science_time_act'],
            [test.before_essay_break_time_act, 'Break 2', 'before_essay_break_time_act'],
            [test.essay_time_act, 'Essay', 'essay_time_act'],
            [test.id, 'id', 'id']]
    print(all_sections[1:7])
    test_sections.append(all_sections[0])
    if test.test == 'SAT':
        for section in all_sections[1:7]:
            test_sections.append(section)

    if test.test == 'SAT With Essay':
        for section in all_sections[1:9]:
            test_sections.append(section)

    if test.test == 'SAT With Accommodations':
        for section in all_sections[9:17]:
            test_sections.append(section)
        
    if test.test == 'SAT With Accommodations and Essay':
        for section in all_sections[9:19]:
            test_sections.append(section)

    if test.test == 'ACT':
        for section in all_sections[19:24]:
            test_sections.append(section)

    if test.test == 'ACT With Accommodations':
        for section in all_sections[19:24]:
            test_sections.append(section)

    if test.test == 'ACT With Accommodations and Essay':
        for section in all_sections[19:26]:
            test_sections.append(section)
    
    
    context = {
        'test_sections': test_sections,
    }

    if request.method == 'POST':
        request_name = request.POST['action'].split('-')[0]
        request_id = request.POST['action'].split('-')[1]
        if request_name == 'save':
            print('save')
            none_filter = lambda x: x if x != None else ""
            filter = lambda x: x if x != "" else '00:00'
            reading_time_sat = filter(none_filter(request.POST.get('reading_time_sat')))
            break1_time_sat = filter(none_filter(request.POST.get('break1_time_sat')))
            english_time_sat = filter(none_filter(request.POST.get('english_time_sat')))
            math_ci_time_sat = filter(none_filter(request.POST.get('math_ci_time_sat')))
            break2_time_sat = filter(none_filter(request.POST.get('break2_time_sat')))
            math_ca_time_sat = filter(none_filter(request.POST.get('math_ca_time_sat')))
            before_essay_break_time_sat = filter(none_filter(request.POST.get('before_essay_break_time_sat')))
            essay_time_sat = filter(none_filter(request.POST.get('essay_time_sat')))
            reading_1_time_sat_acc = filter(none_filter(request.POST.get('reading_1_time_sat_acc')))
            break1_time_sat_acc = filter(none_filter(request.POST.get('break1_time_sat_acc')))
            reading_2_time_sat_acc = filter(none_filter(request.POST.get('reading_2_time_sat_acc')))
            break2_time_sat_acc = filter(none_filter(request.POST.get('break2_time_sat_acc')))
            english_time_sat_acc = filter(none_filter(request.POST.get('english_time_sat_acc')))
            math_ci_time_sat_acc = filter(none_filter(request.POST.get('math_ci_time_sat_acc')))
            break3_time_sat_acc = filter(none_filter(request.POST.get('break3_time_sat_acc')))
            math_ca_time_sat_acc = filter(none_filter(request.POST.get('math_ca_time_sat_acc')))
            before_essay_break_time_sat_acc = filter(none_filter(request.POST.get('before_essay_break_time_sat_acc')))
            essay_time_sat_acc = filter(none_filter(request.POST.get('essay_time_sat_acc')))
            english_time_act = filter(none_filter(request.POST.get('english_time_act')))
            math_ca_time_act = filter(none_filter(request.POST.get('math_ca_time_act')))
            break1_time_act = filter(none_filter(request.POST.get('break1_time_act')))
            reading_time_act = filter(none_filter(request.POST.get('reading_time_act')))
            science_time_act = filter(none_filter(request.POST.get('science_time_act')))
            before_essay_break_time_act = filter(none_filter(request.POST.get('before_essay_break_time_act')))
            essay_time_act = filter(none_filter(request.POST.get('essay_time_act')))

            print(
                reading_time_sat,
                break1_time_sat,
                english_time_sat,
                math_ci_time_sat,
                break2_time_sat,
                math_ca_time_sat,
                before_essay_break_time_sat,
                essay_time_sat,
                reading_1_time_sat_acc,
                break1_time_sat_acc,
                reading_2_time_sat_acc,
                break2_time_sat_acc,
                english_time_sat_acc,
                math_ci_time_sat_acc,
                break3_time_sat_acc,
                math_ca_time_sat_acc,
                before_essay_break_time_sat_acc,
                essay_time_sat_acc,
                english_time_act,
                math_ca_time_act,
                break1_time_act,
                reading_time_act,
                science_time_act,
                before_essay_break_time_act,
                essay_time_act)
            
            testModel.objects.filter(id=id).update(
                reading_time_sat = reading_time_sat,
                break1_time_sat = break1_time_sat,
                english_time_sat = english_time_sat,
                math_ci_time_sat = math_ci_time_sat,
                break2_time_sat = break2_time_sat,
                math_ca_time_sat = math_ca_time_sat,
                before_essay_break_time_sat = before_essay_break_time_sat,
                essay_time_sat = essay_time_sat,
                reading_1_time_sat_acc = reading_1_time_sat_acc,
                break1_time_sat_acc = break1_time_sat_acc,
                reading_2_time_sat_acc = reading_2_time_sat_acc,
                break2_time_sat_acc = break2_time_sat_acc,
                english_time_sat_acc = english_time_sat_acc,
                math_ci_time_sat_acc = math_ci_time_sat_acc,
                break3_time_sat_acc = break3_time_sat_acc,
                math_ca_time_sat_acc = math_ca_time_sat_acc,
                before_essay_break_time_sat_acc = before_essay_break_time_sat_acc,
                essay_time_sat_acc = essay_time_sat_acc,
                english_time_act = english_time_act,
                math_ca_time_act = math_ca_time_act,
                break1_time_act = break1_time_act,
                reading_time_act = reading_time_act,
                science_time_act = science_time_act,
                before_essay_break_time_act = before_essay_break_time_act,
                essay_time_act = essay_time_act
            )
            return redirect('../..')
        if request_name == 'cancel':
            print('cancel')
            return redirect('../..')

    return render(request, 'edit_test.html', context)


def execute_test_view(request, user, id, *args, **kwargs):
    if str(request.user) != user: # make sure the sure is logged in
        return redirect('../../../signup')
    
    user = request.user
    test = testModel.objects.get(user=user, id=id)
    test_sections = []

    all_sections = [[test.test, 'Test', 'test'],
            [test.reading_time_sat, 'Reading', 'reading_time_sat'],
            [test.break1_time_sat, 'Break 1', 'break1_time_sat'],
            [test.english_time_sat, 'English', 'english_time_sat'],
            [test.math_ci_time_sat, 'Math (Inactive)', 'math_ci_time_sat'],
            [test.break2_time_sat, 'Break 2', 'break2_time_sat'],
            [test.math_ca_time_sat, 'Math (Active)', 'math_ca_time_sat'],
            [test.before_essay_break_time_sat, 'Break 3', 'before_essay_break_time_sat'],
            [test.essay_time_sat, 'Essay', 'essay_time_sat'],
            [test.reading_1_time_sat_acc, 'Reading (First Half)', 'reading_1_time_sat_acc'],
            [test.break1_time_sat_acc, 'Break 1', 'break1_time_sat_acc'],
            [test.reading_2_time_sat_acc, 'Reading (Second Half)', 'reading_2_time_sat_acc'],
            [test.break2_time_sat_acc, 'Break 2', 'break2_time_sat_acc'],
            [test.english_time_sat_acc, 'English', 'english_time_sat_acc'],
            [test.math_ci_time_sat_acc, 'Math (Inactive)', 'math_ci_time_sat_acc'],
            [test.break3_time_sat_acc, 'Break 3', 'break3_time_sat_acc'],
            [test.math_ca_time_sat_acc, 'Math (Active)', 'math_ca_time_sat_acc'],
            [test.before_essay_break_time_sat_acc, 'Break 4', 'before_essay_break_time_sat_acc'],
            [test.essay_time_sat_acc, 'Essay', 'essay_time_sat_acc'],
            [test.english_time_act, 'English', 'english_time_act'],
            [test.math_ca_time_act, 'Math', 'math_ca_time_act'],
            [test.break1_time_act, 'Break 1', 'break1_time_act'],
            [test.reading_time_act, 'Reading', 'reading_time_act'],
            [test.science_time_act, 'Science', 'science_time_act'],
            [test.before_essay_break_time_act, 'Break 2', 'before_essay_break_time_act'],
            [test.essay_time_act, 'Essay', 'essay_time_act']]
    for section in all_sections:
            if section[0] != '00:00':
                test_sections.append(section) 
    context = {
        'test_sections': test_sections
    }
    return render(request, 'execute_test.html', context)


def signup_and_login_view(request, *args, **kwargs):
    context = {}
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        auth_username = request.POST.get('auth_username')
        auth_password = request.POST.get('auth_password')
        print(first_name, last_name, username, password, email, auth_username, auth_password)
        if username != None:
            print("creating...")
            user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name)
            print(user, user.password)
            print("create")
        if auth_username != None:
            print('authenticating...')
            user = authenticate(username=auth_username, password=auth_password)
            context['user'] = user
            # user = authenticate(username='ethanxu1', password='1234')
            print(user)
            if user is not None:
                print("correct")
                login(request, user)
                return redirect(f"../{request.user}/dashboard")
            else:
                messages.info(request, "incorrect")

            # print(request.user)
            # print(user.is_staff)

    return render(request, 'signup_and_login.html', context)


def edit_account_view(request, *args, **kwargs):
    user = User.objects.get(username=request.user)
    print(user.password)
    
    context = {

    }
    
    return render(request, 'edit_account.html', context)
