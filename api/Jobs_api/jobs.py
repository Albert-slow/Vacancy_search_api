from fastapi import Request, Body, UploadFile, APIRouter
from database.jobservice import *
from urllib import request
from utilittys import *

import requests
from bs4 import BeautifulSoup
import aiohttp

jobs_router = APIRouter(prefix="/jobs", tags=["Управление запросами"])


@jobs_router.get("/api/search")
async def parse(link):
    url = generator(link)
    my_dict = {}
    id = 1
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            web_content = await response.text()
            beautiful_parse = BeautifulSoup(web_content, 'html.parser')
            for e in beautiful_parse.find_all('span', class_='serp-item__title-link-wrapper'):
                my_dict[id] = [e.text, e.find('a')['href']]
                id += 1
            return {"status": 1, "message": my_dict}


@jobs_router.post("/api/vacancy")
async def parse_vacancy(url, user_id: int, job_title: str, user_location: str, jobs_tag: str = None):
    my_dict = {}
    id = 1
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            web_content = await response.text()
            beautiful_parse = BeautifulSoup(web_content, 'html.parser')
            result = beautiful_parse.find('h1', class_='bloko-header-section-1')
            my_dict[id] = [result.text]
            result = beautiful_parse.find('div', class_='vacancy-title')
            my_dict[id].append(result.find('span', class_='magritte-text___pbpft_3-0-9 '
                                                          'magritte-text_style-primary___AQ7MW_3-0-9 '
                                                          'magritte-text_typography-label-1-regular___pi3R-_3-0-9').text)
            result = beautiful_parse.find('div', class_='wrapper-flat--H4DVL_qLjKLCo1sytcNI')
            my_dict[id].append(result.find('p', class_="vacancy-description-list-item").text)
            result = beautiful_parse.find('div', class_='wrapper-flat--H4DVL_qLjKLCo1sytcNI')
            my_dict[id].append(result.find('p', {'data-qa': "vacancy-view-employment-mode"}).text)
            my_dict[id].append(beautiful_parse.find('div', class_='g-user-content').text)
            id += 1
            register_job_db(user_id=user_id, job_title=job_title, job_city=user_location,
                            jobs_tag=jobs_tag)
            return {"status": 1, "message": my_dict}
