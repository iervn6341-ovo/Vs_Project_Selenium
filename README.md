# Vs_Project
主程式Python_web_crawler  
與line連動主程式為line_api.py   
若要執行整個專案  
Windows:  
    python ./line_api.py  
    ./ngrok http 5000  
linux:  
    sudo apt install ngrok  
    [Terminal 1]:  
        python3 line_api.py  
    [Terminal 2]:  
        ngrok http 5000  
最後請在line-devoloper修改Webhook URL  
例 :[url]/callback  
由於使用selenium作為爬蟲模組  
所以必要條件為有GUI介面  
一次的查看所需時間較長,請耐心等候  
  
  
git push token : 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 
