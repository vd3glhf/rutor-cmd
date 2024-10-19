import time
import os.path
from selenium.common.exceptions import WebDriverException
from selenium.common.exceptions import NoSuchElementException
from pick import pick
from selenium import webdriver
from selenium.webdriver.common.by import By

name_file = ""


def set_prefs():
    filename = "Path_to_download.txt"
    log = os.path.isfile("Path_to_download.txt")
    if log:
        title = "Хотите изменить путь к папке загрузок?"
        option = ["YES", "NO"]
        choice, idx = pick(option, title, indicator='=>', default_index=1)
        if choice == "NO":
            with open(filename, "r") as f:
                path_download = f.read()
        else:
            path_download = input("Введите путь (пример: C:\***\***\***) до места загрузки файлов:\n")
            with open(filename, "w") as f:
                f.write(path_download)
    else:
        path_download = input("Введите путь (пример: C:\***\***\***) до места загрузки файлов:\n")
        with open(filename, "w") as f:
            f.write(path_download)
    return path_download


def main():
    name_file = input("Введите названия фильма/серила: >>>>> ")
    URL = "http://rutor.info"
    options = []
    new = []
    PROXY = '163.116.177.47:80'

    webdriver.DesiredCapabilities.CHROME['proxy'] = {
        "httpProxy": PROXY,
        "ftpProxy": PROXY,
        "sslProxy": PROXY,
        "proxyType": "MANUAL",
    }
    chromeOptions = webdriver.ChromeOptions()
    path_prefs = set_prefs()
    prefs = {"download.default_directory": path_prefs}
    chromeOptions.add_experimental_option("prefs", prefs)
    chromeOptions.add_experimental_option('excludeSwitches', ['enable-logging'])
    #chromeOptions.add_argument("--headless")
    webdriver.DesiredCapabilities.CHROME['acceptSslCerts'] = True
    driver = webdriver.Chrome(options=chromeOptions)
    try:
        driver.get(url=URL)
        print("Браузер запущен")
    except WebDriverException:
        print("gg wp")
        driver.quit()
    time.sleep(1)
    search_bar = driver.find_element(By.XPATH, """/html/body/div[2]/div[2]/div[2]/center/table/tbody/tr[1]/td[2]/input""")
    search_bar.send_keys(name_file)
    time.sleep(0.5)
    search_button = driver.find_element(By.XPATH, """/html/body/div[2]/div[2]/div[2]/center/table/tbody/tr[2]/td/input""")
    search_button.click()
    print("Начинаю поиск...")
    # quantity_link = driver.find_element(By.XPATH, "/html/body/div[2]/div[1]/div[2]")
    # print(f"Страниц: {quantity_link.text[10]}, Результатов поиска: {quantity_link.text[31]}{quantity_link.text[32]}")
    time.sleep(3)
    all_link = driver.find_elements(By.XPATH, """/html/body/div[2]/div[1]/div[2]""")
    all_link_i = driver.find_element(By.ID, "index")
    all_link_s = all_link_i.size
    h = all_link_s['height']
    if h <= 73:
        print(f"К сожалению фильма/сериала по названию:", name_file, "найти не удолось")
        driver.quit()
        time.sleep(0.5)
        cmd = input("Повторный ввод =>> y, выход из программы =>> q \n")
        if cmd == "y":
            main()
        elif cmd == "q":
            print("Выхожу...")
            time.sleep(1)
            raise SystemExit(1)

    for i in range(len(all_link)):
        # print(all_link[i].text)
        new.append(all_link[i].text.split("\n"))
        for x in new:
            options.extend(x if isinstance(x, list) else [x])

    title = "Выберите нужную сылку на файл: \n"
    option, index = pick(options, title, indicator="=>", default_index=2)
    if index:
        good_link = driver.find_element(By.XPATH, f"""/html/body/div[2]/div[1]/div[2]/table/tbody/tr[{index}]/td[2]/a[3]""")
        good_link.click()
    print("Захожу...")
    download_button = driver.find_element(By.XPATH, """/html/body/div[2]/div[1]/div[2]/a[2]""")
    download_button.click()
    print("Торрент скачивается...")
    time.sleep(1.5)
    print(f"Файл скачен, находится по адресу:", *prefs.values())
    driver.quit()
    time.sleep(1)
    cmd = input("Повторный ввод =>> y, выход из программы =>> q \n")
    if cmd == "y":
        main()
    elif cmd == "q":
        print("Выхожу...")
        time.sleep(1)
        raise SystemExit(1)


if __name__ == '__main__':
    main()
