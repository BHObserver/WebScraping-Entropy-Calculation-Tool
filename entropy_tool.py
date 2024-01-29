from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time

def process_file(file_path, driver):
    # Replace 'your_website_url' with the actual URL of your webpage
    url = 'https://www.hiv.lanl.gov/content/sequence/ENTROPY/entropy_one.html?sample_input=1'

    try:
        driver.get(url)  # Open the URL for each file

        # Find the textarea element
        textarea = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "seq_input2")))
        textarea.clear()

        # Find the file input element
        file_input = driver.find_element("name", "FILESEQ_2")

        # Set the file path for the file input
        file_input.send_keys(file_path)

        # Submit the form
        submit_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//input[@type="button" and @value="Submit"]')))
        submit_button.click()

        print(f"Submitted file: {file_path}")

        # Wait for the result page to load
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//a[contains(@href, "download.cgi")]')))

        print("Result page loaded successfully.")

        # Click the download link
        download_link = driver.find_element("xpath", '//a[contains(@href, "download.cgi")]')
        download_link.click()

        print("Clicked the download link.")

        # Wait for the download to complete
        wait_for_download_completion(driver)

        print("Download completed successfully.")

        # Return the current working directory
        return os.path.expanduser('~') + '/Downloads'

    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def rename_zip(old_file_path, new_file_path):
    try:
        # Wait for the file to be fully downloaded
        wait_for_download_completion(driver)

        # Wait for a short duration to ensure the file is ready for renaming
        time.sleep(5)  # You may adjust this waiting time based on your download speed

        # Rename the downloaded file
        os.rename(old_file_path, new_file_path)
        print(f"Renamed file from {old_file_path} to {new_file_path}")
    except Exception as e:
        print(f"An error occurred while renaming the file: {e}")

def wait_for_download_completion(driver, timeout=20):
    try:
        WebDriverWait(driver, timeout).until(lambda d: d.execute_script("return document.readyState") == "complete")
    except Exception as e:
        print(f"An error occurred while waiting for download completion: {e}")

# Set up the WebDriver (assuming you have ChromeDriver installed)
driver = webdriver.Chrome()

try:
    # Specify the folder path containing your files
    folder_path = 'E:/Web_Scraping_Python/folder'  # Replace with the actual folder path

    # List all files in the folder
    file_list = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

    # Iterate over each file in the folder and process it
    for file_name in file_list:
        file_path = os.path.join(folder_path, file_name)
        downloads_path = process_file(file_path, driver)

        if downloads_path:
            # Specify the old and new file names
            old_file_name = 'Entropy_One.zip'
            new_file_name = os.path.basename(file_path).replace('.fas', '_Result.zip')

            # Construct the old and new file paths
            old_file_path = os.path.join(downloads_path, old_file_name)
            new_file_path = os.path.join(downloads_path, new_file_name)

            # Rename the downloaded file
            rename_zip(old_file_path, new_file_path)

finally:
    # Close the browser window after processing all files
    driver.quit()
