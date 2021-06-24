from wordcloud import WordCloud
from konlpy.tag import Hannanum
import matplotlib.pyplot as plt

class KakaoTextCloud:
    def __init__(self, wordPath):
        self.f = open(wordPath, 'r', encoding='utf-8')
        self.wordPath = wordPath
        self.hannanum = Hannanum()
        self.frequency = dict()
        self.run()

    def getContent(self, line):
        if "," in line:
            line = line[line.find(",") + 1:]
            if " : " in line:
                content = line[line.find(" : ") + 3:].strip('\n')
                return content
        return None

    def run(self):
        self.processing()
        sorted(self.frequency.items(), key=(lambda x: x[1]))
        self.f.close()

    def processing(self):
        index = 0
        while True:
            index += 1
            line = self.f.readline()
            if not line: break
            content = self.getContent(line)
            if content is not None:
                for text in self.hannanum.nouns(content):
                    if text in self.frequency:
                        self.frequency[text] += 1
                    else:
                        self.frequency[text] = 1



if __name__ == '__main__':
    kakao = KakaoTextCloud("KakaoTalkChats.txt")
    wc = WordCloud(width=1000, height=600, background_color="white", random_state=0, font_path=r'c:\Windows\Fonts\malgun.ttf')
    plt.imshow(wc.generate_from_frequencies(kakao.frequency))
    plt.axis("off")
    plt.savefig('./textCloud.png')
    f = open("TextFrequency.txt", 'w', encoding='utf-8')
    f.write(str(kakao.frequency))
    f.close()