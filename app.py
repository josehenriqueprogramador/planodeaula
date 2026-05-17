import streamlit as st
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.pagesizes import A4
from reportlab.lib.enums import TA_CENTER
import os

def gerar_pdf(dados):
    diretorio_atual = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(diretorio_atual, "plano_aula_ilan.pdf")
    doc = SimpleDocTemplate(file_path, pagesize=A4)
    styles = getSampleStyleSheet()
    style_title = ParagraphStyle('IlanTitle', parent=styles['Title'], alignment=TA_CENTER, fontSize=16, spaceAfter=20)
    elementos = [Paragraph("PLANO DE AULA - ILAN CHURCH", style_title), Spacer(1, 12)]
    for chave, valor in dados.items():
        if valor:
            v_fmt = str(valor).replace('\n', '<br/>')
            elementos.append(Paragraph(f"<b>{chave.upper()}:</b> {v_fmt}", styles['Normal']))
            elementos.append(Spacer(1, 12))
    doc.build(elementos)
    return file_path

st.set_page_config(page_title="Gerador Ilan Church", layout="centered")
st.title("⛪ Gerador de Plano de Aula CLIC")
st.subheader("Ilan Church - Modelo Oficial")

col1, col2 = st.columns(2)
with col1:
    professor = st.text_input("Professor(a)")
    curso = st.text_input("Curso")
with col2:
    data_aula = st.text_input("Data (DD/MM/AAAA)")
    encontro = st.text_input("Encontro")

tema = st.text_input("Tema da Aula")
referencia = st.text_input("Referência Bíblica")
st.divider()

st.header("1. Introdução")
objetivo = st.text_area("Objetivo da Aula")
motivacao = st.text_area("Motivação")
orientacao = st.text_area("Orientação (Roteiro)")

st.header("2. Desenvolvimento")
pontos = st.text_area("Pontos de Desenvolvimento")

st.header("3. Conclusão")
resumo = st.text_area("Resumo")
remotivacao = st.text_area("Remotivação")
encerramento = st.text_area("Encerramento (Versículo)")

if st.button("📄 Gerar Plano de Aula"):
    dados_plano = {
        "Professor": professor, "Data": data_aula, 
        "Curso/Encontro": f"{curso} - {encontro}",
        "Tema": tema, "Referência": referencia,
        "Objetivo": objetivo, "Motivação": motivacao,
        "Orientação": orientacao, "Desenvolvimento": pontos,
        "Resumo": resumo, "Remotivação": remotivacao,
        "Encerramento": encerramento
    }
    path = gerar_pdf(dados_plano)
    with open(path, "rb") as f:
        st.download_button("📥 Baixar PDF", f, file_name="plano_aula.pdf", mime="application/pdf")
    st.success("Sucesso!")
