import streamlit as st
import os
import base64

def display_hero_section():
    """
    トップページ等のヒーローセクション（企業理念アニメーション）を表示する関数
    """
    
    # --- 画像をBase64に変換する関数（内部用） ---
    def get_image_base64(path):
        if not os.path.exists(path):
            return ""
        with open(path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()

    # 画像パス（TOP.pyと同じ階層の image フォルダを見る想定）
    # ※ページによって読み込み位置がずれないよう、絶対パスに近い処理をしています
    image_path = "image/挑与本願_logo.png" 
    
    # もし画像が見つからない場合の安全策（デバッグ用）
    if not os.path.exists(image_path):
        # カレントディレクトリからの相対パスで再トライ（pagesフォルダ対策）
        image_path = "../image/挑与本願_logo.png"

    img_base64 = get_image_base64(image_path)

    # --- CSSとHTML ---
    st.markdown(f"""
    <style>
        /* 全体のコンテナ */
        .hero-container {{
            text-align: center;
            margin-bottom: 50px;
            max-width: 800px;
            margin-left: auto;
            margin-right: auto;
        }}

        /* 線の共通スタイル */
        .line {{
            height: 2px;
            background-color: #333;
            margin: 15px 0;
            transform: scaleX(0);
        }}

        /* 上の線：左から */
        .line-top {{
            transform-origin: left;
            animation: lineGrow 1.5s ease forwards;
        }}

        /* 下の線：右から */
        .line-bottom {{
            transform-origin: right;
            animation: lineGrow 1.5s ease forwards;
        }}

        /* キャッチコピー */
        .catch-copy {{
            font-size: 2.5em;
            font-weight: bold;
            color: #333;
            opacity: 0;
            animation: fadeInDown 1.5s ease forwards;
        }}

        /* ロゴと説明文の枠 */
        .content-box {{
            display: flex;
            justify-content: center;
            align-items: center;
            gap: 20px;
            margin-top: 40px;
            opacity: 0;
            animation: fadeIn 2s ease 1.5s forwards;
            border: 2px solid #333;
            padding: 20px;
            border-radius: 10px;
        }}

        /* ロゴ画像のスタイル */
        .logo-img {{
            width: 250px;
            height: auto;
            object-fit: contain;
        }}

        .description-text {{
            text-align: left;
            font-size: 1.6em;
            color: #555;
            line-height: 1.6;
        }}

        /* アニメーション定義 */
        @keyframes lineGrow {{
            0% {{ transform: scaleX(0); }}
            100% {{ transform: scaleX(1); }}
        }}
        @keyframes fadeInDown {{
            0% {{ opacity: 0; transform: translateY(-20px); }}
            100% {{ opacity: 1; transform: translateY(0); }}
        }}
        @keyframes fadeIn {{
            0% {{ opacity: 0; }}
            100% {{ opacity: 1; }}
        }}
    </style>

    <div class="hero-container">
    <div class="line line-top"></div>
        
    <div class="catch-copy">
    挑み与えて、本願を成す
    </div>
        
    <div class="line line-bottom"></div>
    <div class="content-box">
    <img src="data:image/png;base64,{img_base64}" class="logo-img">
    <div class="description-text">
    <b>合同会社 挑与本願</b><br><br>
    <p>「挑戦」を「価値」に変え、<br>「共に願いを形」にする<br><b>IT職人集団です。</b></p>
    </div>
    </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")