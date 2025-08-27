# swagger-static

將 FastAPI 產生的 openapi.json 放在此資料夾，搭配 index.html 可在 GitHub Pages 上瀏覽 Swagger UI。

- index.html 會自動載入同目錄下的 openapi.json
- openapi.json 可用 curl 下載：

```sh
curl http://127.0.0.1:8000/openapi.json -o openapi.json
```

然後 push 到 gh-pages 分支即可。
