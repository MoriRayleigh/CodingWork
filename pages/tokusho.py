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
    ("法人名", "合同会社 挑与本願"),
    ("住所", "〒621-0834 京都府亀岡市篠町広田2丁目2-11"),
    ("電話番号", "050-1794-9184"),
    ("メールアドレス", "choyohongan0801.mori@gmail.com"),
    ("運営責任者", "森 翔一"),
    ("追加手数料", "特にございません。"),
    ("交換および返品に関する<br>ポリシー", "<b>【商品およびコース変更について】</b><br>別途相談可能ですので、ご相談ください。<br><br><b>【お客様都合による返金について】</b><br>デジタルコンテンツの性質上、決済完了後の「学習が進めらない」などのお客様都合による返品・返金・キャンセルはお受けできません。"),
    ("配達時間", "注文後もしくはご契約後、すぐに利用可能です。"),
    ("利用可能な決済手段", "クレジットカード決済または国内の銀行振込"),
    ("決済期間", "お申し込み時（ご利用のカード会社の規定に基づき引き落としが行われます）"),
    ("営業時間", "平日 10:00 〜 18:00（土日祝休み）"),
    ("販売価格", "各コース詳細ページに表示された価格に基づきます。<br>・自走コース: 16,500円（税込）<br>・自走コースSP: 16,500円（税込）<br>・スパルタコース: 825,000円（税込）<br>・大人のプログラミングクラブ: 月額1,000円（税込）"),
    ("商品代金以外の必要料金", "・消費税<br>・通信にかかる通信料"),
    ("動作環境<br>（推奨スペック）", "・インターネット接続環境<br>・PC（Mac OS または Windows OS）<br>・Google Chrome 最新版 推奨"),
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