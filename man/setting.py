#*-*coding:utf8*-*

"""
爬虫配置文件
============
"""
#爬虫运行方式
#可选类型:singleton,distributed
RUNNING_TYPE = 'singleton'


#调度器类型
#可选类型:singleton,redis,rabbitmq
SCHEDULER = 'singleton'
#调度器重试次数
SCHEDULER_RETRY_TIME = 5
#调度器重试间隔,单位秒
SCHEDULER_RETRY_INTERVAL = 1


#爬虫最大并发数
CONCURRENT_REQUESTS = 1
#请求休眠时间,单位秒
REQUEST_SLEEP_TIME = 1
#请求超时时间,单位秒
REQUEST_TIMEOUT = 2


#爬虫名
SPIDER_NAME     =   'demo'
#爬虫类型
SPIDER_TYPE     =   'rulelink'


#中间数据结果集前缀
MIDDLE_DATA_COLLECTION = 'rule'
#合并后结果集前缀
MERGE_DATA_COLLECTION = 'merge_result'
#持久化存储配置
LASTING         =   {
                        'type':'mongo',
                        'host':'172.18.4.52',
                        'port':'27017',
                        'password':'',
                        'timeout':5
                    }


#登录的headers
LOGIN_HEADER = {'DWRSESSIONID':'IvCebsu7Ifbcx*H5o*jyP','JSESSIONID':'abcbwytCNeNmn6E0J40pv','jsessionid':'CECE9ED64DAE21A218B284CE0E33E6AC','Hm_lvt_acbe332524305cf7430995bc4404a862':'1460101950','Hm_lpvt_acbe332524305cf7430995bc4404a862':'1460101950'}

#爬虫初始地址
FIRST_URLS       =   ['http://czy.jtyhjy.com/Jty/tbkt/getTbkt_currentBitCode_001001.shtm']
#页面爬取规则
PAGE1           =   {
                        #只能生成一种类型的数据,不能生成多种
                        #生成多种最好使用多个爬虫
                        'extract_data':
                        [
                            {
                                'type':'css', #reg #xpath
                                'expression':'div.tbkt_title > a.active > span',
                                'field':'subject',#想要抽取的数据必须有字段名,否则没法存储
                                'multiple':False
                            },
                            {
                                'type':'group_xpath', #reg #xpath
                                'group_expression':'//*[@id="mainContent"]/form/table[2]/tbody/tr/td/table/tbody/tr[2]/td/table/tbody/',
                                'expression':['tr[*]/td/table/tbody/tr/td[1]/a','tr[?0]/td/table/tbody/tr/td[2]/table/tbody/tr[*]/td[*]/a/text()'],#?只能匹配其父级的个数
                                #'extract_urls':'tr[?0]/td/table/tbody/tr/td[2]/table/tbody/tr[*]/td[*]/a/href()',
                                'field':['grade','edition'],#想要抽取的数据必须有字段名,否则没法存储
                                'parent':0,   
                                'multiple':True,
                                'associate':True#默认为False
                            }
                            #这里的列表可以产生多级数据

                        ],
                        'extract_urls':
                        {
                            'allow':r'/Jty/tbkt/getTbkt2_currentBitCode_\d{12}.shtm',
                            #'deny':r'http://news.sina.com.cn/china/',
                            #'headers':{'name':'zhangchunyang'},
                            #'cookies':{'user':'zhangchunyang'},#如果不指定，沿用上一页后的http头
                            #'method':'GET',
                            #'data':None,
                            #'nextPage'#翻页功能,获取到的url与当前平级
                        },
                        #'format_urls':
                        #{
                        #    'format_url':'http://format/%(name)s/%(age)d',
                        #    'format_data':{'name':{'type':'xpath','expression':'//*[@id="syncad_1"]/h1[1]/a/text()'},'age':range(1,2)},
                        #    #tuple也可以,这个填充format_url用的,两个的组合需要满足python中format的原则,type:regex,xpath,他们的记过必须是上方类型的元素或者包含上方元素的列表,默认为为字符串
                        #    'method': 'GET',
                        #    'data':{},
                        #    'headers':{'name':'zhangchunyang'},
                        #    'cookies':{'user':'zhangchunyang'},#如果不指定，沿用上一页后的http头
                        #},
                   }
PAGE2           =   {
                        'extract_data':
                        [
                            {
                                'type':'xpath', #reg #xpath
                                'expression':'//*[@id="mainContent"]/form/table[2]/tbody/tr/td/table/tbody/tr[1]/td[1]/text()',
                                'field':'unit',#想要抽取的数据必须有字段名,否则没法存储
                                'multiple':False,
                                'associate':False
                            },
                        ],
                        'extract_urls':
                        {           
                            'allow':r'/Jty/tbkt/getTbkt2_currentBitCode_\d{15}.shtm',
                        }
                    }
"""
PAGE3           =   {
                        'extract_urls':
                        {
                            'allow':r'/Jty/tbkt/getTbkt2_currentBitCode_\d{18}.shtm',
                        }
                    }
PAGE4           =   {
                        'extract_urls':
                        {
                            'allow':r'/Jty/tbkt/getTbkt2.action?currentBitCode=\d{21}',
                        }
                    }
PAGE5           =   {
                        'extract_urls':
                        {
                            'allow':r'/jty/tbkt/showDetail.action?articleId=\d*',
                        }
                    }
PAGE6           =   {
                        'extract_data':
                        {
                            'type':'xpath',
                            'expression':'//*[@id="mainContent"]/table[1]/tbody/tr/td'
                        }
                    }
"""
