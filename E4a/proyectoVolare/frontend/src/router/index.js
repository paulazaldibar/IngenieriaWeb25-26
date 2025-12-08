import { createRouter, createWebHistory } from "vue-router";
import AerolineasLista from "../components/AerolineasLista.vue";
import PaisesLista from "../components/PaisesLista.vue";
import AeropuertosLista from "../components/AeropuertosLista.vue";
import AerolineaDetalle from "../components/AerolineaDetalle.vue";
import PaisDetalle from "../components/PaisDetalle.vue";
import AeropuertoDetalle from "../components/AeropuertoDetalle.vue";

const routes = [
  {
    path: "/",
    redirect: "/aerolineas",
  },
  {
    path: "/aerolineas",
    name: "aerolineas",
    component: AerolineasLista,
  },
  {
    path: "/aerolineas/:id",
    name: "aerolinea-detalle",
    component: AerolineaDetalle,
  },
  {
    path: "/paises",
    name: "paises",
    component: PaisesLista,
  },
  {
    path: "/paises/:id",
    name: "pais-detalle",
    component: PaisDetalle,
  },
  {
    path: "/aeropuertos",
    name: "aeropuertos",
    component: AeropuertosLista,
  },
  {
    path: "/aeropuertos/:id",
    name: "aeropuerto-detalle",
    component: AeropuertoDetalle,
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
