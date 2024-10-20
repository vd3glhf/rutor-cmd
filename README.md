# rutor-cmd
ENG:

Downloading torrent files from rutor.info using the command line interface.
I would also like to note that for a users from Russia to operate the service rutor.info A VPN is required.

How to use it?
1. Install the Selenium library.

pip install selenium

2. Go to this resource (https://getwebdriver.com/chromedriver#stable ), download the driver for the latest version of Chrome Browser.
3. Next, you need to unpack the downloaded archive to a place convenient for you, and then add it to the PATH variable. To verify the successful installation of the driver, run the command prompt and type "chromedriver --version" (without quotes) if everything is done correctly, you will see the version number
4. Next, run the file main.py
5. If you want to hide the browser and work only on the command line, then uncomment line 59 of the code in the main() function.

RUS:

Загрузка торрент-файлов с rutor.info с помощью интерфейса командной строки.
Также хочется отметить, что для пользователей из России для работы сервиса rutor.info требуется VPN.

Как это использовать?
1. Установите библиотеку Selenium.

pip install selenium

2. Перейдите на этот ресурс (https://getwebdriver.com/chromedriver#stable) и скачайте драйвер для последней версии браузера Chrome.
3. Далее вам нужно распаковать скачанный архив в удобное для вас место, а затем добавить его в переменную PATH. Чтобы убедиться, что драйвер успешно установлен, запустите командную строку и введите «chromedriver --version» (без кавычек). Если всё сделано правильно, вы увидите номер версии
4. Затем запустите файл main.py
5. Если Вы хотите скрыть браузер и работать только в командной строке, тогда раскомментируйте 59 строчку кода в функции main().
