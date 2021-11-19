#Main file
from import_ import *

clean_file("./information_.py")
count_div = 1

driver= webdriver.Firefox()
driver.get('https://wateroff.water.gov.tw/city/%E8%87%BA%E4%B8%AD%E5%B8%82/index.html')

#選擇篩選區域  南區: 66000030 北區: 66000050 南屯區: 66000070 西屯區: 66000060
#北屯區: 66000080
#若沒有請註解
#locate_place(driver, '/html/body/main/div/div[1]/div[2]/div[1]/select', '66000070', 'citySelect')

while(1) :
	if  count_div == 21 :
		break

	path = "/html/body/main/div/div[2]/div[1]/div/div[" + str(count_div) + "]/a/div[2]/div[2]/div[2]/div"
	
	try:
		#取得案件編號
		case_num = get_case_num(driver, path)

		#導向停水的詳細資訊
		locate_url = "https://wateroffmap.water.gov.tw/map/view/" + case_num
		driver.get(locate_url)

		#寫入檔案
		if [ driver_wait_by_xpath_text(driver, '/html/body/div/div/div[1]/div[3]/div[2]/div[3]/div[1]/div[2]') != '無停水地區' and driver_wait_by_xpath_text(driver, '/html/body/div/div/div[1]/div[3]/div[2]/div[4]/div[1]/div[2]') != '無降壓地區' ]:
			collect_information_condition_1(driver, case_num)
		elif [ driver_wait_by_xpath_text(driver, '/html/body/div/div/div[1]/div[3]/div[2]/div[3]/div') == '無停水地區' ] :
			collect_information_condition_2(driver, case_num)

		elif [ driver_wait_by_xpath_text(driver, '/html/body/div/div/div[1]/div[3]/div[2]/div[4]/div') == '無降壓地區' ] :
			collect_information_condition_3(driver, case_num)	
		else:
			collect_information_condition_4(driver, case_num)

		#印出資訊
		from information_ import *
		print("\n")
		print(f"案件編號: {case_number}")
		print(f"停水日期: {start_water_cut_date}")
		print(f"停水時間: {start_water_cut_time}")
		print(f"供水日期: {stop_water_cut_date}")
		print(f"供水時間: {stop_water_cut_time}")
		print(f"停水範圍: {water_cut_range}")
		print(f"停水原因: {water_cut_reason}")
		print(f"發布日期: {post_time}")
		print(f"停水叮嚀: {water_cut_tips}")
		print(f"更多資訊: {more_information}")
		print("\n")
		driver.back()
	except Exception as e:
		print(e)
		print("似乎是最後一筆了呢")
		break
	#except:
	#	print("發生未知的錯誤")
	#	break
	count_div += 1

driver.quit()
