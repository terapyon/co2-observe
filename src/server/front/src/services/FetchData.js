import axios from "axios";

const apiClient = axios.create({
    // baseURL: "http://localhost:5000",
    baseURL: "https://70vz4mfcki.execute-api.ap-northeast-1.amazonaws.com/dev",
    withCredentials: false,
    headers: {
        Accept: "application/json",
        "Content-Type": "application/json",
    },
});

export default {
    postFetch(data) {
        return apiClient.post("/fetch", { date: data });
    },
};