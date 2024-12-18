import { config } from 'dotenv';
import axios from 'axios';
config();

const API_URL = "https://127.0.0.1:8080/"
const api = axios.create({
    baseURL: process.env.API_URL || API_URL,
    headers: {
        'Content-Type': 'application/json',
    },
    withCredentials: true,
});

export default api;