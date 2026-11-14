# API-client-NeighborOnionapp

**隔壁老洋｜FastAPI 後端 API**

本 Repository 是「隔壁老洋」農業資訊應用的 API 後端，提供栽植期提醒、預警報及預約資料的 REST API，使用 SQLite 儲存資料。

## 技術

- Python
- FastAPI
- Pydantic
- SQLAlchemy ORM
- SQLite
- Uvicorn
- Gunicorn

## 程式架構

| 檔案 | 職責 |
|---|---|
| `sql_app/main.py` | FastAPI app、CORS middleware、路由及 DB dependency |
| `sql_app/database.py` | SQLite engine、SessionLocal、declarative Base |
| `sql_app/models.py` | User、Room、Booking ORM models |
| `sql_app/schemas.py` | API 請求與回應 schema |
| `sql_app/crud.py` | 查詢、新增與預約衝突檢查 |

## API 路由

| Method | Endpoint | 用途 |
|---|---|---|
| GET | `/plant` | 取得栽植期提醒 |
| POST | `/plant` | 新增溫度與雨量提醒 |
| GET | `/aler` | 取得預警報 |
| POST | `/aler` | 新增預警報 |
| GET | `/bookings` | 取得預約紀錄 |
| POST | `/bookings` | 新增預約紀錄 |

GET 路由支援 `skip` 與 `limit` 參數。

## 資料表

- `users`：`p_id`、`temp`、`rain`。
- `rooms`：`a_id`、`aler`。
- `bookings`：`booking_id`、`p_id`、`a_id`、`booked_num`、`start_datetime`、`end_datetime`。

資料庫 URL 在程式中設定為 `sqlite:///./sql_app.db`。

## 管理端串接

[Api-Post-NeighborOnionapp](https://github.com/Kouichi1229/Api-Post-NeighborOnionapp) 使用 Streamlit 建立表單，透過 Requests 對 `/plant` 與 `/aler` 發送 POST JSON。

## 已知限制

- `crud.create_booking()` 建立 Booking ORM instance 時使用 `user_id`、`room_id`，但 model 欄位實際為 `p_id`、`a_id`；預約新增路徑存在欄位不一致問題。
- Booking 外鍵使用 `ondelete='SET NULL'`，但欄位同時設定 `nullable=False`。
- CORS allowlist 目前是 localhost origins。
- 管理端表單沒有呼叫 bookings API。
- 本文件依程式碼整理，未重新部署或進行端到端測試。

完整系統架構與技術回顧請參閱主專案：[NeighborOnionapp](https://github.com/Kouichi1229/NeighborOnionapp)。
