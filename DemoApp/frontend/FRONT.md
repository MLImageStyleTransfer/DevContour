# Demo React microfront

### Architecture

```
.
├── FRONT.md
├── package-lock.json
├── package.json
├── public
│   ├── favicon.ico
│   ├── index.html
│   ├── logo192.png
│   ├── logo512.png
│   ├── manifest.json
│   └── robots.txt
├── src
│   ├── api
│   │   ├── api.ts
│   │   ├── config.ts
│   │   ├── constants.ts
│   │   └── types.ts
│   ├── common
│   │   └── helpers
│   │       ├── URLToBase64.ts
│   │       ├── base64ToURL.ts
│   │       └── createBlob.ts
│   ├── components
│   │   ├── content-box
│   │   │   ├── content-box.module.css
│   │   │   └── content-box.tsx
│   │   └── load-box
│   │       ├── load-box.css
│   │       └── load-box.tsx
│   ├── general
│   │   ├── App.css
│   │   └── App.tsx
│   ├── index.css
│   ├── index.tsx
│   ├── react-app-env.d.ts
│   ├── reportWebVitals.ts
│   └── setupTests.ts
└── tsconfig.json
```

### Setup

1. Установка необходимого ПО
    ```
    $sudo apt install nodejs
    ```

2. Настройка проекта
    ```
    $npm install
    ```

### Run server

1. Создать файл `.env` в корне проекта и указать в нем PORT:
    ```
    PORT=3000
    ```

2. Запустить работу сервера
    ```
    $npm run start
    ```

### WIP: Config
`.env` - Config file (auto)