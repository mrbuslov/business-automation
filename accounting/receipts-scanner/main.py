import asyncio
import json

import aiofiles
from langchain_core.messages import HumanMessage

from app.consts import INITIAL_CHAT_HISTORY, FOLDER_PATH
from app.utils import ask_llm, html_to_docx


async def main():
    docx_path = f'{FOLDER_PATH}/receipts.docx'
    user_updates_input = "Generate an html report based on the images of receipts"
    chat_history = INITIAL_CHAT_HISTORY.copy()
    while True:
        result = await ask_llm(
            user_updates_input,
            chat_history
        )
        chat_history.append(HumanMessage(content=user_updates_input))
        chat_history.append(result)

        llm_response_dict = json.loads(result.content)

        print(llm_response_dict['message_to_user'])
        print('-' * 40)
        async with aiofiles.open(docx_path, 'wb') as f:
            await f.write(html_to_docx(llm_response_dict['html']))
            print(f"File saved to {docx_path}")

        updates = input("Would you like to add any updates to the report? (type n to exit): ")
        if updates == "n":
            break


if __name__ == "__main__":
    asyncio.run(main())
