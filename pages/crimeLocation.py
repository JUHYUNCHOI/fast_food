import streamlit as st
import pandas
import os

# import matplotlib.pyplot as plt
# import matplotlib as mpl

def drawCrimeLocationPage():
    current_path = os.path.abspath(os.path.dirname(__file__))
    csv_file = os.path.join(current_path, '..', 'resources', '대검찰청_범죄발생지.csv')

    csv_read = pandas.read_csv(csv_file, encoding='CP949')

    # df = pandas.DataFrame(csv_read)
    # st.dataframe(df, 1000, 1000)
    #
    # # 위에서 기본 5줄 읽어오기
    # st.dataframe(csv_read.head())
    # print(csv_read.head())
    #
    # # 위에서 기본 100줄 읽어오기
    # st.dataframe(csv_read.head(100))
    # print(csv_read.head(100))
    #
    # # 뒤에서 기본 5줄 읽어오기
    # st.dataframe(csv_read.tail())
    # print(csv_read.tail())
    #
    # # 뒤에서 기본 100줄 읽어오기
    # st.dataframe(csv_read.tail(100))
    # print(csv_read.tail(100))
    #
    # # 데이터프레임의 자료형, 행 인덱스의 종류와 개수, 열의 갯수와 자료형, 메모리 사용량 등의 정보를 확인 할 수 있음
    # print(csv_read.info())
    #
    # # 데이터프레임에 대한 통계정보를 요약해 줌. 열의 데이터 개수, 평균값, 표준편차, 최소값 등등
    # st.dataframe(csv_read.describe())
    # print(csv_read.describe())
    #
    # # column의 선택, 추가, 변경, 삭제
    # print(csv_read)
    #
    # # column 선택하여 읽어오기
    # print(csv_read['서울_종로'])
    #
    # # column 추가: 모든 row에 0이 추가된다.
    # csv_read['추가'] = 0
    # print(csv_read)
    #
    # # column 추가: '서울_종로'에 있는 값이 복사되어 추가된다.
    # csv_read['추가1'] = csv_read['서울_종로']
    # print(csv_read)
    #
    # # column 삭제
    # csv_read['추가1'] = csv_read['서울_종로']
    # print(csv_read)
    # # 뒤에 둘 옵션 꼭 필요함. 기존 데이터 프레임에 변경내용을 반영하기 위해서는 inplace=True 옵션 필요
    # csv_read.drop('추가1', axis=1, inplace=True)
    # print(csv_read)
    #
    # # ----------------------------------------------------------------------
    # # row 선택, 추가, 변경, 삭제
    #
    # # index를 이용하여 row 선택 출력하기
    # row1 = csv_read.iloc[0]
    # print(row1)
    #
    # # row 이름을 이용하여 선택 출력하기
    # row1 = csv_read.loc[0]   # 지금 갖고 있는 데이터의 row가 숫자로 세팅 되어 있어서 0을 사용하게 되었음.
    # print(row1)
    # print(csv_read)
    #
    # # row추가
    # csv_read.loc['추가1'] = 0
    # print(csv_read)
    #
    # # row 삭제
    # csv_read.loc['추가1'] = 0
    # csv_read.drop('추가1', axis=0, inplace=True)
    # print(csv_read)
    #
    # # -------------------------------------------------
    # # 각 아이템 선택 변경
    #
    # # 선택 - index
    # e1 = csv_read.iloc[0, 1]
    # print(e1)
    # print(csv_read)
    #
    # # 선택 - row, column 이름
    # e1 = csv_read.loc[0, '서울_종로']
    # print(e1)
    # print(csv_read)
    #
    # # 멀티 선택 - row, column 이름
    # e1 = csv_read.loc[0:5, '서울_종로': '서울_용산']
    # print(e1)
    # print(csv_read)
    #
    # # 멀티 선택 - index
    # e1 = csv_read.iloc[0:5, 0:10]
    # print(e1)
    # print(csv_read)
    #
    # # 아이템 값 변경 - index
    # csv_read.iloc[0, 2] = 'aaaa'
    # print(csv_read)
    #
    # # 멀티 아이템 값 변경 - index
    # csv_read.iloc[0: 10, 0:2] = 'aaaa'
    # print(csv_read)
    #
    # # --------------------------------
    # # 데이터프레임을 외부 파일로 저장하기
    #
    # dict_data = {
    #     'c0': [1, 2, 3],
    #     'c1': [4, 5, 6]
    # }
    # df = pandas.DataFrame(dict_data, index=['r0', 'r1', 'r2'])
    #
    # csv_file_ouput = os.path.join(current_path, '..', 'ouput', 'result.csv')
    # # csv 파일로 저장
    # df.to_csv(csv_file_ouput)
    #
    # excel_file_ouput = os.path.join(current_path, '..', 'ouput', 'result.xlsx')
    # #excel로 저장
    # df.to_excel(excel_file_ouput)  # pip3 install openpyxl
    #
    # # 특정 column을 row로 정하기
    # csv_read.set_index('범죄분류', inplace=True)
    # print(csv_read)
    df = pandas.DataFrame(csv_read)
    # st.dataframe(df, 1000, 1000)
    # st.dataframe(csv_read, 1000, 1000)

    # https://docs.streamlit.io/library/api-reference/charts
    # 선 그래프 그리기
    #https: // wikidocs.net / 92089
    # pip3 install matplotlib
    # import matplotlib.pyplot as plt

    # fig = plt.figure(figsize=(500, 500), dpi=2, facecolor='red',edgecolor='black')
    # fig = plt.figure(figsize=(10,10))
    # # 전체 창을 가로 1칸, 세로 1칸으로 쪼개고 그 중 첫 번째 칸에 ax라는 이름의 axes를 생성한다.
    # ax1 = fig.add_subplot(1, 2, 1)
    # # 전체 창을 가로 1칸, 세로 2칸으로 쪼개고, 그 중 첫 번째 칸에 ax1, 두 번째 칸에 ax2를 생성한다.
    # ax2 = fig.add_subplot(1, 2, 2)

    # subplot
    # plt.subplot(3, 3, 1)
    # plt.subplot(3, 3, 3)
    # plt.subplot(3, 3, 5)
    # plt.subplot(3, 3, 9)

    # subplots
    # fig, axes = plt.subplots(2, 2)  # axes는 Axes객체의 2x2의 배열
    # axes[0][0].plot([1, 2, 3])
    # axes[1][0].plot([4, 5, 4, 5])

    # Axes
    # ax1 = plt.subplot(2, 2, 1)  # 4x4의 첫 번째
    # ax4 = plt.subplot(2, 2, 4)  # 4x4의 네 번째
    # ax1.plot([1, 2, 3, 4])  # 첫 번째에 그림을 그린다.
    # ax1.plot([2, 3, 2, 3])  # 첫 번째에 그림을 추가한다.
    # ax1.set_xlabel('foo')  # 첫 번째에 x 라벨을 추가한다.
    # ax1.set_ylabel('bar')  # 첫 번째에 y 라벨을 추가한다.
    # ax4.plot([5, 10, 20, 10])  # 네 번째에 그림을 그린다.
    # ax4.set_title('baz')  # 네 번째에 타이틀을 추가한다.

    # csv_read.set_index('범죄분류', inplace=True)
    #
    # font1 = {'family': 'serif',
    #          'color': 'b',
    #          'weight': 'bold',
    #          'size': 14
    #          }
    #
    # font2 = {'family': 'fantasy',
    #          'color': 'deeppink',
    #          'weight': 'normal',
    #          'size': 'xx-large'
    #          }
    # graph = plt.subplot(1, 1, 1)
    # # graph.set_xlabel('aaa')
    # # graph.set_ylabel('bbb')
    # plt.xlabel('X-Axis', labelpad=15, fontdict=font1)  # loc='right'
    # plt.ylabel('Y-Axis', labelpad=20, fontdict=font2)  # loc='top'
    # graph.set_title('cccc')
    # graph.plot(csv_read['서울_종로'])
    #
    # plt.show()

    # https://wikidocs.net/book/5011
    # 기본 그래프 그리기
    # import matplotlib.pyplot as plt
    #
    # plt.plot([1, 3, 7, 4])
    # plt.show()

    # import matplotlib.pyplot as plt
    #
    # plt.plot([1, 3, 7, 4], [1, 4, 9, 16])
    # plt.show()

    # 스타일 지정하기
    # import matplotlib.pyplot as plt
    #
    # plt.plot([1, 3, 7, 4], [1, 4, 9, 16], 'r*')  # red에 O로 표시, r-, r*, ro
    # plt.axis([0, 8, 0, 20])   # x축: 0~8, y축: 0~20
    # plt.show()

    # 여러 개의 그래프 그리기
    # import matplotlib.pyplot as plt
    # import numpy as np
    #
    # # 200ms 간격으로 균일하게 샘플된 시간
    # t = np.arange(0., 5., 0.2)
    #
    # # 빨간 대쉬, 파란 사각형, 녹색 삼각형
    # plt.plot(t, t, 'r--', t, t ** 2, 'bs', t, t ** 3, 'g^')
    # plt.show()

    # 레이블 사용하기
    # import matplotlib.pyplot as plt
    #
    # plt.plot([1, 2, 3, 4], [1, 4, 9, 16])
    # plt.xlabel('X-Label')
    # plt.ylabel('Y-Label')
    # plt.show()

    # 레이블 패딩
    # import matplotlib.pyplot as plt
    #
    # plt.plot([1, 2, 3, 4], [2, 3, 5, 10])
    # plt.xlabel('X-Axis', labelpad=15)
    # plt.ylabel('Y-Axis', labelpad=20)
    # plt.show()

    # font 정하기
    # import matplotlib.pyplot as plt
    #
    # font1 = {'family': 'serif',
    #          'color': 'b',
    #          'weight': 'bold',
    #          'size': 14
    #          }
    #
    # font2 = {'family': 'fantasy',
    #          'color': 'deeppink',
    #          'weight': 'normal',
    #          'size': 'xx-large'
    #          }
    #
    # plt.plot([1, 2, 3, 4], [2, 3, 5, 10])
    # plt.xlabel('X-Axis', labelpad=15, fontdict=font1)
    # plt.ylabel('Y-Axis', labelpad=20, fontdict=font2)
    # plt.show()

    # 라벨 위치 정하기
    # import matplotlib.pyplot as plt
    #
    # plt.plot([1, 2, 3, 4], [2, 3, 5, 10])
    # plt.xlabel('X-Axis', loc='right')
    # plt.ylabel('Y-Axis', loc='top')
    # plt.show()

    # 선 설명하기
    # import matplotlib.pyplot as plt
    #
    # plt.plot([1, 2, 3, 4], [2, 3, 5, 10], label='Price ($)')
    # plt.xlabel('X-Axis')
    # plt.ylabel('Y-Axis')
    # plt.legend()
    #
    # plt.show()

    # 선 설명의 위치 지정하기
    # import matplotlib.pyplot as plt
    #
    # plt.plot([1, 2, 3, 4], [2, 3, 5, 10], label='Price ($)')
    # plt.xlabel('X-Axis')
    # plt.ylabel('Y-Axis')
    # # plt.legend(loc=(0.0, 0.0))
    # # plt.legend(loc=(0.5, 0.5))
    # plt.legend(loc=(1.0, 1.0))
    # # plt.legend(loc='lower right')
    #
    # plt.show()

    # 열 개수 지정하기
    # import matplotlib.pyplot as plt
    #
    # plt.plot([1, 2, 3, 4], [2, 3, 5, 10], label='Price ($)')
    # plt.plot([1, 2, 3, 4], [3, 5, 9, 7], label='Demand (#)')
    # plt.xlabel('X-Axis')
    # plt.ylabel('Y-Axis')
    # # plt.legend(loc='best')          # ncol = 1
    # plt.legend(loc='best', ncol=2)  # ncol = 2
    #
    # plt.show()

    # 범위정하기
    # import matplotlib.pyplot as plt
    #
    # plt.plot([1, 2, 3, 4], [2, 3, 5, 10])
    # plt.xlabel('X-Axis')
    # plt.ylabel('Y-Axis')
    # plt.xlim([0, 5])  # X축의 범위: [xmin, xmax]
    # plt.ylim([0, 20])  # Y축의 범위: [ymin, ymax]
    #
    # plt.show()


    # 선 종류 지정하기
    # import matplotlib.pyplot as plt
    #
    # plt.plot([1, 2, 3], [4, 4, 4], '-', color='C0', label='Solid')
    # plt.plot([1, 2, 3], [3, 3, 3], '--', color='C0', label='Dashed')
    # plt.plot([1, 2, 3], [2, 2, 2], ':', color='C0', label='Dotted')
    # plt.plot([1, 2, 3], [1, 1, 1], '-.', color='C0', label='Dash-dot')
    # plt.xlabel('X-Axis')
    # plt.ylabel('Y-Axis')
    # plt.axis([0.8, 3.2, 0.5, 5.0])
    # plt.legend(loc='upper right', ncol=4)
    # plt.show()
    #
    # 또는.
    # import matplotlib.pyplot as plt
    #
    # plt.plot([1, 2, 3], [4, 4, 4], linestyle='solid', color='C0', label="'solid'")
    # plt.plot([1, 2, 3], [3, 3, 3], linestyle='dashed', color='C0', label="'dashed'")
    # plt.plot([1, 2, 3], [2, 2, 2], linestyle='dotted', color='C0', label="'dotted'")
    # plt.plot([1, 2, 3], [1, 1, 1], linestyle='dashdot', color='C0', label="'dashdot'")
    # plt.xlabel('X-Axis')
    # plt.ylabel('Y-Axis')
    # plt.axis([0.8, 3.2, 0.5, 5.0])
    # plt.legend(loc='upper right', ncol=4)
    # plt.tight_layout()
    # plt.show()

    # 선 끝모양 지정하기
    # import matplotlib.pyplot as plt
    #
    # plt.plot([1, 2, 3], [4, 4, 4], linestyle='solid', linewidth=10,
    #          solid_capstyle='butt', color='C0', label='solid+butt')
    # plt.plot([1, 2, 3], [3, 3, 3], linestyle='solid', linewidth=10,
    #          solid_capstyle='round', color='C0', label='solid+round')
    #
    # plt.plot([1, 2, 3], [2, 2, 2], linestyle='dashed', linewidth=10,
    #          dash_capstyle='butt', color='C1', label='dashed+butt')
    # plt.plot([1, 2, 3], [1, 1, 1], linestyle='dashed', linewidth=10,
    #          dash_capstyle='round', color='C1', label='dashed+round')
    #
    # plt.xlabel('X-Axis')
    # plt.ylabel('Y-Axis')
    # plt.axis([0.8, 3.2, 0.5, 5.0])
    # plt.legend(loc='upper right', ncol=2)
    # plt.tight_layout()
    # plt.show()

    # 눈금 표시하기
    # import numpy as np
    # import matplotlib.pyplot as plt
    #
    # x = np.arange(0, 2, 0.2)
    #
    # plt.plot(x, x, 'bo')
    # plt.plot(x, x ** 2, color='#e35f62', marker='*', linewidth=2)
    # plt.plot(x, x ** 3, color='forestgreen', marker='^', markersize=9)
    # plt.xticks([0, 1, 2])
    # plt.yticks(np.arange(1, 6))
    #
    # plt.show()

    # import matplotlib.pyplot as plt
    # import numpy as np
    #
    # x = np.arange(0, 2, 0.2)
    #
    # plt.plot(x, x, 'bo')
    # plt.plot(x, x ** 2, color='#e35f62', marker='*', linewidth=2)
    # plt.plot(x, x ** 3, color='springgreen', marker='^', markersize=9)
    # plt.xticks(np.arange(0, 2, 0.2), labels=['Jan', '', 'Feb', '', 'Mar', '', 'May', '', 'June', '', 'July'])
    # plt.yticks(np.arange(0, 7), ('0', '1GB', '2GB', '3GB', '4GB', '5GB', '6GB'))
    #
    # plt.show()



if __name__ == "__main__":
    drawCrimeLocationPage()