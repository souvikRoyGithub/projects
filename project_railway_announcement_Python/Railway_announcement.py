from pydub import AudioSegment
import pandas as pd
from gtts import gTTS
import os

data=pd.read_excel("announce_hindi.xlsx")

def already_saved_audio_by_recording_railway(i1,x,y):
    start=x
    end=y
    song=AudioSegment.from_mp3("../railway.mp3")
    extract=song[start:end]
    chdir
    extract.export(f"{i1}_already_saved_audio_by_recording_railway.mp3",format="mp3")

for i in range(0,len(data)):
    try:
        #making different directory for each train
        os.makedirs(f"Train_no_{data['train_no'].loc[i]}")
        chdir=os.chdir(f"Train_no_{data['train_no'].loc[i]}/")
        # print(os.getcwd())
        #calling function
        already_saved_audio_by_recording_railway("01", 88000, 90200)
        already_saved_audio_by_recording_railway("03", 91000,92200)
        already_saved_audio_by_recording_railway("05", 94000,95000)
        already_saved_audio_by_recording_railway("07", 96000,98900)
        already_saved_audio_by_recording_railway("09", 105500,108200)
        already_saved_audio_by_recording_railway("11", 109000,112250)

        #"from" mp3 saved
        myobj=gTTS(text=data["from"].loc[i],lang="en",slow=True)
        myobj.save(f"02_Row{i+1}_railway.mp3")   
        #"via" city mp3 saved
        myobj=gTTS(text=data["via"].loc[i],lang="en",slow=True)
        myobj.save(f"04_Row{i+1}_railway.mp3")
        #"to city" mp3 saved
        myobj=gTTS(text=data["to"].loc[i],lang="en",slow=True)
        myobj.save(f"06_Row{i+1}_railway.mp3")
        #"train no and name" mp3 saved
        myobj=gTTS(text=data["train_no"].loc[i]+data["train_name"].loc[i],lang="en",slow=True)
        myobj.save(f"08_Row{i+1}_railway.mp3")
        #"platform number" mp3 saved
        myobj=gTTS(text=data["platform"].loc[i],lang="en",slow=True)
        myobj.save(f"10_Row{i+1}_railway.mp3")

        #Audio merging...
        merge=AudioSegment.empty()
        for item in os.listdir():
            merge+=AudioSegment.from_file(item)
        merge.export(f"Train_no_{data['train_no'].loc[i]}_merge.mp3",format="mp3")
        #removing the 
        for item in os.listdir():
            if "merge" in item:
                pass
            else:
                os.remove(item)
        os.chdir("../")
    except FileExistsError:
        print(f"\nDirectory train_no:{data['train_no'].loc[i]} already present,please check that directory,if you dont find any file then delete the folder and run the program again.")
        continue


print("\n\t\t\t\t\t\t\tSuccessfully ran.")