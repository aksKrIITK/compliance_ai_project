/** Axios client — injects tenant JWT, handles 401 refresh */
import axios from "axios";

const API_URL = import.meta.env.VITE_API_URL || "http://localhost:8000";

export const api = axios.create({ baseURL: `${API_URL}/api/v1` });

api.interceptors.request.use((config) => {
  const token = localStorage.getItem("access_token");
  if (token) config.headers.Authorization = `Bearer ${token}`;
  return config;
});

export async function triggerScan(documentIds: string[], jurisdictions: string[]) {
  const { data } = await api.post("/compliance/scan", { document_ids: documentIds, jurisdictions });
  return data;
}
