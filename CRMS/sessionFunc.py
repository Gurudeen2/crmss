from datetime import datetime

def sessions(request):
    now = datetime.now()
    convToDate = datetime.strptime(request.session["last_login"], "%Y-%m-%d %H:%M:%S.%f")
    print("NEW DATE FORMAT", type(convToDate))
    dateDiffInSecs = (now - convToDate).seconds
    if dateDiffInSecs >600:
        request.session['username']=""

key = 'django-insecure-l*971$#y*%-!-y)ppqk2(s168#v-ve^tv)payphucw*a%^i&lx'

# class CustomMiddleware:
#     def __init__(self, get_response):
#         self.get_response = get_response

#     def __call__(self, request):
#         request.session['a'] ='akee'
#         print("custom middleware before next middleware/view")
#             # Code to be executed for each request before
#             # the view (and later middleware) are called.

#         response = self.get_response(request.session['a'])

#         # Code to be executed for each request after
#             # the view are called.
#         print("custom middlewar", response)
            
#         return response

# # class sessionExpire:
#     # def process_request(self, request):

#     #     last_activity = request.session["last_activity"] 
#     # def process_response(self, request, response):
#     #     last_activity = request.session["last_activity"] 
#     #     now = datetime.now()
#     #     if (now-last_activity).minutes > 5:
#     #             #session expired
#     #         messages.success(request, "Session Expire, You are logout")
#     #     return HttpResponseRedirect("login")