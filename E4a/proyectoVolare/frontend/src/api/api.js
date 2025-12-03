import axios from "axios";

const API_URL = "http://localhost:8000/api";

export function getAerolineas() {
  return axios.get(`${API_URL}/aerolineas/`);
}
