from osintbuddy.elements import TextInput
import osintbuddy as ob

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class Username(ob.Plugin):
    label = "Username"
    color = "#BF288D99"
    elements = [
        TextInput(label="Username", icon="user-search"),
    ]
    icon = "user-search"
    author = ["OSIB", "Artemii"]
    description = "Investigate usernames used as identification"

    @ob.transform(label='To checkuser.vercel.app', icon='user')
    async def to_checkuser(self, entity):
        with use.get_driver() as driver:
            driver.get('https://checkuser.vercel.app/')
            driver.find_element(By.XPATH, "/html/body/div/div/div/div/div/div[1]/div/div/input").send_keys(entity.username)
            driver.find_element(By.XPATH, '//*[@id="button-addon2"]').click()
            WebDriverWait(driver, 90).until(
                EC.text_to_be_present_in_element((By.XPATH, "/html/body/div/div/div/div/div/div[1]/div/h5"), "Total Scanned Services: 74 / 74")
            )
            records = driver.find_elements(By.XPATH, "/html/body/div/div/div/div/div/div[2]/div/div[2]/div/a")
            data = []
            username_profile = await ob.Registry.get_plugin('username_profile')
            for elm in records:
                href = elm.get_attribute('href')
                text = elm.get_attribute('innerText')
                if "Registered" in text:
                    blueprint = username_profile.create(
                        profile_link=href,
                    )
                    data.append(blueprint)
            return data
