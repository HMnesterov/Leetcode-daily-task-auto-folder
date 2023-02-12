import pathlib
import time

from bs4 import BeautifulSoup
from selenium import webdriver

# Settings
absolute_path = ''
solution_file_type = 'py'  # .py, .c, .js


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
    task_link = "https://leetcode.com/" + data.get('href')
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




def create_folder_and_files(data: dict, absolute_path):
    task_link, task_name, task_difficulty = data.get('task_link'), data.get('task_name'), data.get('task_difficulty')
    task_description = parse_task_page(task_link)









if __name__ == '__main__':
    url = "https://leetcode.com/problemset/all/"

    create_folder_and_files(get_data_about_task(get_html(url)), absolute_path)
