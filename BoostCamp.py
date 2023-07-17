from Worker import *
from WebAction import *
from OutputController import *

GetPage('https://nid.naver.com/oauth2.0/authorize?response_type=code&client_id=FuFWZDfBLaBvE2LUtT3Q&redirect_uri=https://www.boostcourse.org/neoid/naverCallback&state=1rqMFPk2WFiVOlJy&svctype=0')
MessageGetPage()
Sleep()
Login()
Sleep()