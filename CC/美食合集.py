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
       filter: { "演唱会4K":[{"key":"order","name":"排序","value":[{"n":"综合排序","v":"0"},{"n":"最多点击","v":"click"},{"n":"最新发布","v":"pubdate"},{"n":"最多弹幕","v":"dm"},{"n":"最多收藏","v":"stow"}]},{"key":"tid","name":"分类","value":[{"n":"全部","v":"演唱会4K"},{"n":"A阿杜","v":"阿杜演唱会4K"},{"n":"A阿黛尔","v":"阿黛尔演唱会4K"},{"n":"BBeyond","v":"Beyond演唱会4K"},{"n":"BBy2","v":"By2演唱会4K"},{"n":"BBIGBANG","v":"BIGBANG演唱会4K"},{"n":"B布兰妮","v":"布兰妮演唱会4K"},{"n":"B坂井泉水","v":"坂井泉水演唱会4K"},{"n":"C陈奕迅","v":"陈奕迅演唱会4K"},{"n":"C蔡依林","v":"蔡依林演唱会4K"},{"n":"C初音未来","v":"初音未来演唱会4K"},{"n":"C蔡健雅","v":"蔡健雅演唱会4K"},{"n":"C陈小春","v":"陈小春演唱会4K"},{"n":"C草蜢","v":"草蜢演唱会4K"},{"n":"C陈慧娴","v":"陈慧娴演唱会4K"},{"n":"C崔健","v":"崔健演唱会4K"},{"n":"C仓木麻衣","v":"仓木麻衣演唱会4K"},{"n":"D戴荃","v":"戴荃演唱会4K"},{"n":"D动力火车","v":"动力火车演唱会4K"},{"n":"D邓丽君","v":"邓丽君演唱会4K"},{"n":"D丁当","v":"丁当演唱会4K"},{"n":"D刀郎","v":"刀郎演唱会4K"},{"n":"D邓紫棋","v":"邓紫棋演唱会4K"},{"n":"D戴佩妮","v":"戴佩妮演唱会4K"},{"n":"D邓丽君","v":"邓丽君演唱会4K"},{"n":"F飞儿乐队","v":"飞儿乐队演唱会4K"},{"n":"F费玉清","v":"费玉清演唱会4K"},{"n":"F费翔","v":"费翔演唱会4K"},{"n":"F方大同","v":"方大同演唱会4K"},{"n":"F房东的猫","v":"房东的猫演唱会4K"},{"n":"F凤飞飞","v":"凤飞飞演唱会4K"},{"n":"F凤凰传奇","v":"凤凰传奇演唱会4K"},{"n":"G郭采洁","v":"郭采洁演唱会4K"},{"n":"G光良","v":"光良演唱会4K"},{"n":"G郭静","v":"郭静演唱会4K"},{"n":"G郭富城","v":"郭富城演唱会4K"},{"n":"H胡彦斌","v":"胡彦斌演唱会4K"},{"n":"H胡夏","v":"胡夏演唱会4K"},{"n":"H韩红","v":"韩红演唱会4K"},{"n":"H黄品源","v":"黄品源演唱会4K"},{"n":"H黄小琥","v":"黄小琥演唱会4K"},{"n":"H花儿乐队","v":"花儿乐队演唱会4K"},{"n":"H黄家强","v":"黄家强演唱会4K"},{"n":"H后街男孩","v":"后街男孩演唱会4K"},{"n":"J经典老歌","v":"经典老歌演唱会4K"},{"n":"J贾斯丁比伯","v":"贾斯丁比伯演唱会4K"},{"n":"J金池","v":"金池演唱会4K"},{"n":"J金志文","v":"金志文演唱会4K"},{"n":"J焦迈奇","v":"焦迈奇演唱会4K"},{"n":"K筷子兄弟","v":"筷子兄弟演唱会4K"},{"n":"L李玟","v":"李玟演唱会4K"},{"n":"L林忆莲","v":"林忆莲演唱会4K"},{"n":"L李克勤","v":"李克勤演唱会4K"},{"n":"L刘宪华","v":"刘宪华演唱会4K"},{"n":"L李圣杰","v":"李圣杰演唱会4K"},{"n":"L林宥嘉","v":"林宥嘉演唱会4K"},{"n":"L梁静茹","v":"梁静茹演唱会4K"},{"n":"L李健","v":"李健演唱会4K"},{"n":"L林俊杰","v":"林俊杰演唱会4K"},{"n":"L李玉刚","v":"李玉刚演唱会4K"},{"n":"L林志炫","v":"林志炫演唱会4K"},{"n":"L李荣浩","v":"李荣浩演唱会4K"},{"n":"L李宇春","v":"李宇春演唱会4K"},{"n":"L洛天依","v":"洛天依演唱会4K"},{"n":"L林子祥","v":"林子祥演唱会4K"},{"n":"L李宗盛","v":"李宗盛演唱会4K"},{"n":"L黎明","v":"黎明演唱会4K"},{"n":"L刘德华","v":"刘德华演唱会4K"},{"n":"L罗大佑","v":"罗大佑演唱会4K"},{"n":"L林肯公园","v":"林肯公园演唱会4K"},{"n":"LLadyGaga","v":"LadyGaga演唱会4K"},{"n":"L旅行团乐队","v":"旅行团乐队演唱会4K"},{"n":"M莫文蔚","v":"莫文蔚演唱会4K"},{"n":"M毛不易","v":"毛不易演唱会4K"},{"n":"M梅艳芳","v":"梅艳芳演唱会4K"},{"n":"M迈克尔杰克逊","v":"迈克尔杰克逊演唱会4K"},{"n":"N南拳妈妈","v":"南拳妈妈演唱会4K"},{"n":"P朴树","v":"朴树演唱会4K"},{"n":"Q齐秦","v":"齐秦演唱会4K"},{"n":"Q青鸟飞鱼","v":"青鸟飞鱼演唱会4K"},{"n":"R容祖儿","v":"容祖儿演唱会4K"},{"n":"R任贤齐","v":"任贤齐演唱会4K"},{"n":"S水木年华","v":"水木年华演唱会4K"},{"n":"S孙燕姿","v":"孙燕姿演唱会4K"},{"n":"S苏打绿","v":"苏打绿演唱会4K"},{"n":"SSHE","v":"SHE演唱会4K"},{"n":"S孙楠","v":"孙楠演唱会4K"},{"n":"T陶喆","v":"陶喆演唱会4K"},{"n":"T谭咏麟","v":"谭咏麟演唱会4K"},{"n":"T田馥甄","v":"田馥甄演唱会4K"},{"n":"T谭维维","v":"谭维维演唱会4K"},{"n":"T逃跑计划","v":"逃跑计划演唱会4K"},{"n":"T田震","v":"田震演唱会4K"},{"n":"T谭晶","v":"谭晶演唱会4K"},{"n":"T屠洪刚","v":"屠洪刚演唱会4K"},{"n":"T泰勒·斯威夫特","v":"泰勒·斯威夫特演唱会4K"},{"n":"W王力宏","v":"王力宏演唱会4K"},{"n":"W王杰","v":"王杰演唱会4K"},{"n":"W吴克群","v":"吴克群演唱会4K"},{"n":"W王心凌","v":"王心凌演唱会4K"},{"n":"W汪峰","v":"汪峰演唱会4K"},{"n":"W伍佰","v":"伍佰演唱会4K"},{"n":"W王菲","v":"王菲演唱会4K"},{"n":"W五月天","v":"五月天演唱会4K"},{"n":"W汪苏泷","v":"汪苏泷演唱会4K"},{"n":"X徐佳莹","v":"徐佳莹演唱会4K"},{"n":"X弦子","v":"弦子演唱会4K"},{"n":"X萧亚轩","v":"萧亚轩演唱会4K"},{"n":"X许巍","v":"许巍演唱会4K"},{"n":"X薛之谦","v":"薛之谦演唱会4K"},{"n":"X许嵩","v":"许嵩演唱会4K"},{"n":"X小虎队","v":"小虎队演唱会4K"},{"n":"X萧敬腾","v":"萧敬腾演唱会4K"},{"n":"X谢霆锋","v":"谢霆锋演唱会4K"},{"n":"X徐小凤","v":"徐小凤演唱会4K"},{"n":"X信乐队","v":"信乐队演唱会4K"},{"n":"Y夜愿乐队","v":"夜愿乐队演唱会4K"},{"n":"Y羽泉","v":"羽泉演唱会4K"},{"n":"Y郁可唯","v":"郁可唯演唱会4K"},{"n":"Y叶倩文","v":"叶倩文演唱会4K"},{"n":"Y杨坤","v":"杨坤演唱会4K"},{"n":"Y庾澄庆","v":"庾澄庆演唱会4K"},{"n":"Y尤长靖","v":"尤长靖演唱会4K"},{"n":"Y易烊千玺","v":"易烊千玺演唱会4K"},{"n":"Y袁娅维","v":"袁娅维演唱会4K"},{"n":"Y杨丞琳","v":"杨丞琳演唱会4K"},{"n":"Y杨千嬅","v":"杨千嬅演唱会4K"},{"n":"Y杨宗纬","v":"杨宗纬演唱会4K"},{"n":"Z周杰伦","v":"周杰伦演唱会4K"},{"n":"Z张学友","v":"张学友演唱会4K"},{"n":"Z张信哲","v":"张信哲演唱会4K"},{"n":"Z张宇","v":"张宇演唱会4K"},{"n":"Z周华健","v":"周华健演唱会4K"},{"n":"Z张韶涵","v":"张韶涵演唱会4K"},{"n":"Z周深","v":"周深演唱会4K"},{"n":"Z纵贯线","v":"纵贯线演唱会4K"},{"n":"Z赵雷","v":"赵雷演唱会4K"},{"n":"Z周传雄","v":"周传雄演唱会4K"},{"n":"Z张国荣","v":"张国荣演唱会4K"},{"n":"Z周慧敏","v":"周慧敏演唱会4K"},{"n":"Z张惠妹","v":"张惠妹演唱会4K"},{"n":"Z周笔畅","v":"周笔畅演唱会4K"},{"n":"Z郑中基","v":"郑中基演唱会4K"},{"n":"Z张艺兴","v":"张艺兴演唱会4K"},{"n":"Z张震岳","v":"张震岳演唱会4K"},{"n":"Z张雨生","v":"张雨生演唱会4K"},{"n":"Z郑智化","v":"郑智化演唱会4K"},{"n":"Z卓依婷","v":"卓依婷演唱会4K"},{"n":"Z中岛美雪","v":"中岛美雪演唱会4K"}]},{"key":"duration","name":"时长","value":[{"n":"全部","v":"0"},{"n":"60分钟以上","v":"4"},{"n":"30~60分钟","v":"3"},{"n":"10~30分钟","v":"2"},{"n":"10分钟以下","v":"1"}]}] },
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
