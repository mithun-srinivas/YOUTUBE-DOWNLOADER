from flask import Flask,render_template,request
from pytube import YouTube 

SAVE_PATH = "E:/"
app = Flask(__name__)

@app.route('/')
def home():
   return render_template('index.html')

@app.route('/download',methods=["GET","POST"])
def download():
    if request.method == 'POST':
        link=request.form['link']
        yt = YouTube(link)
        stream = yt.streams.first() 
        title=yt.title
        thumbnail=yt.thumbnail_url
        print(thumbnail)
        stream.download('f:/')
        return render_template('afterdownload.html',title=title,url=thumbnail,location=SAVE_PATH)
    else:
        return "Error"
        
if __name__ == '__main__':
   app.run(host="0.0.0.0", port=5000, debug=True)