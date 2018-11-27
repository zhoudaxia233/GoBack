import sys
import argparse
import requests
from lxml import html

def get_num_of_commits(response): # param response: the return of requests.get() method
    tree = html.fromstring(response.content)
    xpath_to_commits_num = '//*[@id="js-repo-pjax-container"]//div[@class="overall-summary overall-summary-bottomless"]//li[@class="commits"]//span[@class="num text-emphasized"]/text()'
    res = tree.xpath(xpath_to_commits_num) # res is a list of results matching the xpath we specified
    num_of_commits = res[0].strip()
    num_of_commits = num_of_commits.replace(',', '') # to remove thousands separators in "num_of_commits"
    return int(num_of_commits)

def get_page_num_of_the_very_first_commit(response):
    num_of_commits_per_page = 35 # on GitHub, the number of commits demonstrated per page is 35 by default
    num_of_commits = get_num_of_commits(response)
    res = num_of_commits // num_of_commits_per_page
    if num_of_commits > num_of_commits_per_page and (num_of_commits % num_of_commits_per_page) != 0:
        res += 1
    return res

def _url_join(*args):
    return '/'.join(arg.strip('/') for arg in args)

def init():
    parser = argparse.ArgumentParser()
    parser.add_argument("url", help="url of the project on GitHub")
    parser.add_argument("-b", "--branch", help="name of the branch you want to check", type=str, default='master')
    args = parser.parse_args()
    return (args.url, args.branch)

def main():
    url_raw, branch = init()
    url = _url_join(url_raw, 'tree', branch)
    r = requests.get(url)

    status_code = r.status_code
    if status_code == 200:
        page_num = get_page_num_of_the_very_first_commit(r)
        res_url = _url_join(url_raw, 'commits', branch, '?page={}'.format(page_num))
        print(res_url)
    else:
        print("HTTP status code is {}, something is wrong!".format(status_code))
