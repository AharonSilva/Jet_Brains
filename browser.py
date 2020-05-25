import os
import sys
from collections import deque
import requests
from bs4 import BeautifulSoup
import string
from colorama import init
from colorama import Fore, Back, Style


print(Fore.BLUE + 'some red text')
print(Style.DIM + 'and in dim text')


# version 1.3   completely remade: only accepts known web pages
# version 1.4   added en.wikipedia.org
# version 2.0   implemented a browser history (stack) that provides a 'back' function to the user
# version 2.1   does not add a page to the browser history if it is the most recent one
# version 3.0   - this version searches for real web pages and prints out the server response
#               - system was remade to work with real URLs and safe real tabs
#               - note a) pages are only added to history if not the most recent one (like 2.1)
#               - note b) first local page is loaded if searched key-word matches any (!) part of the original site
# version 4.0   - uses library BeautifulSoup to parse the text from a website and show it to the user
# version 4.1   - strips \n and non ascii letters from the output, looks ONLY for 'p' tags
# version 4.2   - looks for more tags than 4.1 ('p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'a' 'ul', 'ol', 'li')

class Browser:
    init()
    ERROR_WRONG_URL = 'Error: Incorrect URL'
    FILE_EXTENSION = '.txt'  # extension of the files that store the web pages
    HTTPS_PROTOCOL = 'https://'
    NAVIGABLE_STRING = '<class \'bs4.element.NavigableString\'>'
    ALL_ASCII_LETTERS = tuple(string.ascii_letters)
    TAGS_TO_RESOLVE = ('p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'a' 'ul', 'ol', 'li')

    def __init__(self):
        self.exit = False
        self.user_input = ''
        self.dir_name = os.getcwd()     # default: current working directory
        self.web_page_object = None     # IMPORTANT: this is used to store a web page that was requested by .get(URL)
                                        # var is cleared at the end of every browser iteration
        self.browser_history = deque()  # this stack saves all web pages the user enters (during the session)

    # ## system functions
    #
    def look_up_saved_pages(self, searched):
        # looks for a file that contains parameter string 'searched'
        # finds only the first occurance of string 'searched'
        # returns file names without file extension
        for file in os.listdir(self.dir_name):
            if searched in file:
                return file.replace(self.FILE_EXTENSION, '')
        return None

    def is_web_page_saved(self, url):
        # looks for a file that exactly matches the input url
        for file in os.listdir(self.dir_name):
            if file == url + self.FILE_EXTENSION:
                print('DEBUG this site was already saved', url)
                return True
        return False

    def get_page_path(self, page_name):
        return self.dir_name + '\\' + page_name + self.FILE_EXTENSION

    def scrape_web_page(self):
        # returns a list of all text on the requested web page
        soup = BeautifulSoup(self.web_page_object.content, 'html.parser')
        # get site html
        site_main = soup.children
        html = None
        body = None
        for element in site_main:
            if element.name == 'html':
                html = element
                break
        # get site body
        for element in list(html.children):
            if element.name == 'body':
                body = element
                break
        # resolve all <p> tags and print the text
        all_text = []
        for tag in body.find_all(self.TAGS_TO_RESOLVE):
            all_text.append(tag.get_text().strip().replace('\n', ' '))
        return all_text

    def save_web_page(self, url):
        path = self.get_page_path(url)
        with open(path, 'w', encoding='utf-8') as wp:
            page_text = self.scrape_web_page()
            for line in page_text:
                wp.write(line + '\n')

    def is_string_web_page(self, string):
        # will return None, if an incorrect URL was requested
        # will assign the web page object to the class, if succesful request
        self.web_page_object = None
        try:
            self.web_page_object = requests.get(string)
        except:
            self.web_page_object = requests.get(self.HTTPS_PROTOCOL + string)
        finally:
            return self.web_page_object

    def print_web_page(self, page_name, online=True):
        if online:
            page_text = self.scrape_web_page()
            for line in page_text:
                print(line)
        else:
            path = self.get_page_path(page_name)
            print('DEBUG local path will be printed', path)
            with open(path, 'r', encoding='utf-8') as wp:
                print(wp.read())

    # ## browser history management
    #
    def browser_history_add_page(self, url):
        if self.browser_history_get_last_page() != url:
            self.browser_history.append(url)
            print('DEBUG browser history after adding', url, 'is now', self.browser_history)

    def browser_history_remove_last_page(self):
        # To avoid an error, we check whether the stack is empty here anyway
        if self.browser_history:
            self.browser_history.pop()
            print('DEBUG browser history after removing last element is now', self.browser_history)

    def browser_history_get_last_page(self):
        if self.browser_history:
            return self.browser_history[-1]
        return None

    def browser_history_is_not_first_site(self):
        return len(self.browser_history) > 1

    # ## user interaction
    #
    def manage_user_input(self):
        if self.user_input == 'exit':
            self.exit = True
        elif self.user_input == 'back':
            print('DEBUG back button')
            # implements the back button to the browser
            # if no previous web pages left, then simply do not show anything
            if self.browser_history_is_not_first_site():
                self.browser_history_remove_last_page()
                self.print_web_page(self.browser_history_get_last_page(), online=False)
        else:
            # 1. case: user inputs a correct URL
            if self.is_string_web_page(self.user_input):
                print('DEBUG this site exists')
                # convert web page by adding HTTPS in case URL was entered without
                # if the page was not opened yet, save it as a file in folder
                if not self.is_web_page_saved(self.user_input):
                    self.save_web_page(self.user_input)
                # print web page in both cases
                self.print_web_page('')
                # add the page to the stack of viewed pages (if no https, we add it here)
                self.browser_history_add_page(self.user_input)
            else:
                # 2. case: incorrect URL. check, if input refers to an already saved page
                # caution! web_page_object should be None from here
                print('DEBUG URL request did not work')
                local_web_page = self.look_up_saved_pages(self.user_input)
                if local_web_page is not None:
                    print('DEBUG local web page was found', local_web_page)
                    # print the web page, if user requests a locally saved page
                    self.print_web_page(local_web_page, online=False)
                    # add the page to the stack of viewed pages (if no https, we add it here)
                    self.browser_history_add_page(local_web_page)
                else:
                    # 3. case: no web page, also no known short form, return an error message
                    print(self.ERROR_WRONG_URL)

    # ## system core
    #
    def make_web_page_folder(self, folder_name):
        self.dir_name = folder_name
        if not os.path.exists(self.dir_name):
            os.makedirs(self.dir_name)

    def command_line_input(self):
        # if there is more than the script name as an argument, it is run from the shell
        # we want to create a folder for web pages if the user did request it
        # [0] script name [1] folder name
        args = sys.argv
        if len(args) == 2:
            self.make_web_page_folder(args[1])

    def browser_input(self):
        self.user_input = input()

    def clear_browser_iteration(self):
        self.user_input = ''
        self.web_page_object = None

    def run_browser(self):
        # command line input will only be executed, if the script was run from a command prompt (Windows)
        self.command_line_input()
        while not self.exit:
            self.browser_input()
            self.manage_user_input()
            self.clear_browser_iteration()


browser = Browser()
browser.run_browser()
