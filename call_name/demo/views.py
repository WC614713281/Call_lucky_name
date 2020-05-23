from django.shortcuts import render
from django.views import View
import random
from demo.models import Students

# Create your views here.


class CompleteView(View):

    def get(self, request):
        student_id = request.GET.get('student_id', 0)

        try:
            student = Students.objects.get(id=student_id)
        except Students.DoesNotExist:
            return render(request, 'roll.html')
        else:
            student.is_mark = True
            student.save()
            return render(request, 'complete.html', {'student': student})


class CallTheRollView(View):

    def get(self, request):
        num = random.randint(1, 61)

        try:
            student = Students.objects.get(id=num, is_mark=False)
        except Students.DoesNotExist:
            student = {'name': '查无此人'}

        return render(request, 'roll.html', {'student': student})


class ShowRollView(View):

    def get(self, request):
        return render(request, 'roll.html')
