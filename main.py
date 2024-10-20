import time
import os.path
from selenium import webdriver
from selenium.webdriver.common.by import By


def set_prefs():
    filename = "Path_to_download.txt"
    log = os.path.isfile("Path_to_download.txt")
    if log:
        title = "Хотите изменить путь к папке загрузок? (y/n)"
        choice = input(title).strip().lower()
        if choice == "n":
            with open(filename, "r") as f:
                path_download = f.read().strip()
        else:
            path_download = input("Введите путь (пример: C:\\***\\***\\***) до места загрузки файлов:\n")
            with open(filename, "w") as f:
                f.write(path_download)
    else:
        path_download = input("Введите путь (пример: C:\\***\\***\\***) до места загрузки файлов:\n")
        with open(filename, "w") as f:
            f.write(path_download)
    return path_download


def select_option(options):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Выберите нужную ссылку на файл:")
    print(options[0])
    print(options[1])
    option_index = 0

    for idx in range(2, len(options)):
        if "Страницы" not in options[idx]:
            print(f"{idx - 1}. {options[idx]}")
            option_index += 1

    while True:
        try:
            choice = int(input("Введите номер выбранного варианта: ")) - 1 
            if 0 <= choice < len(options):
                return choice 
            else:
                print("Неверный номер, попробуйте снова.")
        except ValueError:
            print("Пожалуйста, введите число.")

def main():
    name_file = input("Введите названия фильма/серила: >>>>> ")
    URL = "http://rutor.info"
    options = []
    new = []
    chromeOptions = webdriver.ChromeOptions()
    path_prefs = set_prefs()
    prefs = {"download.default_directory": path_prefs}
    chromeOptions.add_experimental_option("prefs", prefs)
    chromeOptions.add_experimental_option('excludeSwitches', ['enable-logging'])
    #chromeOptions.add_argument("--headless")
    webdriver.DesiredCapabilities.CHROME['acceptInsecureCerts'] = True
    driver = webdriver.Chrome(options=chromeOptions)
    driver.get(url=URL)
    time.sleep(1)
    search_bar = driver.find_element(By.XPATH, """/html/body/div[2]/div[2]/div[2]/center/table/tbody/tr[1]/td[2]/input""")
    search_bar.send_keys(name_file)
    time.sleep(0.5)
    search_button = driver.find_element(By.XPATH, """/html/body/div[2]/div[2]/div[2]/center/table/tbody/tr[2]/td/input""")
    search_button.click()
    print("Начинаю поиск...")
    time.sleep(3)
    all_link = driver.find_elements(By.XPATH, """/html/body/div[2]/div[1]/div[2]""")
    all_link_i = driver.find_element(By.ID, "index")
    all_link_s = all_link_i.size
    h = all_link_s['height']
    if h <= 73:
         print(f"К сожалению фильма/сериала по названию:", name_file, "найти не удолось")
         driver.quit()
    for i in range(len(all_link)):
         new.append(all_link[i].text.split("\n"))
         for x in new:
             options.extend(x if isinstance(x, list) else [x])

    select_index = select_option(options)
    good_link = driver.find_element(By.XPATH, f"""/html/body/div[2]/div[1]/div[2]/table/tbody/tr[{select_index + 2}]/td[2]/a[3]""")
    good_link.click()
    print("Захожу...")
    download_button = driver.find_element(By.XPATH, """/html/body/div[2]/div[1]/div[2]/a[2]""")
    download_button.click()
    print("Торрент скачивается...")
    time.sleep(1.5)
    print(f"Файл скачен, находится по адресу:", *prefs.values())
    driver.quit()
    os.system('cls' if os.name == 'nt' else 'clear')
    time.sleep(1)
   
def repeat_or_exit():
    while True:
        cmd = input("Повторный ввод =>> y, выход из программы =>> q \n").strip().lower()
        if cmd == "y":
            main()
        elif cmd == "q":
            print("Выхожу...")
            time.sleep(1)
            raise SystemExit(1)
        else:
            print("Неверный ввод, попробуйте снова.")


if __name__ == '__main__':
    main()
    repeat_or_exit()