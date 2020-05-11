#Importing Libraries
import glassdoor_scraper as gs
import pandas as pd
path = "E:/Data Science Project/Salary Estimator/ds_salary_proj/chromedriver"

df = gs.get_jobs('data scientist',15, False, path, 15)

#Extra
from selenium.common.exceptions import StaleElementReferenceException

def _loop_is_text_present(text, max_attempts=3):
    attempt = 1
    while True:
        try:
            return self.browser.is_text_present(text)
        except StaleElementReferenceException:
            if attempt == max_attempts:
                raise
            attempt += 1

        