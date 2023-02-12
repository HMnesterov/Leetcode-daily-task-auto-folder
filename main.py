import pathlib
from pathlib import Path
import time
import os
from bs4 import BeautifulSoup
from selenium import webdriver

absolute_path = r''


def change_work_directory(path):
    current_directory = Path(path)
    os.chdir(current_directory)
    return current_directory


def get_html(url: str):
    browser = webdriver.Chrome()
    browser.get(url)
    time.sleep(5)
    html = browser.page_source
    browser.quit()
    return html


def get_data_about_task(html: str):
    soup = BeautifulSoup(html, 'lxml')
    tasks_row = soup.find('div', role='rowgroup')
    task_line = tasks_row.find('div', role='row').find_all('div', class_='mx-2 py-[11px]')
    data = task_line[1].find('a')
    task_link = "https://leetcode.com" + data.get('href')
    task_name = data.text
    task_difficulty = task_line[4].find('span').text

    return {
        'task_link': task_link,
        'task_name': task_name,
        'task_difficulty': task_difficulty
    }


def parse_task_page(url: str):
    soup = BeautifulSoup(get_html(url), 'lxml')
    description = soup.find('div', class_='_1l1MA')

    complicated_text = ''''''
    for p in description.find_all('p')[:-5]:
        complicated_text += p.text + '\n'
    examples = description.find_all('pre')

    for indx, ex in enumerate(examples, 1):
        complicated_text += f'Example {indx}' + '\n' + ex.text + '\n'

    return complicated_text


def create_folder_and_files(absolute_path: str, data: dict):
    task_link, task_name, task_difficulty = data.get('task_link'), data.get('task_name'), data.get('task_difficulty')
    task_description = parse_task_page(task_link)
    if not task_link or not task_name or not task_link:
        return

    current_directory = Path(absolute_path)
    os.chdir(current_directory)
    for difficult in current_directory.iterdir():
        if task_difficulty == difficult.name:
            break
    else:

        pathlib.Path(f"{task_difficulty}/").mkdir(parents=True, exist_ok=True)

    current_directory = change_work_directory(current_directory / task_difficulty)

    pathlib.Path(f"{task_name}/").mkdir(parents=True, exist_ok=True)

    current_directory = change_work_directory(current_directory / task_name)

    with open("task_description.txt", 'w', encoding='utf-8') as file, open("solution.py", "w", encoding='utf-8'):
        file.write(task_description)


if __name__ == '__main__':
    while True:
        url = "https://leetcode.com/problemset/all/"
        create_folder_and_files(absolute_path, get_data_about_task(get_html(url)))
        time.sleep(60 * 60 * 12)
