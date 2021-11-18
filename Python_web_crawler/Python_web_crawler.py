#Main file
from import_ import *

clean_file("./information_.py")
driver= webdriver.Firefox()
driver.get('https://wateroff.water.gov.tw/city/%E8%87%BA%E4%B8%AD%E5%B8%82/index.html')

#選擇篩選區域  南區: 66000030 北區: 66000050 南屯區: 66000070
locate_place(driver, '/html/body/main/div/div[1]/div[2]/div[1]/select', '66000030', 'citySelect')
sleep(2)
case_num = get_case_num(driver, "/html/body/main/div/div[2]/div[1]/div/div/a/div[2]/div[2]/div[2]/div")

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
		collect_information(driver, case_num)

		#印出資訊
		from information_ import *
		print("\n")
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
	except Exception as e:
		print("似乎是最後一筆了呢")
	except:
		print("發生未知的錯誤")
	count_div += 1

input()

