from django.test import TestCase

# Create your tests here.


# <!-- <div class="pagination">
#     <span class="step-links">
#         {% if page_obj.has_previous %}
#             <a href="?page=1">&laquo; first</a>
#             <a href="?page={{ page_obj.previous_page_number }}">previous</a>
#         {% endif %}

#         <span class="current">
#             Page {{ page_obj.number }} of {{ page_obj.paginator.num_pages }}.
#         </span>

#         {% if page_obj.has_next %}
#             <a href="?page={{ page_obj.next_page_number }}">next</a>
#             <a href="?page={{ page_obj.paginator.num_pages }}">last &raquo;</a>
#         {% endif %}

#     </span>
# </div> -->




# from django.contrib.sessions.backends.db import SessionStore as DbSessionStore

# class SessionStore(DbSessionStore):
#     def __init__(self, *args, **kwargs):
#         print 'hello from SessionStore'
#         super(SessionStore, self).__init__(*args, **kwargs)
# settings.py:

# SESSION_ENGINE='tcore.my_sessions'