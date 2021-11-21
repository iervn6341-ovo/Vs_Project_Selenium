#funtion在這裡
#註1 :所有定義函式的引入變數都要有 [driver :源自於ｍａｉｎｆｉｌｅ的ｗｅｂｄｒｉｖｅｒ] 
from import_ import *

#初始化(清空) information.py 檔案
def init_file(path):
	file = open(path, 'w')
	file.write("store_data = []")
	file.write("\n")
	file.write("water_given_data = []")
	file.close()

def check_del_module():
	if 'data_' in sys.modules:
		del sys.modules["data_"]

#利用webdriverwait函式等待直到找到指定xpath元素
def driver_wait_by_xpath(driver, x_path):
	information = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, x_path)))
	return information

def driver_wait_by_xpath_text(driver, x_path):
	information = driver_wait_by_xpath(driver, x_path)
	information = information.text
	return information

#選取行政區
def locate_place(driver, x_path, value, id_):
	#location_position = Select(driver.find_element_by_id(id_))
	path = x_path + '/option[@value=' + value + ']'
	driver_wait_by_xpath(driver, '/html/body/main/div/div[2]/div[1]/div/div[1]/a')
	driver_wait_by_xpath(driver, path).click()

#取得案件編號
def get_case_num(driver, x_path):
	case_num = driver_wait_by_xpath_text(driver, x_path)
	#driver_wait_by_xpath(driver, '/html/body/main/div/div[2]/div[1]/div/div[1]/a')
	#case_num = driver.find_element_by_xpath(x_path).text
	return case_num

def sleep(times):
	times = int(times)
	time.sleep(times)

#將當前案件編號的資訊蒐集起來
#collect_information_condition_1: 有停水有降壓地區尚未復水的狀態
#collect_information_condition_2: 無停水有降壓地區尚未復水的狀態
#collect_information_condition_3: 有停水無降壓地區尚未復水的狀態
#collect_information_condition_4: 已復水

def collect_information_condition_1(driver, case__num):
	start_water_cut_time_string = ['']
	stop_water_cut_time_string = ['']
	writefile_store_data(driver, '', case__num)
	writefile_store_data(driver, '/html/body/div/div/div[1]/div[3]/div[2]/div[2]/div[1]/div[1]', '')

	try:
		driver.find_element_by_xpath('/html/body/div/div/div[1]/div[3]/div[2]/div[2]/div[1]/div[2]/span[2]')
		start_water_cut_time_string[0] +=  driver.find_element_by_xpath('/html/body/div/div/div[1]/div[3]/div[2]/div[2]/div[1]/div[2]/span[1]').text + " ～ " + driver.find_element_by_xpath('/html/body/div/div/div[1]/div[3]/div[2]/div[2]/div[1]/div[2]/span[2]').text
		writefile_store_data(driver, '', start_water_cut_time_string[0])
	except:
		writefile_store_data(driver, '/html/body/div/div/div[1]/div[3]/div[2]/div[2]/div[1]/div[2]/span', '')
	writefile_store_data(driver, '/html/body/div/div/div[1]/div[3]/div[2]/div[2]/div[2]/div[1]', '')

	try:
		driver.find_element_by_xpath('/html/body/div/div/div[1]/div[3]/div[2]/div[2]/div[2]/div[2]/span[2]')
		stop_water_cut_time_string[0] +=  driver.find_element_by_xpath('/html/body/div/div/div[1]/div[3]/div[2]/div[2]/div[2]/div[2]/span[1]').text + " ～ " + driver.find_element_by_xpath('/html/body/div/div/div[1]/div[3]/div[2]/div[2]/div[2]/div[2]/span[2]').text
		writefile_store_data(driver, '', stop_water_cut_time_string[0])
	except:
		writefile_store_data(driver, '/html/body/div/div/div[1]/div[3]/div[2]/div[2]/div[2]/div[2]/span', '')

	writefile_store_data(driver, '/html/body/div/div/div[1]/div[3]/div[2]/div[3]/div[1]/div[2]', '')
	writefile_store_data(driver, '/html/body/div/div/div[1]/div[3]/div[2]/div[3]/div[2]/div[2]', '')
	writefile_store_data(driver, '/html/body/div/div/div[1]/div[3]/div[2]/div[4]/div[1]/div[2]', '')
	writefile_store_data(driver, '/html/body/div/div/div[1]/div[3]/div[2]/div[4]/div[2]/div[2]', '')
	writefile_store_data(driver, '/html/body/div/div/div[1]/div[3]/div[2]/div[5]/div[4]/div', '')
	writefile_store_data(driver, '/html/body/div/div/div[1]/div[3]/div[2]/div[5]/div[7]/div', '')
	writefile_store_data(driver, '', '未復水')
	url = "https://wateroffmap.water.gov.tw/map/view/" + case__num
	writefile_store_data(driver, 'more_information', '', url)


