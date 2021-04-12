# Hello world Program
from django.http import HttpResponse


def msg(request):
    return HttpResponse("<center><br><p><h2>Name: Ansh Mahendra Shrivas</h2> </p><br><p><h2>PRN: 1841049</h2></p><br><p><h2>Class: T.Y.Btech (Computer)</h2></p><br><h1>Hello World</h1></center>")
