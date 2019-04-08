from crawl_qq import QQmusicSpider
from crawl_kuwo import KuwoSpider
from crawl_kugou import KugouSpider

def get_music(search_key):
    qq_music = QQmusicSpider().search_music(search_key)
    kuwo_music = KuwoSpider().search_music(search_key)
    kugou_music = KugouSpider().search_music(search_key)
    print(kugou_music)

    all_platform = {

    }
    for platform_item in [qq_music,kuwo_music,kugou_music]:
        for item in platform_item:
            pass

    pass

if __name__ == '__main__':
    key = '孤独探戈'
    a = get_music(key)
    print(a)
