# AI-Powered Codeless UI Test Automation Framework

This project is an AI-driven open-source test automation framework that enables
codeless UI test execution using natural language prompts. Just describe your test
steps in plain English, and let the AI agent handle browser automation intelligently.
---
## 🚀 Features:
- Codeless test automation via natural language input
- AI-driven interpretation of tasks using Google Gemini
- Browser automation powered by Playwright
- Screenshot capture and JSON result generation
- Intelligent fallback mechanisms for flaky UI elements
---
## 🛠️ Tech Stack:
- Python (Asyncio)
- Google Gemini API via LangChain
- Pydantic for input validation
- Playwright (via browser_use.agent)
- Custom AI Agent Logic
---
## 💡 How It Works:
1. Define a task using plain English instructions.
2. The AI model interprets and breaks down the steps.
3. The agent drives the browser to perform those actions.
4. Final results, including screenshots and structured data, are generated.
---
## 📄 Sample Task:
task = (
- 'Important: I am a UI Automation tester validating the tasks. '
- 'Open website https://www.saucedemo.com/. '
- 'Log in using the username and password provided on the same page. '
- 'After logging in, add to cart the first 2 products. '
- 'Click on the Cart icon at the top right and navigate to the Your Cart page. '
- 'Click on Checkout, enter First Name as Kiran, Last Name as M, and Zip/Postal Code as 4321, then click on Continue. '
- 'Click on the Finish button at the bottom of the page. '
- 'Verify that the message "Thank you for your order!" is displayed.'
)
---
## 🔐 Set your Gemini API Key
os.environ["GEMINI_API_KEY"] = "your_actual_api_key_here"  # Replace this

async def SiteValidation():
    api_key = os.environ["GEMINI_API_KEY"]
    llm = ChatGoogleGenerativeAI(model='gemma-3-27b-it', api_key=SecretStr(api_key))
    agent = Agent(task, llm, use_vision=True)
    history = await agent.run()
    result = history.final_result()
    print("\n✅ Final Test Result:")
    print(result)
---
## 📦 Output:
- Final test result displayed in console
- Screenshots captured for visual proof (if supported)
- JSON structured data for each step (if enabled)