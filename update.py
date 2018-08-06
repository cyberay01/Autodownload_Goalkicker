from selenium import webdriver
import os, shutil, json

path_json = open("driver_path.json").read()
path_data = json.loads(path_json)

driver_path = path_data['driver_path']
folder_path = path_data['folder_path']
download_path = path_data['download_path']

def update_folder(target_folder, filename):
    if not os.path.exists(folder_path):
        os.mkdir(folder_path)
    move_file = download_path + "\\" + filename
    while not os.path.exists(move_file):
        pass
    shutil.move(move_file, target_folder + "\\" + filename)

def task():
    browser = webdriver.Chrome(exectuable_path=driver_path)
    browser.get("https://books.goalkicker.com/")
    books_url = []
    book_container = browser.find_elements_by_class_name("bookContainer")
    for element in book_container:
        link = element.find_element_by_css_selector("a").get_attribute("href")
        books_url.append(link)
    for url in books_url:
        browser.get(url)
        browser.find_element_by_class_name("download").click()
        innertext = browser.execute_script("return arguments[0].textContent", browser.find_element_by_id("footer"))
        split_text = innertext.split(" ")
        file_name = split_text[0]
        print("Downloading " + file_name)
        update_folder(folder_path, file_name)
    browser.close()

task()
        