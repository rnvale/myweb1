import axios from "axios"

const http = axios.create({
    baseURL: import.meta.env.VITE_API_BASE_URL || "https://myweb-bwk2.onrender.com",
    timeout: 10000
})

export default http
