import requests
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_scores_service(url):
    try:
        # Set up the Selenium WebDriver
        driver = webdriver.Chrome()  # Ensure you have ChromeDriver installed
        driver.get(url)

        # Locate the score element by its ID and retrieve the score value
        score_element = driver.find_element(By.ID, "score")
        score = int(score_element.text)

        # Check if the score is between 1 and 1000
        if 1 <= score <= 1000:
            return True
        else:
            return False
    except Exception as e:
        print(f"An error occurred: {e}")
        return False
    finally:
        driver.quit()


def main_function():
    url = "http://localhost:8777"  # Replace with your actual URL
    if test_scores_service(url):
        exit(0)
    else:
        exit(-1)


if __name__ == "__main__":
    main_function()
