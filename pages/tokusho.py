import streamlit as st
import sys
import os

# 親フォルダのcomponentsを読み込む設定
sys.path.append(os.path.abspath(os.path.dirname(__file__) + "/.."))
import components 

# ページ設定
st.set_page_config(page_title="特定商取引法に基づく表記", page_icon="⚖️")

# 共通部品（ロゴなど）
components.display_hero_section()

st.title("特定商取引法に基づく表記")
st.write("特定商取引法に基づき、以下のとおり表示いたします。")

st.markdown("---")

# スタイリング調整（表を見やすくする）
st.markdown("""
<style>
    td { vertical-align: top !important; }
</style>
""", unsafe_allow_html=True)

# 情報を定義
data = [
    ("販売業者", "合同会社 挑与本願"),
    ("運営統括責任者", "森 翔一"),
    ("所在地", "〒621-0834 京都府亀岡市篠町広田2丁目"),
    ("電話番号", "050-1794-9184"),
    ("メールアドレス", "choyohongan0801.mori@gmail.com"),
    ("営業時間", "平日 10:00 〜 18:00（土日祝休み）"),
    ("販売価格", "各コース詳細ページに表示された価格に基づきます。<br>・自走コース: 16,500円（税込）<br>・自走コースSP: 16,500円（税込）<br>・スパルタコース: 825,000円（税込）"),
    ("商品代金以外の必要料金", "・消費税<br>・通信にかかる通信料"),
    ("お支払い方法", "クレジットカード決済"),
    ("代金の支払時期", "お申し込み時（ご利用のカード会社の規定に基づき引き落としが行われます）"),
    ("商品の引渡時期", "決済完了後、24時間以内にメールにて詳細を送付し、即時利用可能となります。"),
    ("動作環境<br>（推奨スペック）", "・インターネット接続環境<br>・PC（Mac OS または Windows OS）<br>・Google Chrome 最新版 推奨"),
    ("キャンセル・返品について<br>（お客様都合）", "<b>【お客様都合による返金】</b><br>デジタルコンテンツの性質上、決済完了後の「学習が進めらない」などのお客様都合による返品・返金・キャンセルはお受けできません。"),
    ("キャンセル・返品について<br>（不良品・不具合）", "<b>【不具合等による対応】</b><br>提供するコンテンツやシステムに瑕疵（不具合）があり、受講が不可能であると弊社が認めた場合は、速やかに修正・再提供を行います。<br>再提供が困難な場合に限り、当該代金の返金に応じます。上記連絡先（メールまたは電話）までご連絡ください。")
]

# テーブルとして表示
for label, content in data:
    st.markdown(f"""
    <div style="display: flex; border-bottom: 1px solid #ddd; padding: 15px 0;">
        <div style="width: 30%; font-weight: bold; color: #333;">{label}</div>
        <div style="width: 70%; color: #555;">{content}</div>
    </div>
    """, unsafe_allow_html=True)

st.write("")
st.caption("お問い合わせは上記メールアドレスまでお願いいたします。")