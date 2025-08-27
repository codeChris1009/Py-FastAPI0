# AdvImplement

一個用 FastAPI 製作的書籍管理 RESTful API 專案，支援書籍的新增、查詢、修改、刪除，並可批次匯入、查詢作者/書名/ISBN，並有 mock 資料可供測試。

## 目錄結構

```
AdvImplement/
├── main.py                # FastAPI 主程式
├── requirements.txt       # Python 套件需求
├── forMockBooks.json      # 測試用書籍資料
├── .gitignore             # Git 忽略清單
```

## 安裝步驟

1. **安裝 Python 3.8+**
2. **建立虛擬環境（建議）**
   ```sh
   python3 -m venv .venv
   source .venv/bin/activate
   ```
3. **安裝必要套件**
   ```sh
   pip install -r requirements.txt
   ```

## 啟動 API 伺服器

```sh
uvicorn main:app --reload
```

伺服器啟動後，預設在 http://127.0.0.1:8000

- Swagger UI 文件: http://127.0.0.1:8000/docs
- Redoc 文件: http://127.0.0.1:8000/redoc

## API 主要功能

- `GET    /` ：歡迎訊息
- `POST   /bookshelf` ：新增一本書
- `POST   /bookshelf/bulk` ：批次新增多本書
- `GET    /bookshelf` ：取得所有書籍
- `GET    /bookshelf/{isbn}` ：用 ISBN 查詢書籍
- `GET    /bookshelf/title/{title}`：用書名查詢
- `GET    /bookshelf/author/{author}`：用作者查詢
- `PUT    /bookshelf/{book_id}` ：用 UUID 完全更新書籍
- `PUT    /bookshelf/isbn/{isbn}` ：用 ISBN 完全更新書籍
- `PATCH  /bookshelf/title/{title}`：用書名部分更新
- `DELETE /bookshelf/{book_id}` ：刪除書籍

## 書籍資料格式（Book Model）

```python
class Book(BaseModel):
    id: Optional[UUID]
    isbn: str
    author: Optional[str]
    title: Optional[str]
    lang: str
    isRead: bool = False
    reflection: Optional[Reflection]

class Reflection(BaseModel):
    rate_star: Optional[int] = 1
    desc: Optional[str] = None
```

## 匯入 mock 資料

可用 `forMockBooks.json` 內的資料，透過 `/bookshelf/bulk` API 批次匯入：

```sh
curl -X POST "http://127.0.0.1:8000/bookshelf/bulk" \
     -H "Content-Type: application/json" \
     -d @forMockBooks.json
```

## 測試

可用 Swagger UI 進行 API 測試，或用 curl/Postman。

---

如有問題請開 issue 或聯絡作者。
