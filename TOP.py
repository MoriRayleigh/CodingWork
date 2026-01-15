import streamlit as st
import components  # 作ったファイルをインポート

# ページ設定
st.set_page_config(
    page_title="コデワーク コース一覧",
    page_icon="🏫",
    layout="centered"
)

# 部品を呼び出す（これだけであのアニメーションが出ます！）
components.display_hero_section()

# ヘッダー画像やタイトル
st.title("「コデワーク」について")
st.write("実践的なスキルを身につけ、エンジニアとしての自走力をプログラミングスクールです。")
st.info("現在、以下の3つのコースを提供しております。")

st.markdown("---")

# --- ナビゲーションセクション ---

# 1. 自走コース (Java)
st.subheader("🔰 コデワーク 自走コース (Java Webアプリ開発)")
st.write("Java言語の基礎からWebアプリケーション開発までを網羅したスタンダードなコースです。")
st.caption("対象: 初心者〜 / 期間: 6ヶ月")
# ページへのリンクボタン
st.page_link("pages/jisocors.py", label="自走コースの詳細・お申し込み", icon="☕")

st.markdown("---")

# 2. 自走コース SP (Spring Boot)
st.subheader("🍃 コデワーク 自走コース SP")
st.write("Javaフレームワーク「Spring Boot」を用いた、より実践的で効率的な開発手法を学びます。")
st.caption("対象: 基礎習得済みの方 / 期間: 3ヶ月")
st.page_link("pages/jisocorsSP.py", label="自走コースSPの詳細・お申し込み", icon="🚀")

st.markdown("---")

# 3. スパルタコース
st.subheader("🔥 スパルタコース(Java Webアプリ開発)")
st.write("「稼ぐ力」に特化。高単価案件の獲得を目指し、実案件レベルの課題に挑戦する特別コースです。")
st.caption("対象: 本気でキャリアを変えたい方 / 期間: 6ヶ月 / 案件保証あり")
st.page_link("pages/suparuta.py", label="スパルタコースの詳細・お申し込み", icon="⚔️")

st.markdown("---")

# 4. 大人のプログラミングクラブ
st.subheader("🧑 大人のプログラミングクラブ")
st.write("プログラミングを『ゆるく、長く、確実に』学ぶ大人の部活コースです。")
st.caption("対象: 『ゆるく、長く、確実に』プログラミングを学びたい方 / 期間: 24ヶ月")
st.page_link("pages/oldprogramclub.py", label="詳細・お申し込み", icon="⚔️")


st.markdown("---")

# 会社情報（TOPページにもあると信頼性が増します）
st.header("運営会社情報")

with st.expander("詳細を見る", expanded=True):
    st.write("合同会社 挑与本願")
    st.write("〒621-0834 京都府亀岡市篠町広田2丁目")
    st.write("担当：森 翔一")

st.markdown("---")

st.header("法務情報")
st.caption("法律に基づく表記はこちらをご確認ください。")
# ここでページへのリンクを作成
st.page_link("pages/tokusho.py", label="特定商取引法に基づく表記", icon="⚖️")