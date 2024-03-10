import { Crypto, load, _ } from './lib/cat.js';

    let siteUrl = 'https://v.nmvod.cn';
    let siteKey = '';
    let siteType = 0;
    let headers = {
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1',
        'Referer': siteUrl + '/'
    };
    
    let jxUrl = ['https://api.cnmcom.com/webcloud/nmsvip.php?url=','https://api.cnmcom.com/webcloud/nmsssvip.php?vid=', 'https://api.cnmcom.com/webcloud/nmssvip.php?url=', 'https://api.cnmcom.com/webcloud/m3u8.php?url='];
    async function request(reqUrl, postData, post) {

        let res = await req(reqUrl, {
            method: post ? 'post' : 'get',
            headers: headers,
            data: postData || {},
            postType: post ? 'form' : '',
        });

        let content = res.content;
        return content;
    }

    async function init(cfg) {
        siteKey = cfg.skey;
        siteType = cfg.stype;
        if (cfg.ext) {
            siteUrl = cfg.ext;
        }
    }

    async function home(filter) {
        let classes = [{
            type_id: '1',
            type_name: '电影',
        },{
            type_id: '2',
            type_name: '剧集',
        },{
            type_id: '3',
            type_name: '综艺',
        },{
            type_id: '4',
            type_name: '动漫',
        },{
            type_id: '26',
            type_name: '短剧',
        }];
        let filterObj = genFilterObj();
        return JSON.stringify({
            class: classes,
            filters: filterObj
        });
    }

    async function homeVod() {
        let url = siteUrl;
        let videos = await getRecommend(url);
        return JSON.stringify({
            list: videos,
        });
    }

    async function category(tid, pg, filter, ext) {
        if (!pg) pg = 1;
        if (pg <= 0) pg = 1;

        let id = ext['id'] || tid;
        let year = ext['year'] || '';
        let area = ext['area'] || '';
        let url = siteUrl + '/index.php?m=vod-list-id-'+id+'-pg-'+pg+'-order--by-time-class-0-year-'+year+'-letter--area-'+area+'-lang-.html';
        
        let videos = await getVideos(url);
        return JSON.stringify({
            list: videos,
            page: pg,
        });
    }

    async function detail(id) {
        try {
            const html = await request(siteUrl + id);
            let $ = load(html);
            let content = $('article > p').text();
            let director = _.map($('section.page-bd > div:nth-child(2) > a'), (n) => {
                return $(n).text();
            }).join(' ');
            let actor = _.map($('section.page-bd > div:nth-child(3) > a'), (n) => {
                return $(n).text();
            }).join(' ');

            let play1Url = siteUrl + $('div.page-btn > span:nth-child(1) > a').attr('href');
            $ = load(await request(play1Url));
            let nameUrls = $('section.main > div > script:nth-child(1)').text().split("mac_url='")[1].split("';")[0];
            let playUrls = [];
            let playFroms = [];
            if($('div.hd > ul > li > a').text().indexOf('云播') >= 0) {
                playFroms.push('云播');
                playUrls.push(nameUrls.replaceAll('$', '$' + jxUrl[3]));
            } else {
                for(let i=1;i<=3;i++) {
                    playFroms.push('线路' + i);
                    playUrls.push(nameUrls.replaceAll('$', '$'+jxUrl[i-1]));
    
                }
            }
            
            const video = {
                vod_play_from: playFroms.join('$$$'),
                vod_play_url: playUrls.join('$$$'),
                vod_content: '公众号：【蚂蚁科技杂谈】' +content,
                vod_director: director,
                vod_actor: actor,
            };
            const list = [video];
            const result = { list };
            return JSON.stringify(result);
        } catch (e) {
        console.log('err', e);
        }
        return null;
    }

    async function search(wd, quick, pg) {
        let url = siteUrl + '/index.php?m=vod-search';
        const html = await request(url, {wd: wd}, true);
        const $ = load(html);
        let data = $('#data_list > li');
        let videos = _.map(data, (n) => {
            let id = $($(n).find('div.pic > a')[0]).attr('href');
            let pic = $($(n).find('div.pic > a > img')[0]).attr('data-src');
            let name = $($(n).find(' span.sTit')[0]).text();
            return {
                vod_id: id,
                vod_name: name,
                vod_pic: pic,
                vod_remarks: '',
            };
        });
        return JSON.stringify({
            list: videos,
        });
    }

    async function play(flag, id, flags) {
        let playUrl = id;
        const html = await request(playUrl);
        const $ = load(html);
        for(const n of $('script')) {
            if($(n).text().indexOf("url: '") >= 0) {
                let url = $(n).text().split("url: '")[1].split("'")[0];
                if(url) {
                    playUrl = url;
                }
                return JSON.stringify({
                    parse: 0,
                    url: playUrl,
                });
            }
            if($(n).text().indexOf("var url='") >= 0) {
                let url = $(n).text().split("var url='")[1].split("';")[0];
                if(url) {
                    playUrl = url;
                }
                return JSON.stringify({
                    parse: 0,
                    url: playUrl,
                });
            }
        }
        return JSON.stringify({
            parse: 1,
            url: playUrl,
        });
    }

    function genFilterObj() {
        return {
            '1': [{'key': 'id', 'name': '类型', 'value': [{'n': '全部类型', 'v': '1'}, {'n': '动作', 'v': '5'}, {'n': '喜剧', 'v': '6'}, {'n': '爱情', 'v': '7'}, {'n': '科幻', 'v': '8'}, {'n': '恐怖', 'v': '9'}, {'n': '剧情', 'v': '10'}, {'n': '战争', 'v': '11'},{'n': '惊悚', 'v': '16'},{'n': '奇幻', 'v': '17'}]}, 
                {'key': 'area', 'name': '地区', 'value': [{'n': '全部地区', 'v': ''}, {'n': '大陆', 'v': '大陆'}, {'n': '香港', 'v': '香港'}, {'n': '台湾', 'v': '台湾'}, {'n': '美国', 'v': '美国'}, {'n': '韩国', 'v': '韩国'},{'n': '日本', 'v': '日本'}]}, 
                {'key': 'year', 'name': '年份', 'value': [{'n': '全部年份', 'v': ''}, {'n': '2023', 'v': '2023'}, {'n': '2022', 'v': '2022'}, {'n': '2021', 'v': '2021'}, {'n': '2020', 'v': '2020'}, {'n': '2019', 'v': '2019'}, {'n': '2018', 'v': '2018'}, {'n': '2017', 'v': '2017'}, {'n': '2016', 'v': '2016'}, {'n': '2015', 'v': '2015'}, {'n': '2014', 'v': '2014'}, {'n': '2013', 'v': '2013'}, {'n': '2012', 'v': '2012'}, {'n': '2011', 'v': '2011'}, {'n': '2010', 'v': '2010'}]}
            ], 
            '2': [{'key': 'id', 'name': '类型', 'value': [{'n': '全部类型', 'v': '2'}, {'n': '国产剧', 'v': '12'}, {'n': '港台剧', 'v': '13'},{'n': '日韩剧', 'v': '14'}, {'n': '欧美剧', 'v': '15'}]}, 
                {'key': 'area', 'name': '地区', 'value': [{'n': '全部地区', 'v': ''}, {'n': '大陆', 'v': '大陆'}, {'n': '台湾', 'v': '台湾'}, {'n': '香港', 'v': '香港'}, {'n': '韩国', 'v': '韩国'}, {'n': '日本', 'v': '日本'}, {'n': '美国', 'v': '美国'}, {'n': '泰国', 'v': '泰国'}, {'n': '英国', 'v': '英国'}, {'n': '新加坡', 'v': '新加坡'}, {'n': '其他', 'v': '其他'}]},
                {'key': 'year', 'name': '年份', 'value': [{'n': '全部年份', 'v': ''}, {'n': '2023', 'v': '2023'}, {'n': '2022', 'v': '2022'}, {'n': '2021', 'v': '2021'}, {'n': '2020', 'v': '2020'}, {'n': '2019', 'v': '2019'}, {'n': '2018', 'v': '2018'}, {'n': '2017', 'v': '2017'}, {'n': '2016', 'v': '2016'}, {'n': '2015', 'v': '2015'}, {'n': '2014', 'v': '2014'}, {'n': '2013', 'v': '2013'}, {'n': '2012', 'v': '2012'}, {'n': '2011', 'v': '2011'}, {'n': '2010', 'v': '2010'}, {'n': '2009', 'v': '2009'}, {'n': '2008', 'v': '2008'}, {'n': '2006', 'v': '2006'}, {'n': '2005', 'v': '2005'}]}
            ]
        };
    }

    async function getRecommend(url) {
        const html = await request(url);
        const $ = load(html);
        const cards = $('div > ul.resize_list > li:nth-child(2)')
        let videos = _.map(cards, (n) => {
            let id = $($(n).find('a')[0]).attr('href');
            let name = $($(n).find('a')[0]).attr('title');
            let pic = $($(n).find('img')[0]).attr('src');
            let remarks = $($(n).find('span.sBottom > span')[0]).text().trim().replaceAll('0.0', '');
            return {
                vod_id: id,
                vod_name: name,
                vod_pic: pic,
                vod_remarks: remarks,
            };
        });
        return videos;
    }

    async function getVideos(url) {
        const html = await request(url);
        const $ = load(html);
        const cards = $('div > ul.resize_list > li')
        let videos = _.map(cards, (n) => {
            let id = $($(n).find('a')[0]).attr('href');
            let name = $($(n).find('a')[0]).attr('title');
            let pic = $($(n).find('img')[0]).attr('src');
            let remarks = $($(n).find('span.sBottom > span > em')[0]).text().trim();
            return {
                vod_id: id,
                vod_name: name,
                vod_pic: pic,
                vod_remarks: remarks,
            };
        });
        return videos;
    }

    export function __jsEvalReturn() {
        return {
            init: init,
            home: home,
            homeVod: homeVod,
            category: category,
            detail: detail,
            play: play,
            search: search,
        };
    }
