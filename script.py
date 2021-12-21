from youtube_transcript_api import YouTubeTranscriptApi
import os

from transformers import AutoTokenizer, AutoModelForTokenClassification
from transformers import pipeline
tokenizer = AutoTokenizer.from_pretrained("oliverguhr/fullstop-punctuation-multilang-large")
model = AutoModelForTokenClassification.from_pretrained("oliverguhr/fullstop-punctuation-multilang-large")


outls=[]
class conversion():
    def __init__(self):
        pass
    def Tscript(input):
        os.remove('env//static//output.txt')
        tx=YouTubeTranscriptApi.get_transcript(input)
        for i in tx:
            outtxt=(i['text'])
            outls.append(outtxt)
            print(outtxt)
            with open('env//static//output.txt','a') as f:
                if outtxt[0]=='[':
                    continue
                else:
                    f.write(outtxt+' ')
        
        ans=[]
        with open('env//static//output.txt','r') as f1:
            filedata = f1.readlines()
            ans.append(filedata)
    
        pun = pipeline('ner', model=model, tokenizer=tokenizer,grouped_entities=True)
        output_json = pun(ans[0][0])
        #print(output_json)
        s = ''
        for n in output_json:
            result = n['word'].replace('▁',' ') + n['entity_group'].replace('0',' ')
            s += result

    
        print(s)
  
        with open('env//static//result.txt','w') as f:
            f.write(s)


# if __name__=='__main__':
#     Tscript('XEOvNVYmjDM')