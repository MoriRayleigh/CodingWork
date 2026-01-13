import streamlit as st
import sys
import os

# --- 【ここが重要】親フォルダ（一つ上）を読み込めるようにする魔法 ---
# 現在のファイルの場所から見て「..（一つ上）」を検索パスに追加
sys.path.append(os.path.abspath(os.path.dirname(__file__) + "/.."))
import components 

# ページ設定
st.set_page_config(page_title="コデワーク 自走コース", page_icon="SPR")

# --- 共通部品を表示 ---
components.display_hero_section()

# タイトル
st.title("コデワーク スパルタコース 商品説明ページ")

# 商品説明セクション（Stripe要件1：商品内容）
st.header("サービス内容")
st.write("""
6ヶ月でJava言語を使った、Webアプリケーション開発スキルを習得して頂きます。
         
※必ず毎週1回のコーチングを受けてください
""")

# 価格
st.info("受講料金: 750,000円（税抜）")
st.write("""
6ヶ月で卒業を目標に学んでいただきます。
""")

st.markdown("---")

# 商品詳細セクション
st.header("学ぶ内容")
st.write("""
1.HTML/CSS
         
2.Java オブジェクト指向
         
3.SQL
         
4.Servlet/JSP
         
5.Webアプリケーション開発/システム設計

6.AWSへの公開

7.案件獲得戦略
         
8.副業案件の実施
         
9.チャレンジ案件の実施（20～30万の案件をこなし、報酬を受け取ってください）

""")
