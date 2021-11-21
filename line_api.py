from import_ import *
from Python_web_crawler import search_water_
count_div = 1
app = Flask(__name__)

#設定資料
line_bot_api = LineBotApi('XI7nR5ztvkRzKMIGcbBbm5zxL7xj1uf4tTS5TrgltV93aCV1uCby0eUr0S0NHbgFNDMXIjK/E7vqqfAnjfYnDUbobs9e4WN4A+uSZboEuhDiwUIsZgplCfFAHyGsQd57M6uxLrZ5HwOCj6zyqOJ4jgdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('370d4ef98d73310f91550dbbc2fa4f40')



@app.route("/callback", methods=['POST'])
def callback():
	signature = request.headers['X-Line-Signature']

	body = request.get_data(as_text=True)
	app.logger.info("Request body: " + body)

	try:
		print(body, signature)
		handler.handle(body, signature)
	except InvalidSignatureError:
		abort(400)

	return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def pretty_echo(event):
	global count_div 
	string = ['']
	if "查看" in event.message.text :
		line_bot_api.push_message('Ueea1498b70a1795aceac5537f1fa8d11',TextSendMessage(text="程式語言: Python\n模組: Selenium\n請稍後..."))
		store_data_list =['案件編號', '停水日期', '停水時間', '復水日期', '復水時間', '停水範圍', '停水原因', '降壓範圍', '降壓原因', '發布日期', '停水叮嚀', '目前狀態', '更多資訊']
		water_given_list =['案件編號', '復水狀態', '更多資訊']
		search_water = search_water_('https://wateroff.water.gov.tw/city/%E8%87%BA%E4%B8%AD%E5%B8%82/index.html', count_div)
		return_data = search_water.start_program()
		if len(return_data) == 13 :
			for i in range(0, 13):
				if return_data[i] == 'None':
					continue
				string[0] += store_data_list[i] + ": " + return_data[i] +"\n"
			line_bot_api.push_message('Ueea1498b70a1795aceac5537f1fa8d11',TextSendMessage(text=string[0]))
		elif len(return_data) == 3:
			for i in range(0, 3):
				string[0] += water_given_list[i] + ": " + return_data[i] +"\n"
			line_bot_api.push_message('Ueea1498b70a1795aceac5537f1fa8d11',TextSendMessage(text=string[0]))

		count_div += 1
	elif "重置" in event.message.text :
		line_bot_api.push_message('Ueea1498b70a1795aceac5537f1fa8d11',TextSendMessage(text="已重置"))
		count_div = 1
	else:
		string[0] += "輸入\n    「查看」以搜尋停水訊息\n    「重置」以重新查看以前的資料"
		line_bot_api.push_message('Ueea1498b70a1795aceac5537f1fa8d11',TextSendMessage(text=string[0]))
app.run()