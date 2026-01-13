import streamlit as st
import sys
import os

# --- 【ここが重要】親フォルダ（一つ上）を読み込めるようにする魔法 ---
# 現在のファイルの場所から見て「..（一つ上）」を検索パスに追加
sys.path.append(os.path.abspath(os.path.dirname(__file__) + "/.."))
import components 

# ページ設定
st.set_page_config(page_title="コデワーク 自走コース SP", page_icon="SP")

# --- 共通部品を表示 ---
components.display_hero_section()

# ページ設定
st.set_page_config(page_title="コデワーク 自走コース SP", page_icon="SP")

# タイトル
st.title("コデワーク 自走コース SP 商品説明ページ")

# 商品説明セクション（Stripe要件1：商品内容）
st.header("サービス内容")
st.write("""
SpringBootでWebアプリケーションを作成することを目標に基礎知識を学びます。
         
※DI、AOP、SpringFrameworkとの関連性は省く
""")

# 価格
st.info("受講料金: 16,500円（税込）※サブスク契約")
st.write("""
3ヶ月で卒業を目標に学んでいただきます。
""")

st.markdown("---")

# 商品詳細セクション
st.header("学ぶ内容")
st.write("""
1.SpringBootとは
         
2.基本知識
         
3.フォームバリデーション
         
4.Tymeleaf
         
5.SpringBootプログジェクト

6.SpringBootでDB操作

7.セッション管理プログラム
         
8.ユーザー認証プログラム

9.例外プログラム

10.アプリケーション作成演習
""")

