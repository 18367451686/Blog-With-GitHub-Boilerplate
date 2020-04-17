# -*- coding: utf-8 -*-
"""博客构建配置文件
"""
<script>
(function(){
    var bp = document.createElement('script');
    var curProtocol = window.location.protocol.split(':')[0];
    if (curProtocol === 'https') {
        bp.src = 'https://zz.bdstatic.com/linksubmit/push.js';
    }
    else {
        bp.src = 'http://push.zhanzhang.baidu.com/push.js';
    }
    var s = document.getElementsByTagName("script")[0];
    s.parentNode.insertBefore(bp, s);
})();
</script>
# For Maverick
site_prefix = "/"
source_dir = "../src/"
build_dir = "../dist/"
index_page_size = 10
archives_page_size = 20
template = {
    "name": "Galileo",
    "type": "local",
    "path": "../Galileo"
}
enable_jsdelivr = {
    "enabled": False,
    "repo": ""
}

# 站点设置
site_name = "鼎天技术博客"
site_logo = "https://frontpage.dtnetwork.top/images/logo.jpg"
site_build_date = "2019-12-18T16:51+08:00"
author = "dtnetwork"
email = "dtnetwork@yeah.net"
author_homepage = "https://frontpage.dtnetwork.top/"
description = "长期免费的技术分享网站"
key_words = ['鼎天网络', 'dtnetwork', '鼎天网络科技工作室', '鼎天网络博客', '鼎天工作室博客']
language = 'zh-CN'
external_links = [
    {
        "name": "dtnetwork",
        "url": "https://github.com/AlanDecode/Maverick",
        "brief": "🏄‍ Go My Own Way."
    },
    {
        "name": "鼎天网络博客",
        "url": "https://www.imalan.cn",
        "brief": "鼎天网络博客的主页。"
    }
]
nav = [
    {
        "name": "首页",
        "url": "${site_prefix}",
        "target": "_self"
    },
    {
        "name": "归档",
        "url": "${site_prefix}archives/",
        "target": "_self"
    },
    {
        "name": "关于",
        "url": "${site_prefix}about/",
        "target": "_self"
    }
]

social_links = [
    {
        "name": "Twitter",
        "url": "https://twitter.com",
        "icon": "gi gi-twitter"
    },
    {
        "name": "GitHub",
        "url": "https://github.com",
        "icon": "gi gi-github"
    },
    {
        "name": "Weibo",
        "url": "https://www.weibo.com/u/6305348942",
        "icon": "gi gi-weibo"
    }
]

head_addon = r'''
<meta http-equiv="x-dns-prefetch-control" content="on">
<link rel="dns-prefetch" href="//cdn.jsdelivr.net" />
'''

footer_addon = ''

body_addon = ''
