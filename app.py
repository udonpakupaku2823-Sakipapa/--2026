import streamlit as st

options = ["京成杯", "日経新春杯", "フェアリーＳ", "シンザン記念", "中山金杯", "京都金杯"]

# Streamlit のコンボボックス
enemy = st.selectbox("レースを選択してください", options)

# 選択されたレースに応じて画像を表示
if enemy:
    # ファイル名を辞書で管理
    image_files = {
        "京成杯": "0118京成杯.png",
        "日経新春杯": "0118日経新春杯.png",
        "フェアリーＳ": "0111フェアリーS.png",
        "シンザン記念": "0112シンザン記念.png",
        "中山金杯": "0104中山金杯.png",
        "京都金杯": "0104京都金杯.png",
    }

    filename = image_files.get(enemy)

    st.write(f"選択されたレース：{enemy}")

    # 画像表示
    st.image(filename, width=800)
