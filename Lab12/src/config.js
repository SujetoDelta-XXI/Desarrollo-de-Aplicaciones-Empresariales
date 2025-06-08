// src/config.js

const isProduction = import.meta.env.PROD;

export const API_BASE_URL = isProduction
  ? "https://cinepoli-api.onrender.com/api/"
  : "http://127.0.0.1:8000/api/";
