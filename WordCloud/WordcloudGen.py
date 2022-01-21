from wordcloud import WordCloud, STOPWORDS
import wikipedia

stop_words = set(STOPWORDS)
info = wikipedia.summary("Pakistan")

word_cloud = WordCloud(background_color='white', stopwords=stop_words).generate(info)

word_cloud.to_file('D:\\Project\\XflowInternship\\WordCloud\\wordcloud.png')