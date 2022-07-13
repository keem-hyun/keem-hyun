import feedparser

keemhyun_blog_rss_url="https://keem.tistory.com/rss" 
rss_feed = feedparser.parse(keemhyun_blog_rss_url)

MAX_POST_NUM = 10

latest_blog_post_list = ""

MAX_POST_NUM = 10

for idx, feed in enumerate(rss_feed['entries']):
    if idx > MAX_POST_NUM:
        break
    feed_date = feed['published_parsed']
    latest_blog_post_list += f"[{feed_date.tm_year}/{feed_date.tm_mon}/{feed_date.tm_mday} - {feed['title']}]({feed['link']}) <br>\n"
    
markdown_text = """## ABOUT ME 👋
I wanna be a cloud engineer.

📩 Contact Email : hw813@naver.com

💻 Tech Blog : https://keem.tistory.com/

[![Top Langs](https://github-readme-stats.vercel.app/api/top-langs/?username=keem-hyun&layout=compact&theme=merko)](https://github.com/anuraghazra/github-readme-stats)
![Anurag's GitHub stats](https://github-readme-stats.vercel.app/api?username=keem-hyun&show_icons=true&theme=merko)
[![Solved.ac Profile](http://mazassumnida.wtf/api/v2/generate_badge?boj=hurrush)](https://solved.ac/hurrush/)

Latest Blog Post
"""

readme_text = f"{markdown_text}{latest_blog_post_list}"

with open("README.md", 'w', encoding='utf-8') as f:
    f.write(readme_text)
