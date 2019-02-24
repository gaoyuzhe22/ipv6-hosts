'''
# import re
# def validate_domain(domain):
    # pattern = '^((?!-)[*A-Za-z0-9-]{1,63}(?<!-)\\.)+[A-Za-z]{2,6}$'
    # p = re.compile(pattern)
    # m = p.match(domain)
    # if m:
        # return True
    # else:
        # return False
		
# if validate_domain('www.google.com'):
    # print('yes')
import os
import sys
import re
import socket
import ipaddress
import getopt
import threading
import subprocess
import shlex
import time
import select
import requests

def validate_ip_addr(ip_addr):
    if ':' in ip_addr:
        try:
            socket.inet_pton(socket.AF_INET6, ip_addr)
            return True
        except socket.error:
            return False
    else:
        try:
            socket.inet_pton(socket.AF_INET, ip_addr)
            return True
        except socket.error:
            return False
            
def query_domain(domain):
    # cmd = "dig +short +time=2 -6 %s @'%s' '%s'"\
        # % (config['querytype'], config['dns'], domain)

    # if tcp:
        # cmd = cmd + ' +tcp'

    # proc = subprocess.Popen(shlex.split(cmd), stdout=subprocess.PIPE)
    # out, _ = proc.communicate()
    # outarr = out.decode('utf-8').splitlines()

    # cname = ip = ''
    # for v in outarr:
        # if cname == '' and validate_domain(v[:-1]):
            # cname = v[:-1]
        # if ip == '' and validate_ip_addr(v):
            # ip = v
            # break


    # url = 'https://dns.google.com/resolve?name=%s&type=%s&edns_client_subnet=202.40.161.203'%(domain,'aaaa')
    # counter=0
    # code=2
    # noblock=0
    # # ip=''
    # # www=''
    # while(counter<10):
        # counter=counter+1
        # r = requests.get(url)
        # code=r.status_code
        # if code == 200 : #int
            # rj=r.json()
            # if 'Answer' in rj:
                # ip=rj['Answer'][0]['data']
                # www=rj['Answer'][0]['name']
                # if validate_ip_addr(ip):
                    # s = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
                    # s.settimeout(1)
                    # tcp_flag=s.connect_ex((ip, 443))
                    # if tcp_flag==0:
                        # s.close()
                        # return ip
                    # else:
                        # s.close()
            # else:
                # break
    # return 
    
    counter=0
    code=2
    ipad=203
    while(counter<10):
        ipad=ipad+counter
        url = 'https://dns.google.com/resolve?name=%s&type=%s&edns_client_subnet=202.40.161.%s'%(domain,'aaaa',ipad)
        counter=counter+1
        r = requests.get(url)
        code=r.status_code
        if code == 200 : #int
            rj=r.json()
            if 'Answer' in rj:
                for pos in rj['Answer']:
                    if 'data' in pos:
                        ip=pos['data']
                        www=pos['name']
                        tcp_flag=ip_available(ip)
                        if tcp_flag==0:
                            return ip
                
                # if validate_ip_addr(ip):
                    # s = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
                    # s.settimeout(1)
                    # tcp_flag=s.connect_ex((ip, 443))
            else:
                break
    return

def ip_available(ip):
    if validate_ip_addr(ip):
        s = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
        s.settimeout(2)
        tcp_flag=s.connect_ex((ip, 443))
        s.close()
        return tcp_flag    

ffff=query_domain('blog.google')
print(ffff)
if ffff:
    print('ee')


# domain='www.google.com'
# url = 'https://dns.google.com/resolve?name=%s&type=%s&edns_client_subnet=175.45.20.138'%(domain,'aaaa')
# counter=0
# code=2
# noblock=0
# # ip=''
# # www=''
# while(counter<3):
    # counter=counter+1
    # r = requests.get(url)
    # print(r)
    # code=r.status_code
    # print(code)
    # if code == 200 : #int
        # rj=r.json()
        # if 'Answer' in rj:
            # ip=rj['Answer'][0]['data']
            # www=rj['Answer'][0]['name']
            # if validate_ip_addr(ip):
                # s = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
                # s.settimeout(1)
                # tcp_flag=s.connect_ex((ip, 443))
                # if tcp_flag==0:
                    # s.close()
                    # print(ip)
                # else:
                    # s.close()
        # else:
            # print('no answer')
            # break
# print('none')
'''
# def gyz(zydy):
    # zyy=global set()
    # zyy.add('%s'%(zydy))
    # print(zyy)

# gyz('love')
# gyz('love1')
# gyz('love2')
# print(zyy)

import requests

# google dns, edns 
# QUAD9 dns,
# cloudflare dns

url_params = {'name':'www.google.com','type':'aaaa','edns_client_subnet':'211.220.194.0'}
url='https://dns.google.com/resolve'
# url='https://9.9.9.9/dns-query'
r = requests.get(url,params = url_params).json()
print(r)