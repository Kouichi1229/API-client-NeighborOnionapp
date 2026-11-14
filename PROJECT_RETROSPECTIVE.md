# 技術回顧｜隔壁老洋 FastAPI 後端

## 專案定位

本 Repository 是「隔壁老洋」農業資訊應用的 FastAPI 後端，提供栽植期提醒、預警報及預約資料的 REST API，並以 SQLite 儲存資料。它與 Streamlit 管理端及整體系統文件屬於同一個專案脈絡，應合併閱讀，不應重複計算為多個獨立產品。

## 可由程式確認的技術

- Python
- FastAPI
- Pydantic request / response schemas
- SQLAlchemy ORM
- SQLite
- CORS middleware
- Uvicorn / Gunicorn deployment configuration（依 Procfile 與 runtime 設定）

## 程式結構

| 檔案 | 職責 |
|---|---|
| `sql_app/main.py` | FastAPI application、CORS、路由、DB dependency |
| `sql_app/database.py` | SQLite engine、SessionLocal、declarative Base |
| `sql_app/models.py` | User、Room、Booking ORM models |
| `sql_app/schemas.py` | Pydantic request / response models |
| `sql_app/crud.py` | ORM 查詢、新增及預約時段衝突檢查 |

## API 路由

- `GET /plant`、`POST /plant`：讀取與新增溫度／雨量提醒。
- `GET /aler`、`POST /aler`：讀取與新增預警報。
- `GET /bookings`、`POST /bookings`：讀取與新增預約資料。
- GET endpoints 支援 `skip` 與 `limit` 分頁參數。

## 資料模型與預約邏輯

程式建立 users、rooms、bookings 三個資料表。預約新增流程會先查詢相同 room 是否存在時間區間重疊，再決定是否新增；這段邏輯呈現了以資料庫查詢處理預約衝突的實作嘗試。

## 靜態檢視發現

1. `crud.create_booking()` 建立 Booking ORM instance 時傳入 `user_id`、`room_id`，但模型欄位實際為 `p_id`、`a_id`，預約新增流程存在欄位名稱不一致。
2. Booking 外鍵設定 `ondelete='SET NULL'`，但欄位同時設定 `nullable=False`，兩者的資料完整性語意不一致。
3. CORS allowlist 目前列出 localhost origins，沒有看到正式前端網域設定。
4. 管理端 Streamlit Repository 目前只呼叫 plant 與 aler endpoints，沒有串接 bookings。
5. Repository 追蹤了 SQLite 資料庫檔案 `sql_app.db`。依專案用途背景，這個資料庫應是供人工資料輸入流程使用的資料儲存檔，而非單純為測試而建立的空資料庫；但目前沒有檢視資料內容，因此無法確認實際紀錄的來源、真實性或是否包含個人資料。
6. Repository 追蹤多個 `__pycache__` 編譯檔，屬於可由原始碼重新產生的環境產物；本次僅記錄，沒有刪除原始檔案。

## 與其他 Repository 的關係

- `Api-Post-NeighborOnionapp`：Streamlit 管理端表單。
- `NeighborOnionapp`：整體系統與架構回顧。
- `projecttest010522`：較早期原型／資料擷取實驗。

## 驗證範圍

本回顧依目前原始碼與設定檔靜態整理。沒有重新部署舊服務、沒有連接歷史資料庫進行功能驗證，也沒有進行端到端測試；因此不宣稱目前 API 服務仍在線或所有路由均可正常運作。
