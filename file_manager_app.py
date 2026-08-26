"""
📁 File Handler Pro — A Streamlit UI for file CRUD operations
Create, Read, Update, and Delete files right from your browser.
"""

import streamlit as st
from pathlib import Path
import datetime

# ----------------------------- PAGE CONFIG -----------------------------
st.set_page_config(
    page_title="File Handler Pro",
    page_icon=":page_facing_up:",
    layout="centered",
    initial_sidebar_state="expanded",
)

# ----------------------------- CUSTOM CSS -----------------------------
st.markdown("""
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500;600&display=swap" rel="stylesheet">
<style>
    html, body, [class*="css"] {
        font-family: 'Inter', -apple-system, sans-serif;
    }

    /* ---- Header ---- */
    .eyebrow {
        font-family: 'JetBrains Mono', monospace;
        font-size: 0.72rem;
        font-weight: 500;
        letter-spacing: 0.12em;
        text-transform: uppercase;
        color: #4F46E5;
        margin-bottom: 0.35rem;
    }
    .main-title {
        font-size: 2.1rem;
        font-weight: 700;
        color: #111827;
        letter-spacing: -0.02em;
        margin-bottom: 0.3rem;
    }
    .sub-title {
        color: #6B7280;
        font-size: 0.95rem;
        margin-bottom: 1.25rem;
    }
    .header-rule {
        border: none;
        border-top: 1px solid #E5E7EB;
        margin: 0 0 1.75rem 0;
    }

    /* ---- Buttons ---- */
    .stButton>button {
        border-radius: 6px;
        font-weight: 600;
        font-size: 0.9rem;
        padding: 0.5rem 1.1rem;
        border: 1px solid transparent;
        transition: all 0.15s ease;
    }
    .stButton>button[kind="primary"] {
        background-color: #4F46E5;
        border-color: #4F46E5;
    }
    .stButton>button[kind="primary"]:hover {
        background-color: #4338CA;
        border-color: #4338CA;
    }
    .stButton>button:not([kind="primary"]) {
        background-color: #FFFFFF;
        color: #374151;
        border-color: #D1D5DB;
    }
    .stButton>button:not([kind="primary"]):hover {
        border-color: #9CA3AF;
        color: #111827;
    }

    /* ---- Tabs ---- */
    .stTabs [data-baseweb="tab-list"] {
        gap: 4px;
        border-bottom: 1px solid #E5E7EB;
    }
    .stTabs [data-baseweb="tab"] {
        font-weight: 500;
        color: #6B7280;
        padding: 0.5rem 1rem;
    }
    .stTabs [aria-selected="true"] {
        color: #4F46E5 !important;
        font-weight: 600;
    }

    /* ---- Content box (Read tab) ---- */
    .file-box {
        background-color: #F9FAFB;
        border: 1px solid #E5E7EB;
        border-radius: 8px;
        padding: 0.25rem 1rem;
        margin-top: 0.75rem;
    }

    /* ---- Sidebar file cards ---- */
    .sidebar-title {
        font-weight: 600;
        font-size: 0.95rem;
        color: #111827;
        margin-bottom: 0.6rem;
    }
    .file-card {
        background-color: #FFFFFF;
        border: 1px solid #E5E7EB;
        border-radius: 6px;
        padding: 0.55rem 0.75rem;
        margin-bottom: 0.5rem;
    }
    .file-card .fname {
        font-family: 'JetBrains Mono', monospace;
        font-size: 0.82rem;
        font-weight: 500;
        color: #1F2937;
        word-break: break-all;
    }
    .file-card .fmeta {
        font-size: 0.74rem;
        color: #9CA3AF;
        margin-top: 0.15rem;
    }
    .empty-note {
        font-size: 0.85rem;
        color: #9CA3AF;
        font-style: italic;
    }

    footer {visibility: hidden;}
    #MainMenu {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# ----------------------------- WORKSPACE -----------------------------
# All files are managed inside this sandboxed folder so the app stays safe & tidy
WORKSPACE = Path("workspace_files")
WORKSPACE.mkdir(exist_ok=True)

# ----------------------------- HEADER -----------------------------
st.markdown('<p class="eyebrow">Python · Streamlit</p>', unsafe_allow_html=True)
st.markdown('<p class="main-title">File Handler Pro</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-title">A lightweight interface for creating, reading, updating, and deleting files.</p>', unsafe_allow_html=True)
st.markdown('<hr class="header-rule">', unsafe_allow_html=True)

# ----------------------------- SIDEBAR: FILE EXPLORER -----------------------------
with st.sidebar:
    st.markdown('<p class="sidebar-title">Workspace Files</p>', unsafe_allow_html=True)
    search_term = st.text_input("Search files", placeholder="Filter by name...", key="sidebar_search", label_visibility="collapsed")

    all_files = sorted([f for f in WORKSPACE.iterdir() if f.is_file()])
    files = [f for f in all_files if search_term.lower() in f.name.lower()] if search_term else all_files

    st.markdown("<div style='margin-top: 0.75rem;'></div>", unsafe_allow_html=True)

    if files:
        for f in files:
            size_kb = f.stat().st_size / 1024
            modified = datetime.datetime.fromtimestamp(f.stat().st_mtime).strftime("%d %b, %H:%M")
            st.markdown(
                f"""<div class="file-card">
                    <div class="fname">{f.name}</div>
                    <div class="fmeta">{size_kb:.1f} KB &nbsp;·&nbsp; {modified}</div>
                </div>""",
                unsafe_allow_html=True,
            )
    elif all_files and search_term:
        st.markdown(f'<p class="empty-note">No files match "{search_term}".</p>', unsafe_allow_html=True)
    else:
        st.markdown('<p class="empty-note">No files yet. Create one to get started.</p>', unsafe_allow_html=True)

    st.divider()
    st.caption("Built with ❤️ using Python & Streamlit")

# ----------------------------- TABS -----------------------------
tab_create, tab_read, tab_update, tab_delete = st.tabs(
    ["Create", "Read", "Update", "Delete"]
)

# ----------------------------- CREATE -----------------------------
with tab_create:
    st.subheader("Create a New File")
    name = st.text_input("File name", placeholder="e.g. notes.txt", key="create_name")
    content = st.text_area("File content", placeholder="Type something...", key="create_content", height=150)

    if st.button("Create File", type="primary", key="create_btn"):
        if not name.strip():
            st.warning("Please enter a file name.")
        else:
            path = WORKSPACE / name
            if path.exists():
                st.error(f"A file named **{name}** already exists.")
            else:
                try:
                    path.write_text(content)
                    st.success(f"File **{name}** created successfully.")
                except Exception as err:
                    st.error(f"An error occurred: {err}")

# ----------------------------- READ -----------------------------
with tab_read:
    st.subheader("Read a File")
    files = sorted([f.name for f in WORKSPACE.iterdir() if f.is_file()])

    if not files:
        st.info("No files available yet. Create one first!")
    else:
        selected = st.selectbox("Choose a file to view", files, key="read_select")
        if st.button("Read File", key="read_btn"):
            path = WORKSPACE / selected
            try:
                text = path.read_text()
                st.markdown('<div class="file-box">', unsafe_allow_html=True)
                st.code(text if text.strip() else "(This file is empty)", language="text")
                st.markdown('</div>', unsafe_allow_html=True)
                st.download_button(
                    label="Download this file",
                    data=text,
                    file_name=selected,
                    mime="text/plain",
                    key="download_btn",
                )
            except Exception as err:
                st.error(f"An error occurred: {err}")

# ----------------------------- UPDATE -----------------------------
with tab_update:
    st.subheader("Update a File")
    files = sorted([f.name for f in WORKSPACE.iterdir() if f.is_file()])

    if not files:
        st.info("No files available yet. Create one first!")
    else:
        selected = st.selectbox("Choose a file to update", files, key="update_select")
        operation = st.radio(
            "What would you like to do?",
            ["Rename", "Append content", "Overwrite content"],
            horizontal=True,
            key="update_op",
        )
        path = WORKSPACE / selected

        if operation == "Rename":
            new_name = st.text_input("New file name", key="rename_input")
            if st.button("Rename", type="primary", key="rename_btn"):
                new_path = WORKSPACE / new_name
                if not new_name.strip():
                    st.warning("Please enter a new file name.")
                elif new_path.exists():
                    st.error(f"A file named **{new_name}** already exists.")
                else:
                    try:
                        path.rename(new_path)
                        st.success(f"Renamed to **{new_name}** successfully.")
                    except Exception as err:
                        st.error(f"An error occurred: {err}")

        elif operation == "Append content":
            extra = st.text_area("Content to append", key="append_input", height=100)
            if st.button("Append", type="primary", key="append_btn"):
                try:
                    with open(path, "a") as fs:
                        fs.write("\n" + extra)
                    st.success(f"Content appended to **{selected}**.")
                except Exception as err:
                    st.error(f"An error occurred: {err}")

        else:  # Overwrite
            new_content = st.text_area("New content (replaces everything)", key="overwrite_input", height=150)
            if st.button("Overwrite", type="primary", key="overwrite_btn"):
                try:
                    path.write_text(new_content)
                    st.success(f"**{selected}** overwritten successfully.")
                except Exception as err:
                    st.error(f"An error occurred: {err}")

# ----------------------------- DELETE -----------------------------
with tab_delete:
    st.subheader("Delete a File")
    files = sorted([f.name for f in WORKSPACE.iterdir() if f.is_file()])

    if not files:
        st.info("No files available yet. Nothing to delete.")
    else:
        selected = st.selectbox("Choose a file to delete", files, key="delete_select")
        st.warning("This action is irreversible.")
        confirm = st.checkbox(f"I confirm I want to permanently delete '{selected}'", key="delete_confirm")

        if st.button("Delete File", type="primary", key="delete_btn", disabled=not confirm):
            try:
                (WORKSPACE / selected).unlink()
                st.success(f"**{selected}** deleted successfully.")
                st.rerun()
            except Exception as err:
                st.error(f"An error occurred: {err}")
