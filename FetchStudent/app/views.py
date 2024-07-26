from django.shortcuts import render
def fun1(request):
    student_records_list = [
    {
        'id': '401',
        'name': 'Alice Johnson',
        'age': 19,
        'phone': '+1 555-123-4567',
        'marks': 85,
        'pass': True
    },
    {
        'id': '402',
        'name': 'Rajesh Patel',
        'age': 20,
        'phone': '+91 98765 43210',
        'marks': 72,
        'pass': True
    },
    {
        'id': '403',
        'name': 'Emily Brown',
        'age': 18,
        'phone': '+44 20 7123 4567',
        'marks': 92,
        'pass': True
    },
    {
        'id': '404',
        'name': 'John Smith',
        'age': 21,
        'phone': '+1 555-765-4321',
        'marks': 78,
        'pass': True
    },
    {
        'id': '405',
        'name': 'Maria Garcia',
        'age': 22,
        'phone': '+34 600 123 456',
        'marks': 88,
        'pass': True
    },
    {
        'id': '406',
        'name': 'Chen Wei',
        'age': 19,
        'phone': '+86 138 0000 1234',
        'marks': 67,
        'pass': False
    },
    {
        'id': '407',
        'name': 'Sara Lee',
        'age': 20,
        'phone': '+61 2 9876 5432',
        'marks': 94,
        'pass': True
    },
    {
        'id': '408',
        'name': 'Nina Williams',
        'age': 22,
        'phone': '+33 1 70 18 99 68',
        'marks': 81,
        'pass': True
    },
    {
        'id': '409',
        'name': 'David Kim',
        'age': 19,
        'phone': '+82 10 1234 5678',
        'marks': 74,
        'pass': True
    },
    {
        'id': '410',
        'name': 'Sophia Martinez',
        'age': 21,
        'phone': '+52 55 1234 5678',
        'marks': 69,
        'pass': False
    }
    ]

    res=None
    for i in student_records_list:
        if i['id']==request.POST.get('id'):
            res=i
            break
    print(res)
    return render(request,'index.html',{'a':res})

