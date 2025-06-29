import asyncio
import os
from browser_use.agent.service import Agent
from browser_use.agent.views import ActionResult
from browser_use.browser.context import BrowserContext
from browser_use.controller.service import Controller
from langchain_google_genai import ChatGoogleGenerativeAI
from pydantic import SecretStr, BaseModel


class CheckoutResult(BaseModel):
    login_status: str
    cart_status: str
    checkout_status: str
    Confirmation_message: str


controller = Controller(output_model=CheckoutResult)


@controller.action('Click on the Cart icon at the top right')
async def click_cart_page(browser : BrowserContext):
    page = await browser.pages[0]  # or use await browser.pages[0] if already opened
    current_url = page.url
    print(f"Current URL: {current_url}")

    # Click on the cart icon – adjust selector as needed
    await page.click("a.shopping_cart_link")
    return ActionResult(extracted_content=f'current url is {current_url}')


async def SiteValidation():
    os.environ[
        "GEMINI_API_KEY"] = ""  # Consider replacing this with a valid secure value

    task = (
        'Important: I am a UI Automation tester validating the tasks '
        'Open website https://www.saucedemo.com/ '
        'Log in using the username and password provided on the same page '
        'After logging in, Add to cart the first 2 products '
        'Click on the Cart icon at the top right and navigate to the Your Cart page '
        'Click on Checkout, enter First Name as Kiran, Last Name as M, and Zip/Postal Code as 4321, then click on Continue '
        'Click on the Finish button at the bottom of the page '
        'Verify that the message "Thank you for your order!" is displayed '
    )

    api_key = os.environ["GEMINI_API_KEY"]
    llm = ChatGoogleGenerativeAI(model='learnlm-2.0-flash-experimental', api_key=SecretStr(api_key))
    agent = Agent(task=task, llm=llm, controller=controller, use_vision=True)
    history = await agent.run()
    history.save_to_file('agentresults.json')
    test_result = history.final_result()
    print(test_result)


asyncio.run(SiteValidation())
