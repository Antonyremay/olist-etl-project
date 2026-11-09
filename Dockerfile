# 1. Select the Python base image
FROM python:3.13-slim

# 2. Set the working directory
WORKDIR /app

# 3. Copy the dependency file
COPY requirements.txt .

# 4. Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copy the Python scripts
COPY python_scripts/ ./python_scripts/

# 6. Set the default execution command
CMD ["python", "python_scripts/load_data_to_mysql.py"]