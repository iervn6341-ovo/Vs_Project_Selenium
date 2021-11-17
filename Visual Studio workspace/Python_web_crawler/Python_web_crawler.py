#main file
from import_ import *

clean_file("./information.py")
driver= webdriver.Firefox()
driver.get('https://wateroff.water.gov.tw/city/%E8%87%BA%E4%B8%AD%E5%B8%82/index.html')

#選擇篩選區域  南區: 66000030 北區: 66000050 南屯區: 66000070
locate_place(driver, '/html/body/main/div/div[1]/div[2]/div[1]/select', '66000030', 'citySelect')
sleep(2)
case_num = get_case_num(driver, "/html/body/main/div/div[2]/div[1]/div/div/a/div[2]/div[2]/div[2]/div")

#導向停水的詳細資訊
locate_url = "https://wateroffmap.water.gov.tw/map/view/" + case_num
driver.get(locate_url)
sleep(1)

#寫入檔案
writefile(driver, 'start_water_cut_date', '/html/body/div/div/div[1]/div[3]/div[2]/div[2]/div[1]/div[1]', '')
writefile(driver, 'start_water_cut_time', '/html/body/div/div/div[1]/div[3]/div[2]/div[2]/div[1]/div[2]/span', '')

writefile(driver, 'stop_water_cut_date', '/html/body/div/div/div[1]/div[3]/div[2]/div[2]/div[2]/div[1]', '')
writefile(driver, 'stop_water_cut_time', '/html/body/div/div/div[1]/div[3]/div[2]/div[2]/div[2]/div[2]/span', '')

writefile(driver, 'water_cut_range', '/html/body/div/div/div[1]/div[3]/div[2]/div[3]/div[1]/div[2]', '')
writefile(driver, 'water_cut_reason', '/html/body/div/div/div[1]/div[3]/div[2]/div[3]/div[2]/div[2]', '')

writefile(driver, 'post_time', '/html/body/div/div/div[1]/div[3]/div[2]/div[5]/div[4]/div', '')
writefile(driver, 'water_cut_tips', '/html/body/div/div/div[1]/div[3]/div[2]/div[5]/div[7]/div', '')
url = "https://wateroffmap.water.gov.tw/map/view/" + case_num
writefile(driver, 'more_information', '', url)

print("\n")

from information import *
sleep(0.5)
print(f"停水日期: {start_water_cut_date}")
print(f"停水時間: {start_water_cut_time}")
print(f"供水日期: {stop_water_cut_date}")
print(f"供水時間: {stop_water_cut_time}")
print(f"停水範圍: {water_cut_range}")
print(f"停水原因: {water_cut_reason}")
print(f"發布日期: {post_time}")
print(f"停水叮嚀: {water_cut_tips}")
print(f"更多資訊: {more_information}")

input()

