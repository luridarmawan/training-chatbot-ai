from langchain.prompts import PromptTemplate

template = """
Berikut adalah tulisan dari laporan pendapatan bulanan:

{content}

buat jawaban dalam kalimat yang {length}.
"""

prompt = PromptTemplate.from_template( template)
message = prompt.format(content="isi kontent", length="panjang")
print(message)
