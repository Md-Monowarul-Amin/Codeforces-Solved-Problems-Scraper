from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
import undetected_chromedriver as uc


# service = Service(executable_path="chromedriver")
# driver = webdriver.Chrome(service= service)

driver = uc.Chrome(
    use_subprocess=False,
)

for i in range(6,13):

    driver.set_page_load_timeout(30)  # Increase timeout
    url = "https://codeforces.com/submissions/MONOWARUL_AMIN/page/" + str(i)
    driver.get(url)

    title = driver.title

    driver.implicitly_wait(2)
    table_data = driver.find_element(by=By.CLASS_NAME, value="status-frame-datatable")

    # Find all table rows (excluding the header row)
    rows = table_data.find_elements(By.TAG_NAME, "tr")

    hrefs = []

    for row in rows[1:]:
        tds = row.find_elements(By.TAG_NAME, "td")
        # for td in tds:
        #     print(td.text, end=" ")
        verdict = tds[5].text
        if verdict == "Accepted":
            submission_ids = tds[0].find_elements(By.TAG_NAME, "a")
            href = submission_ids[0].get_attribute("href")
            hrefs.append(href)
            
            # print(tds[0].text, tds[5].text)
            print("href: ", href)
            # driver.get(href)
            # codes = driver.find_elements(By.TAG_NAME, "ol")
            # for code in codes:
            #     print(code.text)


        # print()
    # print(rows.text)

    time.sleep(30)
    # driver.quit()


    cnt = 0

    for href in hrefs:

        driver.set_page_load_timeout(30)  # Increase timeout
        driver.get(href)
        driver.implicitly_wait(2)

        # table_data = driver.find_elements(By.CLASS_NAME, "highlighted-row")
        rows = driver.find_elements(By.CLASS_NAME, "highlighted-row")
        for row in rows:
            print(row.text)
        # print("Rows len: ", len(rows))
        if len(rows) > 0:
            row_2 = rows[0]
        else:
            continue
        tds = row_2.find_elements(By.TAG_NAME, "td")
        anchor_td_3 = tds[2].find_elements(By.TAG_NAME, "a")
        problem_name = anchor_td_3[0].get_attribute("title")

        print(problem_name)
        ol = driver.find_elements(By.TAG_NAME, "ol")
        problem_text = ol[0].text
        cnt += 1
        print(cnt)
        if "/" in problem_name:
            index = problem_name.find("/")
            problem_name = problem_name[:index] + problem_name[index+1:]
        # print(ol[0].text)
        # Open the file in write mode ('w')
        file_name = "CodeforcesProblems" + "/" + problem_name + ".py"
        with open(file_name, "w") as file:
            file.write(problem_text)

        time.sleep(5)

        # for li in ol:
        #     print(li.text)
        
    driver.quit()
