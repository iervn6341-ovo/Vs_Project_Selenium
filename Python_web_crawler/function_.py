#funtion在這裡
#註1 :所有定義函式的引入變數都要有 [driver :源自於ｍａｉｎｆｉｌｅ的ｗｅｂｄｒｉｖｅｒ] 
from import_ import *


#初始化(清空) information.py 檔案
def clean_file(path):
	file = open(path, 'w')
	file.close()

#利用webdriverwait函式等待直到找到指定xpath元素
def driverwaitbyxpath(driver, x_path):
	information = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, x_path)))
	return information

#選取行政區
def locate_place(driver, x_path, value, id_):
	#location_position = Select(driver.find_element_by_id(id_))
	path = x_path + '/option[@value=' + value + ']'
	driverwaitbyxpath(driver, '/html/body/main/div/div[2]/div[1]/div/div[1]/a')
	driverwaitbyxpath(driver, path).click()

#取得案件編號
def get_case_num(driver, x_path):
	case_num = driver.find_element_by_xpath(x_path).text
	return case_num

def sleep(times):
	times = int(times)
	time.sleep(times)

#將當前案件編號的資訊蒐集起來
def collect_information(driver, case__num):
	writefile(driver, 'case_number ', '', case__num)
	writefile(driver, 'start_water_cut_date', '/html/body/div/div/div[1]/div[3]/div[2]/div[2]/div[1]/div[1]', '')
	#/html/body/div/div/div[1]/div[3]/div[2]/div[2]/div[1]/div[1]
	#/html/body/div/div/div[1]/div[3]/div[2]/div[2]/div[2]/div[1]
	#/html/body/div/div/div[1]/div[3]/div[2]/div[2]/div[2]/div[1]
	writefile(driver, 'start_water_cut_time', '/html/body/div/div/div[1]/div[3]/div[2]/div[2]/div[1]/div[2]/span', '')

	writefile(driver, 'stop_water_cut_date', '/html/body/div/div/div[1]/div[3]/div[2]/div[2]/div[2]/div[1]', '')
	writefile(driver, 'stop_water_cut_time', '/html/body/div/div/div[1]/div[3]/div[2]/div[2]/div[2]/div[2]/span', '')

	writefile(driver, 'water_cut_range', '/html/body/div/div/div[1]/div[3]/div[2]/div[3]/div[1]/div[2]', '')
	writefile(driver, 'water_cut_reason', '/html/body/div/div/div[1]/div[3]/div[2]/div[3]/div[2]/div[2]', '')

	writefile(driver, 'post_time', '/html/body/div/div/div[1]/div[3]/div[2]/div[5]/div[4]/div', '')
	writefile(driver, 'water_cut_tips', '/html/body/div/div/div[1]/div[3]/div[2]/div[5]/div[7]/div', '')
	url = "https://wateroffmap.water.gov.tw/map/view/" + case__num
	writefile(driver, 'more_information', '', url)

#parameter_name: 傳至 [information.py] 的變數名稱 , x_path: 搜尋網頁元素的路徑
def writefile(driver, parameter_name, x_path, url):
	file = open('./information_.py', 'a')
	if x_path != '':
		catch_text = driver.find_element_by_xpath(x_path).text
		text_temp = parameter_name + " = '" + catch_text + "'\n"
		file.write(text_temp)
	if url != '':
		file.write(parameter_name + " = '" + url + "'\n")
	file.close()
