import axios from "axios";

const API_URL = "http://localhost:8000/api";

export function getAerolineas() {
  return axios.get(`${API_URL}/aerolineas/`);
}

export function getAerolinea(id) {
  return axios.get(`${API_URL}/aerolineas/${id}/`);
}

export function getPaises() {
  return axios.get(`${API_URL}/paises/`);
}

export function getPais(id) {
  return axios.get(`${API_URL}/paises/${id}/`);
}

export function getAeropuertos() {
  return axios.get(`${API_URL}/aeropuertos/`);
}

export function getAeropuerto(id) {
  return axios.get(`${API_URL}/aeropuertos/${id}/`);
}
