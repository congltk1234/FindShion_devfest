import streamlit as st
from support_func import *
from langchain_func import *
from datetime import date
import requests
from PIL import Image
from io import BytesIO

import pandas as pd

st.set_page_config(page_title="FindShion✨", page_icon="👚",
                layout="wide", initial_sidebar_state='expanded')


@st.cache_data
def load_csv():
    articles_3000 = pd.read_csv('assets/article_3000.csv')
    articles_3000['article_id'] = articles_3000['article_id'].astype(str)

    return articles_3000
articles_3000 = load_csv()

def url(item_id):
    url = 'https://www2.hm.com/en_us/productpage.0'+ str(item_id) +'.html'
    return url

def recomend_list_label(recommed_label,describe):
    with st.container():  
            container = st.expander(recommed_label['name'], expanded =True)
            with container:
                st.caption(describe)
                cols = st.columns(3)
                for i in range(len(recommed_label['id'])):
                    item = articles_3000[articles_3000['article_id'] == recommed_label['id'][i]]
                    with cols[i]:
                        path ='assets/img/'+ item['path'].values[0]
                        anh = Image.open(path)
                        st.image(anh)
                        item_url = url(recommed_label['id'][i])
                        st.write(f"**[{item['prod_name'].values[0]}]({item_url})**")


def main():
    with st.sidebar:
        with st.form("My form"):
            st.markdown("#### Người dùng nhập thông tin")
            birthday = st.date_input("Ngày sinh", min_value=date(1930, 1, 1))
            type_char = st.select_slider('Tính cách', options=['Hướng nội', 'Hướng ngoại'])
            gender = st.select_slider('Giới tính', options=['Nữ', 'Nam'])
            bodyShape =  st.radio(
            "Dáng người của bạn",
            [":pear: Hình quả lê", ":hourglass: Đồng hồ cát", ":large_yellow_square: Hình chữ nhật", ":apple: Quả táo", ":small_red_triangle_down: Tam giác ngược"],
            )

            style = st.text_input("Phong cách bạn muốn thử?")

            my_upload = st.file_uploader("Khám phá phong cách mới", type=["png", "jpg", "jpeg"])
            print(my_upload)
            submit = st.form_submit_button("Bắt đầu")

#########################################################################################
################ Sector article ###########################################
#########################################################################################
    img =Image.open('bg.png')
    
    placeholder = st.empty()
    placeholder.image(img)

    if submit:
        placeholder.empty()
        zodiac = zodiac_sign(birthday.day,birthday.month)
        age = date.today().year - birthday.year

        user_input = {
            'Cung hoàng đạo':zodiac,
            'Tính cách' : type_char,
            'Giới tính' : gender,
            'Hình dáng cơ thể' : bodyShape,
            'Phong cách':style,
            'Tuổi': age
        }

        

        # img =Image.open('logo.png')
        # st.image(img, width=60)

        st.header(':crystal_ball: Kết quả tư vấn từ FindShion team', divider='rainbow')

        st.title('Đây là tín hiệu vũ trụ gửi đến :red[**Bạn**] :magic_wand:')

        insight = get_user_insight(user_input)
        st.write(insight)


        img =Image.open(my_upload)
        byte_io = BytesIO()
        img.save(byte_io, 'png')
        byte_io.seek(0)
        response = requests.post(url='http://127.0.0.1:8000/img_object_detection_outfit', files={'file': ('file.PNG', byte_io, 'image/png')})
        
        recommend_dict = response.json()
        recommend_list = recommend_dict['item']

        list_desc_prompt= ''
        for label in recommend_list:   
            recommed_ids = label['id']
            list_desc = []
            for i in recommed_ids:
                item = articles_3000[articles_3000['article_id'] == i]
                list_desc.append(item['detail_desc'].values[0])
            list_desc_prompt = list_desc_prompt + label['name'] + ': '+ max(list_desc, key=len)+'\n\n'

        response_desc = get_recommend_describe(insight,list_desc_prompt)
        response_desc = response_desc.split('<break>')
        st.image(img)
        st.write(len(response_desc))

        for i in range(len(response_desc)):
            try:
                recomend_list_label(recommend_list[i], response_desc[i])
            except:
                pass


if __name__ == '__main__':
    main()
