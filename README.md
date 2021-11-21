# Vscode_Project
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
