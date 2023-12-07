import time

from django.http import HttpResponse
import os


def into(request):
    #input
    print(str(request.POST.get('content')))
    output = open('../t2m_app/input.txt', 'a+')
    if str(request.POST.get('content')) != 'None':
        output.writelines(str(request.POST.get('content'))+os.linesep)

    #train
    # os.system('python gen_motion_script.py --name Comp_v6_KLD01 --text_file input.txt --repeat_time 3 --ext customized --gpu_id -1')
    # time.sleep(60)

    #output
    dir_list = sorted(os.listdir('../t2m_app/eval_results/t2m/Comp_v6_KLD01/customized/animations/C000/'))
    f = open('../t2m_app/eval_results/t2m/Comp_v6_KLD01/customized/animations/C000/%s' %dir_list[0], 'rb')
    return HttpResponse(f.read(), content_type='video/mp4')

# /Users/gaozheng/Documents/1.Neu/10.Project/1.HMG/11/t2m_app/eval_results/t2m/Comp_v6_KLD01/customized/animations/C000/gen_motion_00_L080_00_a.mp4
def index(request):
    return HttpResponse("""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Title</title>
    </head>
    <body>
    <form action="/into/" method="post">
        <h1>Title</h1>
        <div>
            content:
            <input type="text" name="content">
        </div>
    
        <div>
            <input type="submit" value="提交">
        </div>
    
    </form>
    </body>
    """)
