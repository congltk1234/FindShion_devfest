import os
import openai
from langchain.prompts import ChatPromptTemplate
from langchain.chat_models import ChatOpenAI


# To control the randomness and creativity of the generated
# text by an LLM, use temperature = 0.0
chat = ChatOpenAI(temperature=0.0, model= "gpt-3.5-turbo-0301",
                openai_api_key= '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',
                model_kwargs={'top_p': 0.1})



def get_user_insight(user_input):
    prompt_insight_template = """Bạn là người có nhiều hiểu biết về tính cách, Hãy phân tích và đưa ra insight xu hướng và sở thích liên quan đến thời trang

    my_profile: {user_input}

    Trả lời thân thiện nhiều nội dung thú vị từ những câu hỏi sau:
    - Người này có điều gì đặc biệt và thú vị?
    - Phong cách theo đuổi có gì tương đồng với cung hoàng đạo của họ?
    - Nêu ngẫu nhiên những yếu tố hoặc tiềm năng ẩn chứa bên trong con người họ.
    - Đưa ra ngẫu nhiên Màu sắc may mắn phù hợp và giải thích?

    Kết quả trả lời và phản hồi trong một đoạn văn ngôn ngữ tiếng Việt , sử dụng các đặc điểm cá nhân trong phản hồi càng nhiều càng tốt cung cấp nhiều insight thú vị về cung hoàng đạo.
    (chú ý: thay "người này" thành "bạn")
    """

    prompt = ChatPromptTemplate.from_template(template=prompt_insight_template)

    messages = prompt.format_messages(
        user_input = user_input,
    )

    response = chat(messages)

    return response.content


def get_recommend_describe(insight, item_describe):
    review_template_recommends = """Bạn là một nhà tư vấn thời trang chuyên nghiệp, từ insight được cung cấp kết hợp với những sản phẩm sau đây:

    insight: {insight}

    list_items: {items}

    Hãy mô tả chi tiết và cung cấp người dùng những tips phối đồ thú vị liên quan đến cung hoàng đạo với những sản phẩm đề xuất bằng ngôn ngữ tiếng Việt. (Giữa mỗi sản phẩm, hãy thêm <break>)

    """

    prompt2 = ChatPromptTemplate.from_template(template=review_template_recommends)

    messages = prompt2.format_messages(
        insight = insight,
        items = item_describe,
    )

    response = chat(messages)
    return response.content