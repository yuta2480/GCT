# %%
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from datetime import timedelta
from matplotlib.ticker import FuncFormatter

def format_y_axis_time(seconds, _):
    minutes, seconds = divmod(seconds, 60)
    return f"{int(minutes):02d}:{int(seconds):02d}"

def plot_vehicle_schedule(vehicle_numbers, trip_durations):
    # トリップ数
    num_trips = len(trip_durations[0])

    # 横軸の位置を設定
    x = np.arange(len(vehicle_numbers))

    fig, ax = plt.subplots()
    ax.invert_yaxis()

    # トリップごとに棒グラフを作成
    bottom = np.zeros(len(vehicle_numbers))
    for i in range(num_trips):
        durations = [trip_duration[i] for trip_duration in trip_durations]
        plt.bar(x, durations, bottom=bottom, alpha=0.7, label=f'Trip {i+1}')
        bottom += durations

        # ラベルをプロット
        for j, duration in enumerate(durations):
            label = f'Trip {i+1}'
            plt.text(x[j], bottom[j] - duration / 2, label, ha='center', va='center')

    # x軸に車両番号を表示
    plt.xticks(x, vehicle_numbers)

    # グラフの軸ラベルやタイトルを設定
    plt.xlabel('Vehicle Number')
    plt.ylabel('Duration')
    plt.title('Vehicle Schedule')

    # 縦軸のラベルを時:分形式に変換
    formatter = FuncFormatter(format_y_axis_time)
    plt.gca().yaxis.set_major_formatter(formatter)


    # プロットを表示
    st.pyplot(fig,use_container_width=50)
#     plt.show()


# サンプルデータ
vehicle_numbers = ['Vehicle 1', 'Vehicle 2', 'Vehicle 3', 'Vehicle 4', 'Vehicle 5']
trip_durations = [
[10, 15, 20, 18, 12],  # 1つ目のトリップ
[8, 11, 16, 14, 9],    # 2つ目のトリップ
[13, 17, 22, 19, 16],  # 3つ目のトリップ
[9, 12, 15, 11, 8],    # 4つ目のトリップ
[11, 14, 18, 16, 13]   # 5つ目のトリップ
]

def importCSV():
     import pandas as pd
     df=pd.DataFrame(trip_durations, index=vehicle_numbers, columns=[f'Trip{i}' for i in range(1,6)])
     st.text('インポートするデータサンプル(各トリップの経過分)')
     st.dataframe(df)

def drawGraph():
     # プロットを作成
     plot_vehicle_schedule(vehicle_numbers, trip_durations)
     

st.button('import csv', on_click=importCSV)
st.button('集計↓', on_click=drawGraph)
# importCSV()
# drawGraph()