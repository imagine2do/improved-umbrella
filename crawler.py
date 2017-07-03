from bs4 import BeautifulSoup
import urllib.request


output_file_name = 'output.txt'

URL = 'http://news.naver.com/main/read.nhn?mode=LSD&mid=shm&sid1=105&oid=014&aid=0003837940'


def get_text(URL):
    source_code_from_URL = urllib.request.urlopen(URL)
    soup = BeautifulSoup(source_code_from_URL, 'lxml', from_encoding='utf-8')
    text = ''
    for item in soup.find_all('div', id='articleBodyContents'):
        text = text + str(item.find_all(text=True))
    return text


def main():
    open_output_file = open(output_file_name, 'w')
    result_text = get_text(URL)
    open_output_file.write(result_text)
    open_output_file.close()

if __name__ == '__main__':
    main()
