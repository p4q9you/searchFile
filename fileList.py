import glob
from datetime import datetime as dt
# モジュールのインポート
import os, tkinter, tkinter.filedialog, tkinter.messagebox

#出力用入れ物
fileList = ""
#検索数
counterInt = 0

# ファイル選択ダイアログの表示
root = tkinter.Tk()
root.withdraw()
fTyp = [("","*")]
iDir = os.path.abspath(os.path.dirname(__file__))
selectDir = tkinter.filedialog.askdirectory(initialdir = iDir)

text_fnames = glob.glob(selectDir + '/**/*.*', recursive=True)
for filename in text_fnames:
    counterInt += 1 
    counterString = str(counterInt)
    fileList = fileList + counterString + ':' +  filename + '\n\r'
    print(counterString + "ファイル目")

#ファイル名のプレフィックスに日付
outputTime = dt.now()
prefixTime = outputTime.strftime('%Y%m%d%H%M')
#書き込みモードでオープン
fileText = open(prefixTime + '_fileList.txt', 'wb')  
fileText.write(fileList.encode('cp932', 'ignore'))