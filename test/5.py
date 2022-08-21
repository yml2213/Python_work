import json
import requests

url = "https://huodong.fanli.com/sign82580/ajaxMainInit"

payload = {}
headers = {
    'Host': 'huodong.fanli.com',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 12; M2102J2SC Build/SKQ1.211006.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.104 Mobile Safari/537.36 Fanli/7.19.28.6 (ID:2-560135116-66740356908189-4-0; WVC:WV; SCR:1080*2340-2.75)',
    'X-Requested-With': 'XMLHttpRequest',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://huodong.fanli.com/sign82580?spm=page_name.h5.pty-entrance~module-apphomiconxin~std-82580&devid=66740356908189&c_aver=1.0&c_src=2&c_v=7.19.28.6&abtest=61747_c-26_d-2510_b-316_b-404_b-156_b-294_b-30_d-162_a-824_a-1154_b-586_d-206_b-12_b-6_b-48_b-70_b-12_a-148_b-76_b-166_a-78_a-2_f-14_b-4_b-52_c-36_a-18_b-8_a-26_b-2_b-54_a-2_b-30_b-52_a-12_b-8_a-4_b-22_b-14_a-20_b-18_b-32_b-38_a-2_a-2_c-20_a-16_b-4_b-6_b-2_b-4_b-0d3e&c_nt=wifi&mc=4&ci=%7B%5C%22ud%5C%22%3A%5C%22from%3Ddb%26local%3Dmapp_activity%26id%3D458241%26id_type%3Dactivity%5C%22%7D',
    'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
    'Cookie': '__utmo=2349992041.460729466.922585781; __utmp=2349992041.460729466.3609735018; FirstUrl=//m.fanli.com/; LandingUrl=https%3A//m.fanli.com/landingapp/chinamobilev2%3Fdevid%3D66740356908189%26c_aver%3D1.0%26c_src%3D2%26c_v%3D7.19.28.6%26abtest%3D61747_d-26_d-3230_b-480_d-162_a-824_a-1154_b-792_b-12_b-6_b-48_b-70_b-236_b-166_a-78_a-2_f-18_b-52_c-36_a-18_b-2_b-6_a-26_b-2_b-54_a-2_b-30_a-52_a-12_b-12_b-56_b-50_b-40_a-38_b-4_b-8_b-dc05%26c_nt%3Dwifi%26mc%3D4; __utmv=132E95C1-FD89-4367-97A4-752F9F799048; Hm_lvt_545c20cb01a15219bfeb0d1f103f99c1=1660972766; prouserid=560135116; prousername=1533995668320220820995; prousernameutf=1533995668320220820995; loginverify=78926940c74ce180; prolong=1660972778; PHPSESSID=92884d228df07d37d4998d366af923d9; _fl_huodong_89933_libao_status=1; _fl_sign82580_has_calendar=1; __utmt=36128d-37160c-38780b-46553b-48835b-55010b-56834b-57140b-60857a-65881b-72211b-72720b-77468b-77533b-79279b-80688b-81959f-82838a-83304a-83790b-83800b-84569a-84670c-84959a-85122a-85323b-85401b-85503b-85890a-86147b-86276b-86432b-86698b-86853b-87292b-87574a-87852b-88057c-88630a-89119a-89590b-89650a-89722b-89749b-89917b; Hm_lpvt_545c20cb01a15219bfeb0d1f103f99c1=1660985882; __fl_trace_cpc=AC9B4281-C6EA-4690-A40A-18C03555DE60'
}

response = requests.request("GET", url, headers=headers, data=payload)

re = eval("u"+"\'"+response.text+"\'")
print(re)
