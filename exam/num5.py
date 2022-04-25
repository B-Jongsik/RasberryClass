from urllib.parse import urlparse

def domain_name1(s):
    parts = urlparse(s)
    print('반환 도메인 이름 : ', parts.netloc)


domain_name1('http://github.com/carbonfive/raygun')
domain_name1('http://google.com/')