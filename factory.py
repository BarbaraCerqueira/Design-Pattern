from abc import ABC, abstractmethod

# Interface comum para todos os documentos
class Document(ABC):
    @abstractmethod
    def create(self):
        pass

# Classes concretas de documentos
class WordDocument(Document):
    def create(self):
        return "Word document created."

class ExcelDocument(Document):
    def create(self):
        return "Excel document created."

class PDFDocument(Document):
    def create(self):
        return "PDF document created."

# Factory para criar documentos
class DocumentFactory:
    @staticmethod
    def get_document(doc_type: str) -> Document:
        if doc_type == 'word':
            return WordDocument()
        elif doc_type == 'excel':
            return ExcelDocument()
        elif doc_type == 'pdf':
            return PDFDocument()
        else:
            raise ValueError("Unknown document type.")

# Código cliente
if __name__ == "__main__":
    doc_type = 'pdf'
    document = DocumentFactory.get_document(doc_type)
    print(document.create())  # Output: PDF document created.