def collect_information_condition_2(driver, case__num):
	start_water_cut_time_string = ['']
	stop_water_cut_time_string = ['']
	writefile_store_data(driver, '', case__num)
	writefile_store_data(driver, '/html/body/div/div/div[1]/div[3]/div[2]/div[2]/div[1]/div[1]', '')
	
	try:
		driver.find_element_by_xpath('/html/body/div/div/div[1]/div[3]/div[2]/div[2]/div[1]/div[2]/span[2]')
		start_water_cut_time_string[0] +=  driver.find_element_by_xpath('/html/body/div/div/div[1]/div[3]/div[2]/div[2]/div[1]/div[2]/span[1]').text + " ～ " + driver.find_element_by_xpath('/html/body/div/div/div[1]/div[3]/div[2]/div[2]/div[1]/div[2]/span[2]').text
		writefile_store_data(driver, '', start_water_cut_time_string[0])
	except:
		writefile_store_data(driver, '/html/body/div/div/div[1]/div[3]/div[2]/div[2]/div[1]/div[2]/span', '')

	writefile_store_data(driver, '/html/body/div/div/div[1]/div[3]/div[2]/div[2]/div[2]/div[1]', '')

	try:
		driver.find_element_by_xpath('/html/body/div/div/div[1]/div[3]/div[2]/div[2]/div[2]/div[2]/span[2]')
		stop_water_cut_time_string[0] +=  driver.find_element_by_xpath('/html/body/div/div/div[1]/div[3]/div[2]/div[2]/div[2]/div[2]/span[1]').text + " ～ " + driver.find_element_by_xpath('/html/body/div/div/div[1]/div[3]/div[2]/div[2]/div[2]/div[2]/span[2]').text
		writefile_store_data(driver, '', stop_water_cut_time_string[0])
	except:
		writefile_store_data(driver, '/html/body/div/div/div[1]/div[3]/div[2]/div[2]/div[2]/div[2]/span', '')

	writefile_store_data(driver, '', 'None')
	writefile_store_data(driver, '', 'None')
	writefile_store_data(driver, '/html/body/div/div/div[1]/div[3]/div[2]/div[4]/div[1]/div[2]', '')
	writefile_store_data(driver, '/html/body/div/div/div[1]/div[3]/div[2]/div[4]/div[2]/div[2]', '')
	writefile_store_data(driver, '/html/body/div/div/div[1]/div[3]/div[2]/div[5]/div[4]/div', '')
	writefile_store_data(driver, '/html/body/div/div/div[1]/div[3]/div[2]/div[5]/div[7]/div', '')
	writefile_store_data(driver, '', '未復水')
	url = "https://wateroffmap.water.gov.tw/map/view/" + case__num
	writefile_store_data(driver, '', url)

def collect_information_condition_3(driver, case__num):
	start_water_cut_time_string = ['']
	stop_water_cut_time_string = ['']
	writefile_store_data(driver, '', case__num)
	writefile_store_data(driver, '/html/body/div/div/div[1]/div[3]/div[2]/div[2]/div[1]/div[1]', '')

	try:
		driver.find_element_by_xpath('/html/body/div/div/div[1]/div[3]/div[2]/div[2]/div[1]/div[2]/span[2]')
		start_water_cut_time_string[0] +=  driver.find_element_by_xpath('/html/body/div/div/div[1]/div[3]/div[2]/div[2]/div[1]/div[2]/span[1]').text + " ～ " + driver.find_element_by_xpath('/html/body/div/div/div[1]/div[3]/div[2]/div[2]/div[1]/div[2]/span[2]').text
		writefile_store_data(driver, '', start_water_cut_time_string[0])
	except:
		writefile_store_data(driver, '/html/body/div/div/div[1]/div[3]/div[2]/div[2]/div[1]/div[2]/span', '')

	writefile_store_data(driver, '/html/body/div/div/div[1]/div[3]/div[2]/div[2]/div[2]/div[1]', '')

	try:
		driver.find_element_by_xpath('/html/body/div/div/div[1]/div[3]/div[2]/div[2]/div[2]/div[2]/span[2]')
		stop_water_cut_time_string[0] +=  driver.find_element_by_xpath('/html/body/div/div/div[1]/div[3]/div[2]/div[2]/div[2]/div[2]/span[1]').text + " ～ " + driver.find_element_by_xpath('/html/body/div/div/div[1]/div[3]/div[2]/div[2]/div[2]/div[2]/span[2]').text
		writefile_store_data(driver, '', stop_water_cut_time_string[0])
	except:
		writefile_store_data(driver, '/html/body/div/div/div[1]/div[3]/div[2]/div[2]/div[2]/div[2]/span', '')

	writefile_store_data(driver, '/html/body/div/div/div[1]/div[3]/div[2]/div[3]/div[1]/div[2]', '')
	writefile_store_data(driver, '/html/body/div/div/div[1]/div[3]/div[2]/div[3]/div[2]/div[2]', '')
	writefile_store_data(driver, '', 'None')
	writefile_store_data(driver, '', 'None')
	writefile_store_data(driver, '/html/body/div/div/div[1]/div[3]/div[2]/div[5]/div[4]/div', '')
	writefile_store_data(driver, '/html/body/div/div/div[1]/div[3]/div[2]/div[5]/div[7]/div', '')
	writefile_store_data(driver, '', '未復水')
	url = "https://wateroffmap.water.gov.tw/map/view/" + case__num
	writefile_store_data(driver, '', url)

def collect_information_condition_4(driver, case__num):
	writefile_water_given_data(driver, case__num)
	writefile_water_given_data(driver, '已復水')
	url = "https://wateroffmap.water.gov.tw/map/view/" + case__num
	writefile_water_given_data(driver, url)
#
#x_path: 搜尋網頁元素的路徑
def writefile_store_data(driver, x_path, output_text):
	from data_ import store_data
	if x_path != '' :
		catch_text = driver.find_element_by_xpath(x_path).text
		store_data.append(catch_text)
	else:
		store_data.append(output_text)
	

def writefile_water_given_data(driver, output_text):
	from data_ import water_given_data
	water_given_data.append(output_text)
