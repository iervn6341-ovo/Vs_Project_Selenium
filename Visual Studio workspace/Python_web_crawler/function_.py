#funtion在這裡
#註1 :所有定義函式的引入變數都要有 [driver :源自於ｍａｉｎｆｉｌｅ的ｗｅｂｄｒｉｖｅｒ] 
from import_ import *

def clean_file(path):
	file = open(path, 'w')
	file.close()

def locate_place(driver, x_path, value, id_):
	#location_position = Select(driver.find_element_by_id(id_))
	path = x_path + '/option[@value=' + value + ']'
	WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/main/div/div[2]/div[1]/div/div[1]/a')))
	location_position  = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, path))).click()

def get_case_num(driver, x_path):
	case_num = driver.find_element_by_xpath(x_path).text
	return case_num

def sleep(times):
	times = int(times)
	time.sleep(times)

#parameter_name: 傳至 [information.py] 的變數名稱 , x_path: 搜尋網頁元素的路徑
def writefile(driver, parameter_name, x_path, url):
	file = open('./information.py', 'a')
	if x_path != '':
		catch_text = driver.find_element_by_xpath(x_path).text
		text_temp = parameter_name + " = '" + catch_text + "'\n"
		file.write(text_temp)
	if url != '':
		file.write(parameter_name + " = '" + url + "'\n")
	file.close()