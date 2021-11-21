#Main file
from import_ import *

class search_water_():
	def __init__(self, url, count_div):
		self.store_data_list =['案件編號', '停水日期', '停水時間', '復水日期', '復水時間', '停水範圍', '停水原因', '降壓範圍', '降壓原因', '發布日期', '停水叮嚀', '目前狀態', '更多資訊']
		self.water_given_list =['案件編號', '復水狀態', '更多資訊']
		self.url = url
		self.count_div = count_div
		self.case_num_temp = 0
	
	def start_program(self):
		#self.driver= webdriver.Chrome()
		self.driver= webdriver.Firefox()
		self.driver.get(self.url)
		init_file("./data_.py")
		check_del_module()
		self.count_list = 0

		#選擇篩選區域  南區: 66000030 北區: 66000050 南屯區: 66000070 西屯區: 66000060
		#北屯區: 66000080 豐原區: 66000090 霧峰區: 66000260 豐原區: 66000090
		#若沒有請註解
		#locate_place(self.driver, '/html/body/main/div/div[1]/div[2]/div[1]/select', '66000090', 'citySelect')
		path = "/html/body/main/div/div[2]/div[1]/div/div[" + str(self.count_div) + "]/a/div[2]/div[2]/div[2]/div"
		check_water =  "/html/body/main/div/div[2]/div[1]/div/div[" + str(self.count_div) + "]/a/div[1]/div[2]"

		try:
			#取得案件編號
		
			case_num = get_case_num(self.driver, path)
			if self.case_num_temp == case_num:
				print("\n似乎是最後一筆了呢")
				return "似乎是最後一筆了呢"
			self.case_num_temp = case_num

			#先檢查是否復水
			try:
				#找已復水元素
				self.driver.find_element_by_xpath(check_water)
				collect_information_condition_4(self.driver, case_num)
				'''
					#印出資訊
					from data_ import water_given_data
					for i in range(0,3):
						print(f"{self.water_given_list[i]}: {water_given_data[i]}")
				'''
				from data_ import store_data
				self.driver.quit()
				return water_given_data
			except NoSuchElementException:
				pass

			#導向停水的詳細資訊
			locate_url = "https://wateroffmap.water.gov.tw/map/view/" + case_num
			self.driver.get(locate_url)

			#寫入檔案
		
			try:
				sleep(1)
				#找停水區域元素
				self.driver.find_element_by_xpath('/html/body/div/div/div[1]/div[3]/div[2]/div[3]/div[1]/div[2]')
			except NoSuchElementException :
				collect_information_condition_2(self.driver, case_num)
				'''
					#印出資訊
					from data_ import store_data
					while(1):
						if self.count_list == 13:
							break
						print("{}: {}".format(self.store_data_list[self.count_list], store_data[self.count_list]))
						self.count_list +=1
				'''
				from data_ import store_data
				self.driver.quit()
				return store_data
				pass
			except:
				pass

			try:
				sleep(1)
				#找降壓區域元素
				self.driver.find_element_by_xpath('/html/body/div/div/div[1]/div[3]/div[2]/div[4]/div[1]/div[2]')
			except NoSuchElementException :
				collect_information_condition_3(self.driver, case_num)
				
				'''
					#印出資訊
					from data_ import store_data
					while(1):
						if self.count_list == 13:
							break
						print("{}: {}".format(self.store_data_list[self.count_list],	store_data[self.count_list]))
						self.count_list += 1
				'''
				from data_ import store_data
				self.driver.quit()
				return store_data
				pass
			except Exception as e:
				print(e)
				pass

			try:
				sleep(1)
				#找停水區域元素
				self.driver.find_element_by_xpath('/html/body/div/div/div[1]/div[3]/div[2]/div[3]/div[1]/div[2]')
				self.driver.find_element_by_xpath('/html/body/div/div/div[1]/div[3]/div[2]/div[4]/div[1]/div[2]')
				collect_information_condition_1(self.driver, case_num)

				'''
					#印出資訊
					from data_ import store_data
					while(1):
						if self.count_list == 13:
							break
						print("{}: {}".format(self.store_data_list[self.count_list], store_data[self.count_list]))
						self.count_list +=1
				'''
				from data_ import store_data
				self.driver.quit()
				return store_data
			except:
				pass

			self.	driver.back()
		#except Exception as e:
		#	print(e)
		except:
			print("尚未發布停水資訊")
			self.driver.quit()
			return "尚未發布停水資訊"
		self.count_div += 1
#search_water = search_water_('https://wateroff.water.gov.tw/city/%E8%87%BA%E4%B8%AD%E5%B8%82/index.html', count_div=1)
#re_data = search_water.start_program()