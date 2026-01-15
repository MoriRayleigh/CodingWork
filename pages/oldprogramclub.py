import streamlit as st
import sys
import os

# --- 【ここが重要】親フォルダ（一つ上）を読み込めるようにする魔法 ---
# 現在のファイルの場所から見て「..（一つ上）」を検索パスに追加
sys.path.append(os.path.abspath(os.path.dirname(__file__) + "/.."))
import components 

# --- 共通部品を表示 ---
components.display_hero_section()

# ページ設定
st.set_page_config(page_title="大人のプログラミングクラブ", page_icon="SP")

# タイトル
st.title("大人のプログラミングクラブ 商品説明ページ")

# 商品説明セクション（Stripe要件1：商品内容）
st.header("サービス内容")
st.write("""
『ゆるく、長く、確実に』をコンプとにJava言語を使ったWebアプリ開発スキルを学びます。
""")

# 価格
st.info("受講料金: 月額1,000円（税込）※サブスク契約")
st.write("""
24ヶ月で卒業を目標に学んでいただきます。
""")

st.markdown("---")

# 商品詳細セクション
st.header("学ぶ内容")
st.write("""
1.HTML/CSSの基礎とコーディング
         
2.Javaの基礎と実務レベルのコーディング
         
3.SQLの基礎と実務レベルのコーディング
         
4.Servlet/JSPの基礎と実務レベルのコーディング
         
5.Webアプリ設計

6.AWS

""")

