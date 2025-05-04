import io
import json

from langchain_anthropic import ChatAnthropic
from langchain_core.messages import HumanMessage, BaseMessage, AIMessage
from langchain_core.tools import StructuredTool

from app.consts import LATEST_MODEL, OUTPUT_STRUCTURE, ANTHROPIC_API_KEY

from htmldocx import HtmlToDocx
from docx import Document as DocxDocument

model = ChatAnthropic(
    model=LATEST_MODEL,
    temperature=0,
    timeout=None,
    max_retries=2,
    api_key=ANTHROPIC_API_KEY
)


async def final_response_formatter(response_dict: dict) -> None:  # noqa
    return None


def response_structure_tool() -> StructuredTool | None:
    return StructuredTool.from_function(
        coroutine=final_response_formatter,
        name=final_response_formatter.__name__,
        description="You MUST always use this tool to structure your response to the user.",
        args_schema=OUTPUT_STRUCTURE,
    )


async def ask_llm(
        prompt: str,
        chat_history: list[BaseMessage] | None = None
) -> AIMessage:
    # bind tools so that LLM could respond with structure output
    model_w_tools = model.bind_tools([response_structure_tool()])
    # call llm with history
    res = await model_w_tools.ainvoke(
        [
            *(chat_history or []),
            HumanMessage(content=prompt),
        ]
    )
    # find the tool call with structured output and return the passed values
    tool_call_output = next((
        i for i in res.tool_calls
        if i['name'] == final_response_formatter.__name__
    ), None)
    return AIMessage(content=json.dumps(tool_call_output['args']))


def html_to_docx(html_content: str) -> bytes:
    # Adds breaklines to file_content for hmtldocx lib (lib bug)
    html_content = "\n" + html_content.strip() + "\n"

    document = DocxDocument()
    style = document.styles["Normal"]
    font = style.font
    font.name = "Arial"

    with io.BytesIO() as buffer:
        new_parser = HtmlToDocx()
        new_parser.table_style = "TableGrid"
        new_parser.add_html_to_document(html_content, document)
        document.save(buffer)
        return buffer.getvalue()
