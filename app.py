from flask import Flask,render_template,request
from script import conversion
import os

from summary import summarize

app=Flask(__name__)

@app.route('/convert',methods=['POST','GET'])
def convert():
    if request.args.get("url")!=None:
        url=request.args.get("url")
        req_url=url.split('%3')
        video_id=req_url[0].split('=')[1]
        print(video_id)
        video="https://www.youtube.com/embed/"+video_id+ "?controls=0&autoplay=1"
    
        conversion.Tscript(video_id)
        ans=summarize.generate("env//static//result.txt",2)

    return render_template('convert.html',ans=ans,video=video)

@app.route('/')
def index():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
