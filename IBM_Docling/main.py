import time
from docling.document_converter import DocumentConverter  #pip install docling

#Convert từ table về markdown -> Cho RAG học
#Thử các source
# source = "https://assets.accessible-digital-documents.com/uploads/2017/01/sample-tables.pdf"  # The Docling technical paper itself
source = "https://www.w3.org/WAI/WCAG20/Techniques/working-examples/PDF20/table.pdf"
# source = "https://drive.google.com/file/d/1cswCefI5i-mf8qpv_NjLov5niYmkt3I-/view?usp=sharing&a=1"

converter = DocumentConverter()

#Đo thời gian chạy

start_time = time.time()
result = converter.convert(source=source)
end_time = time.time()


#In ra kết quả
print(result.document.export_to_markdown())
print(f"Thời gian chạy: {end_time - start_time:.2f} giây")