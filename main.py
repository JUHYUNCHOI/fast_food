import requests
import streamlit as st
import item_container as c

head = st.container()
body = st.container()
foot = st.container()


pre_search_input = ''
search_input = head.text_input('패스트푸드점 찾기: ', placeholder='검색 키워드 입력')
search_button = head.button('검색')

if search_button or pre_search_input != search_input:
    search_content = {'searchKeyword': search_input}
    # parameter = {'page': 5, 'count': 10}
    response = requests.get('https://floating-harbor-78336.herokuapp.com/fastfood', params=search_content)
    response_json = response.json()

    info_list = response_json['list']
    total = response_json['total']

    body.write(f'총 {total}개의 패스트푸드점을 찾았습니다.')

    for i in range(len(info_list)):
        item = info_list[i]
        c.getItemLook(body, i+1, item['name'], item['addr'])

    pre_search_input = search_input

