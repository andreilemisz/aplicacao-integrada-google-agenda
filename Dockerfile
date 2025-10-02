# Usar Python oficial
FROM python:3.11-slim

# Definir diretório de trabalho dentro do container
WORKDIR /aplicacao-andrei

# Definir Python path, porque uso uma pasta chamada code para organizar o código
ENV PYTHONPATH=/aplicacao-andrei

# Copiar arquivo de dependências
COPY requirements.txt .

# Instalar dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copiar TODO o conteúdo da pasta atual para o container
COPY . .

# Comando para rodar sua aplicação
CMD ["python", "aplicacao-andrei.py"]