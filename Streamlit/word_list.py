import streamlit as st
import pandas as pd

st.title("My Word List (Local Management Mode)")
st.caption("データはサーバーに保存されません。開始時にCSVを読み込み、終了時に保存してください。")

# --- セッション状態の初期化 ---
if "word_list" not in st.session_state:
    st.session_state.word_list = []

# --- 1. ファイルの読み込み (Upload) ---
st.sidebar.header("データ読み込み")
uploaded_file = st.sidebar.file_uploader("手元のCSVを選択してください", type="csv")

if uploaded_file is not None:
    # アップロードされた時だけセッション状態を上書き
    if st.sidebar.button("このファイルを読み込む"):
        df_uploaded = pd.read_csv(uploaded_file)
        st.session_state.word_list = df_uploaded.to_dict("records")
        st.sidebar.success("読み込み完了！")

# --- 2. 新規登録 (Form) ---
with st.form("word_input", clear_on_submit=True):
    col1, col2 = st.columns(2)
    with col1:
        english = st.text_input("英語 (English)")
    with col2:
        japanese = st.text_input("日本語 (Japanese)")

    submit = st.form_submit_button("リストに追加")

if submit:
    if english and japanese:
        st.session_state.word_list.append({"英語": english, "日本語": japanese})
        st.success(f"「{english}」を追加しました。")
    else:
        st.warning("両方の項目を入力してください。")

# --- 3. データの表示と管理 ---
st.subheader("現在のリスト")

if st.session_state.word_list:
    df = pd.DataFrame(st.session_state.word_list)
    st.table(df)

    # --- 4. データの保存 (Download) ---
    st.divider()
    st.subheader("データの保存")

    # DataFrameをCSV（バイナリ）に変換
    csv_data = df.to_csv(index=False, encoding="utf-8-sig").encode("utf-8-sig")

    st.download_button(
        label="編集したリストをCSVで保存",
        data=csv_data,
        file_name="my_word_list.csv",
        mime="text/csv",
        help="このボタンを押すと、あなたのブラウザ経由でPCに保存されます。"
    )

    if st.button("画面上のリストを全削除"):
        st.session_state.word_list = []
        st.rerun()
else:
    st.info("データがありません。手元のCSVをアップロードするか、新しく入力してください。")