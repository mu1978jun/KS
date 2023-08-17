#coding=utf-8
#!/usr/bin/python
import sys
sys.path.append('..') 
from base.spider import Spider
import json
import time
import base64

class Spider(Spider):  # 元类 默认的元类 type
    def getName(self):
        return "搭讪"
    def init(self,extend=""):
        print("============{0}============".format(extend))
        pass
    def isVideoFormat(self,url):
        pass
    def manualVideoCheck(self):
        pass
    def homeContent(self,filter):
        result = {}
        cateManual = {
"美食":"美食",
"披萨":"披萨",
"火锅":"火锅",
"烧烤":"烧烤",
"烤鱼":"烤鱼",
"海鲜":"海鲜",
"津菜":"津菜",
"川菜":"川菜",
"湘菜":"湘菜",
"鲁菜":"鲁菜",
"苏菜":"苏菜",
"闽菜":"闽菜",
"粤菜":"粤菜",
"东北菜":"东北菜",
"冀菜":"冀菜",
"豫菜":"豫菜",
"鄂菜":"鄂菜",
"本帮菜":"本帮菜",
"客家菜":"客家菜",
"赣菜":"赣菜",
"京菜":"京菜",
"浙菜":"浙菜",
"徽菜":"徽菜",
"湘菜":"湘菜",
"凉菜":"凉菜",
"蒸菜":"蒸菜",
"日料":"日料",
"点心":"点心",
"面食":"面食",
"汉堡":"汉堡",
"小吃":"小吃",
"素食":"素食",
"韩国菜":"韩国菜",
"泰国菜":"泰国菜",
"穆斯林菜":"穆斯林菜",
"土耳其菜系":"土耳其菜系",
"法国菜":"法国菜",
"意大利菜":"意大利菜",
"希腊菜":"希腊菜",
"德国菜":"德国菜",
"西班牙菜":"西班牙菜",
"阿拉伯菜":"阿拉伯菜",
"伊朗菜":"伊朗菜",
"中亚菜":"中亚菜",
"糖尿病菜":"糖尿病菜",
"早餐":"早餐"

        }
        classes = []
        for k in cateManual:
            classes.append({
                'type_name':k,
                'type_id':cateManual[k]
            })
        result['class'] = classes
        if(filter):
            result['filters'] = self.config['filter']
        return result
    def homeVideoContent(self):
        result = {
            'list':[]
        }
        return result
    cookies = ''
    def getCookie(self):
        import requests
        import http.cookies
        # 这里填cookie
        raw_cookie_line ="buvid3=8B57D3BA-607A-1E85-018A-E8C430023CED42659infoc; b_lsid=BEB8EE7F_18742FF8C2E; bsource=search_baidu; _uuid=DE810E367-B52C-AF6E-A612-EDF4C31567F358591infoc; b_nut=100; buvid_fp=711a632b5c876fa8bbcf668c1efba551; SESSDATA=7624af93%2C1696008331%2C862c8%2A42; bili_jct=141a474ef3ce8cf2fedf384e68f6625d; DedeUserID=3493271303096985; DedeUserID__ckMd5=212a836c164605b7; sid=5h4ruv6o; buvid4=978E9208-13DA-F87A-3DC0-0B8EDF46E80434329-123040301-dWliG5BMrUb70r3g583u7w%3D%3D"
        simple_cookie = http.cookies.SimpleCookie(raw_cookie_line)
        cookie_jar = requests.cookies.RequestsCookieJar()
        cookie_jar.update(simple_cookie)
        return cookie_jar
    def get_dynamic(self,pg):
        result = {}
        
        url= 'https://api.bilibili.com/x/polymer/web-dynamic/v1/feed/all?timezone_offset=-480&type=all&page={0}'.format(pg)
        
        rsp = self.fetch(url,cookies=self.getCookie())
        content = rsp.text
        jo = json.loads(content)
        if jo['code'] == 0:
            videos = []
            vodList = jo['data']['items']
            for vod in vodList:
                if vod['type'] == 'DYNAMIC_TYPE_AV':
                    ivod = vod['modules']['module_dynamic']['major']['archive']
                    aid = str(ivod['aid']).strip()
                    title = ivod['title'].strip().replace("<em class=\"keyword\">","").replace("</em>","")
                    img =  ivod['cover'].strip()
                    remark = str(ivod['duration_text']).strip()
                    videos.append({
                        "vod_id":aid,
                        "vod_name":title,
                        "vod_pic":img,
                        "vod_remarks":remark
                    })
                result['list'] = videos
                result['page'] = pg
                result['pagecount'] = 9999
                result['limit'] = 90
                result['total'] = 999999
        return result

    def get_hot(self,pg):
        result = {}
        url= 'https://api.bilibili.com/x/web-interface/popular?ps=20&pn={0}'.format(pg)
        rsp = self.fetch(url,cookies=self.getCookie())
        content = rsp.text
        jo = json.loads(content)
        if jo['code'] == 0:
            videos = []
            vodList = jo['data']['list']
            for vod in vodList:
                aid = str(vod['aid']).strip()
                title = vod['title'].strip().replace("<em class=\"keyword\">","").replace("</em>","")
                img =  vod['pic'].strip()
                remark = str(vod['duration']).strip()
                videos.append({
                    "vod_id":aid,
                    "vod_name":title,
                    "vod_pic":img,
                    "vod_remarks":remark
                })
            result['list'] = videos
            result['page'] = pg
            result['pagecount'] = 9999
            result['limit'] = 90
            result['total'] = 999999
        return result
    def get_rank(self):
        result = {}
        url= 'https://api.bilibili.com/x/web-interface/ranking/v2?rid=0&type=all'
        rsp = self.fetch(url,cookies=self.getCookie())
        content = rsp.text
        jo = json.loads(content)
        if jo['code'] == 0:
            videos = []
            vodList = jo['data']['list']
            for vod in vodList:
                aid = str(vod['aid']).strip()
                title = vod['title'].s
