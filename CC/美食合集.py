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
"美食纪录片":"美食纪录片",
"大胃女王":"胃女王吃遍日本",
"漫游日本":"超清日本",
"漫步韩国":"漫步韩国",
"漫步台湾":"漫步台湾",
"荒野独居":"荒野独居",

            
            
"音乐":"音乐",
"全区排行榜":"电影",        
"MV首播":"MV首播",
"MV首播韩国":"MV首播韩国",        
"探索发现":"探索发现",
"荒野求生":"荒野求生",
"演唱会":"演唱会",
"综艺":"综艺",
"动物世界":"动物世界"


        }
       filter: {{"n":"Beyond","v":"beyond演唱会超清"},{"n":"坂井泉水","v":"坂井泉水演唱会超清"},{"n":"宝丽金","v":"宝丽金演唱会超清"},{"n":"布兰妮","v":"布兰妮演唱会超清"},{"n":"陈瑞","v":"陈瑞演唱会超清"},{"n":"陈奕迅","v":"陈奕迅演唱会超清"},{"n":"崔健","v":"崔健演唱会超清"},{"n":"Coldplay","v":"coldplay演唱会超清"},{"n":"陈慧娴","v":"陈慧娴演唱会超清"},{"n":"陈百强","v":"陈百强演唱会超清"},{"n":"陈淑桦","v":"陈淑桦演唱会超清"},{"n":"陈慧琳","v":"陈慧琳演唱会超清"},{"n":"邓丽君","v":"邓丽君演唱会超清"},{"n":"邓紫棋","v":"邓紫棋演唱会超清"},{"n":"刀郎","v":"刀郎演唱会超清"},{"n":"达明一派","v":"刘以达歌曲"},{"n":"费玉清","v":"费玉清演唱会超清"},{"n":"谷村新司","v":"谷村新司演唱会超清"},{"n":"郭富城","v":"郭富城演唱会超清"},{"n":"邰正宵","v":"邰正宵演唱会超清"},{"n":"关淑怡","v":"关淑怡演唱会超清"},{"n":"黄凯芹","v":"黄凯芹演唱会超清"},{"n":"黑豹乐队","v":"H黑豹乐队"},{"n":"降央卓玛","v":"降央卓玛演唱会超清"},{"n":"江慧","v":"江慧歌曲"},{"n":"吉永小百合","v":"吉永小百合歌曲"},{"n":"金庸","v":"金庸影视歌曲"},{"n":"刘德华","v":"刘德华演唱会超清"},{"n":"Lady Gaga","v":"Lady Gaga演唱会超清"},{"n":"龙飘飘","v":"龙飘飘演唱会超清"},{"n":"罗百吉","v":"罗百吉演唱会超清"},{"n":"罗大佑","v":"罗大佑演唱会超清"},{"n":"林志炫","v":"林志炫演唱会超清"},{"n":"林忆莲","v":"林忆莲演唱会超清"},{"n":"李知恩","v":"李知恩演唱会超清"},{"n":"梁静茹","v":"梁静茹演唱会超清"},{"n":"冷漠","v":"冷漠演唱会超清"},{"n":"李克勤","v":"李克勤演唱会超清"},{"n":"林子祥","v":"林子祥演唱会超清"},{"n":"黎明","v":"黎明演唱会超清"},{"n":"刘若英","v":"刘若英演唱会超清"},{"n":"McHotdog","v":"MC Hotdog演唱会超清"},{"n":"莫文蔚","v":"莫文蔚演唱会超清"},{"n":"孟庭苇","v":"孟庭苇演唱会超清"},{"n":"麦当娜","v":"麦当娜演唱会超清"},{"n":"迈克杰克逊","v":"迈克杰克逊演唱会超清"},{"n":"雅尼紫禁城","v":"雅尼紫禁城演唱会超清"},{"n":"潘越云","v":"潘越云演唱会超清"},{"n":"潘美辰","v":"潘美辰演唱会超清"},{"n":"齐秦","v":"齐秦演唱会超清"},{"n":"祁美云","v":"祁美云演唱会超清"},{"n":"任贤齐","v":"任贤齐演唱会超清"},{"n":"苏慧伦","v":"苏慧伦演唱会超清"},{"n":"唐朝乐队","v":"唐朝乐队"},{"n":"童安格","v":"童安格演唱会超清"},{"n":"TFBOYS","v":"TFBOYS演唱会超清"},{"n":"太极乐队","v":"太极乐队演唱会超清"},{"n":"唐朝摇滚","v":"唐朝摇滚演唱会超清"},{"n":"谭咏麟","v":"谭咏麟演唱会超清"},{"n":"王琪","v":"王琪歌曲"},{"n":"伍珂玥","v":"伍珂玥演唱会超清"},{"n":"王杰","v":"王杰演唱会超清"},{"n":"伍佰","v":"伍佰演唱会超清"},{"n":"温兆伦","v":"温兆伦演唱会超清"},{"n":"王菲","v":"王菲演唱会超清"},{"n":"熊天平","v":"熊天平演唱会超清"},{"n":"徐小凤","v":"徐小凤演唱会超清"},{"n":"席琳迪翁","v":"席琳迪翁演唱会超清"},{"n":"许嵩","v":"黄许嵩演唱会超清"},{"n":"许美静","v":"许美静演唱会超清"},{"n":"许冠杰","v":"许冠杰演唱会超清"},{"n":"小虎队","v":"小虎队演唱会超清"},{"n":"许巍","v":"许巍演唱会超清"},{"n":"叶启田","v":"叶启田演唱会超清"},{"n":"叶玉卿","v":"叶玉卿演唱会超清"},{"n":"杨千嬅","v":"杨千嬅演唱会超清"},{"n":"左麟右李","v":"左麟右李演唱会超清"},{"n":"赵传","v":"赵传演唱会超清"},{"n":"周华健","v":"周华健演唱会超清"},{"n":"周启生","v":"周启生演唱会超清"},{"n":"张信哲","v":"张信哲演唱会超清"},{"n":"周慧敏","v":"周慧敏演唱会超清"},{"n":"张碧晨","v":"张碧晨演唱会超清"},{"n":"中岛美雪","v":"中岛美雪演唱会超清"},{"n":"张学友","v":"张学友演唱会超清"},{"n":"猪哥亮","v":"猪哥亮歌曲"},{"n":"周杰伦","v":"周杰伦演唱会超清"},{"n":"周深","v":"周深演唱会超清"},{"n":"张蔷","v":"张蔷演唱会超清"},{"n":"张帝","v":"张帝演唱会超清"},{"n":"张国荣","v":"张国荣演唱会超清"},{"n":"郑钧","v":"郑钧演唱会超清"},{"n":"张楚","v":"张楚演唱会超清"},{"n":"张真","v":"张真演唱会超清"},{"n":"赵传","v":"赵传演唱会超清"},{"n":"周传雄","v":"周传雄演唱会超清"}]},{"key":"duration","name":"时长","value":[{"n":"全部","v":"0"},{"n":"60分钟以上","v":"4"},{"n":"30~60分钟","v":"3"},{"n":"10~30分钟","v":"2"},{"n":"10分钟以下","v":"1"}]}] },
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
            result['page'] = 1
            result['pagecount'] = 1
            result['limit'] = 90
            result['total'] = 999999
        return result
    def categoryContent(self,tid,pg,filter,extend):	
        result = {}
        if tid == "热门":
            return self.get_hot(pg=pg)
        if tid == "排行榜" :
            return self.get_rank()
        if tid == '动态':
            return self.get_dynamic(pg=pg)
        url = 'https://api.bilibili.com/x/web-interface/search/type?search_type=video&keyword={0}&page={1}'.format(tid,pg)
        if len(self.cookies) <= 0:
            self.getCookie()
        rsp = self.fetch(url,cookies=self.getCookie())
        content = rsp.text
        jo = json.loads(content)
        if jo['code'] != 0:			
            rspRetry = self.fetch(url,cookies=self.getCookie())
            content = rspRetry.text		
        jo = json.loads(content)
        videos = []
        vodList = jo['data']['result']
        for vod in vodList:
            aid = str(vod['aid']).strip()
            title = tid + ":" + vod['title'].strip().replace("<em class=\"keyword\">","").replace("</em>","")
            img = 'https:' + vod['pic'].strip()
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
    def cleanSpace(self,str):
        return str.replace('\n','').replace('\t','').replace('\r','').replace(' ','')
    def detailContent(self,array):
        aid = array[0]
        url = "https://api.bilibili.com/x/web-interface/view?aid={0}".format(aid)

        rsp = self.fetch(url,headers=self.header,cookies=self.getCookie())
        jRoot = json.loads(rsp.text)
        jo = jRoot['data']
        title = jo['title'].replace("<em class=\"keyword\">","").replace("</em>","")
        pic = jo['pic']
        desc = jo['desc']
        typeName = jo['tname']
        vod = {
            "vod_id":aid,
            "vod_name":title,
            "vod_pic":pic,
            "type_name":typeName,
            "vod_year":"",
            "vod_area":"bilidanmu",
            "vod_remarks":"",
            "vod_actor":jo['owner']['name'],
            "vod_director":jo['owner']['name'],
            "vod_content":desc
        }
        ja = jo['pages']
        playUrl = ''
        for tmpJo in ja:
            cid = tmpJo['cid']
            part = tmpJo['part']
            playUrl = playUrl + '{0}${1}_{2}#'.format(part,aid,cid)

        vod['vod_play_from'] = 'B站'
        vod['vod_play_url'] = playUrl

        result = {
            'list':[
                vod
            ]
        }
        return result
    def searchContent(self,key,quick):
        search = self.categoryContent(tid=key,pg=1,filter=None,extend=None)
        result = {
            'list':search['list']
        }
        return result
    def playerContent(self,flag,id,vipFlags):
        # https://www.555dianying.cc/vodplay/static/js/playerconfig.js
        result = {}

        ids = id.split("_")
        url = 'https://api.bilibili.com:443/x/player/playurl?avid={0}&cid=%20%20{1}&qn=112'.format(ids[0],ids[1])
        rsp = self.fetch(url,cookies=self.getCookie())
        jRoot = json.loads(rsp.text)
        jo = jRoot['data']
        ja = jo['durl']
        
        maxSize = -1
        position = -1
        for i in range(len(ja)):
            tmpJo = ja[i]
            if maxSize < int(tmpJo['size']):
                maxSize = int(tmpJo['size'])
                position = i

        url = ''
        if len(ja) > 0:
            if position == -1:
                position = 0
            url = ja[position]['url']

        result["parse"] = 0
        result["playUrl"] = ''
        result["url"] = url
        result["header"] = {
            "Referer":"https://www.bilibili.com",
            "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"
        }
        result["contentType"] = 'video/x-flv'
        return result

    config = {
        "player": {},
        "filter": {}
    }
    header = {}

    def localProxy(self,param):
        return [200, "video/MP2T", action, ""]
