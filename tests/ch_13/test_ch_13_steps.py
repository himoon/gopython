import sys
from pathlib import Path
from unittest.mock import MagicMock, patch
import pytest

CH_13_DIR = Path(__file__).parent.parent.parent / "ch_13"

@pytest.fixture(autouse=True)
def setup_module_path():
    """
    테스트 실행 전/후로 sys.path와 sys.modules를 초기화하는 픽스처입니다.
    다른 챕터의 동일한 이름의 파일(step_*)이 메모리에 남아있을 경우
    엉뚱한 파일이 import되는 모듈 충돌(ImportError 등)을 방지합니다.
    """
    sys.path.insert(0, str(CH_13_DIR))
    for key in list(sys.modules.keys()):
        if key.startswith("step_"):
            del sys.modules[key]
    yield
    if str(CH_13_DIR) in sys.path:
        sys.path.remove(str(CH_13_DIR))


def test_step_1_1_mkdir(tmp_path, monkeypatch):
    """step_1_1.py: 디렉토리 생성 테스트"""
    import step_1_1  # noqa: E402
    monkeypatch.setattr(step_1_1, "IN_DIR", tmp_path / "input")
    
    step_1_1.IN_DIR.mkdir(exist_ok=True)
    
    assert (tmp_path / "input").is_dir()


@patch("ollama.chat")
@patch("streamlit.chat_message")
@patch("streamlit.chat_input")
@patch("streamlit.markdown")
def test_step_2_1_streamlit_ollama(mock_markdown, mock_chat_input, mock_chat_message, mock_ollama_chat):
    """step_2_1.py: Streamlit과 Ollama 챗봇 통합 테스트"""
    import step_2_1  # noqa: E402
    
    import streamlit as st
    st.session_state.clear()
    
    mock_chat_input.return_value = "안녕"
    mock_ollama_chat.return_value = {"message": {"content": "안녕하세요!"}}
    
    import runpy
    with patch("streamlit.set_page_config"):
        runpy.run_module("step_2_1", run_name="__main__")
        
    mock_chat_input.assert_called_once()
    mock_ollama_chat.assert_called_once()


@patch("ollama.chat")
@patch("streamlit.form_submit_button")
@patch("step_3_1.extract_text_img")
def test_step_3_3_translator(mock_extract, mock_submit, mock_ollama, tmp_path, monkeypatch):
    """step_3_3.py: 기사 번역기 웹 앱 텍스트 추출 및 번역 테스트"""
    import step_1_1  # noqa: E402
    monkeypatch.setattr(step_1_1, "IN_DIR", tmp_path / "input")
    step_1_1.IN_DIR.mkdir(exist_ok=True)
    
    # system.txt 더미 생성
    system_txt = tmp_path / "input" / "system.txt"
    system_txt.write_text("번역 프롬프트", encoding="utf-8")
    
    import step_3_3  # noqa: E402
    
    import streamlit as st
    st.session_state.clear()
    
    mock_submit.return_value = True
    mock_extract.return_value = ("기사 본문", "http://example.com/img.jpg")
    mock_ollama.return_value = {"message": {"content": "Translated text"}}
    
    import runpy
    with patch("streamlit.set_page_config"), patch("streamlit.image"):
        runpy.run_module("step_3_3", run_name="__main__")
        
    mock_extract.assert_called_once()
    mock_ollama.assert_called_once()
