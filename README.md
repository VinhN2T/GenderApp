# GenderApp
## Cài đặt
Cài đặt anaconda tại [đây](https://www.anaconda.com/download) 
> Note: Tick vào tùy chọn thêm vào biến môi trường Path

```bash
conda create --name myenv python=3.9
conda activate myenv
python -m venv venv
```

`Ctrl+Shift+P` chọn `Python: Select Interpreter` chọn môi trường venv

```bash
python -m pip install --upgrade pip
pip install dlib-19.22.99-cp39-cp39-win_amd64.whl
pip install -r requirements.txt
```

Cài thành công thì chạy lệnh

```bash
python main.py
```
