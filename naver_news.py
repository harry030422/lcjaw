from bs4 import BeautifulSoup
import urllib.request

FILE ='naver_news.txt'
URL = "http://news.naver.com/main/hotissue/sectionList.nhn?sid1=101&mid=hot&viewType=pc&cid=996387&nh=20180414145736"

def get_text(URL):
    source = urllib.request.urlopen(URL)
    soup = BeautifulSoup(source, 'lxml', from_encoding='utf-8')
    text=''
    for item in soup.find_all('div',id='articleBodyContents'):
        text += str(item.find_all(text=True))
        =
    return text

def main():
    open_output_file = open(FILE,'w')
    result_text = get_text(URL)
    open_output_file.write(result_text)
    print(result_text)
    open_output_file.close()
    print(result_text)
main()
