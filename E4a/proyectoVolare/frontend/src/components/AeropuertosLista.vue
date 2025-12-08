<script setup>
import { ref, onMounted } from "vue";
import { getAeropuertos } from "../api/api.js";

const aeropuertos = ref([]);
const cargando = ref(true);

onMounted(async () => {
  try {
    const resp = await getAeropuertos();
    aeropuertos.value = resp.data;
  } catch (error) {
    console.error("Error cargando aeropuertos", error);
  } finally {
    cargando.value = false;
  }
});
</script>

<template>
  <div>
    <h2>Listado de Aeropuertos (API Django)</h2>
    <p v-if="cargando">Cargando...</p>

    <ul v-else>
      <li
        v-for="aer in aeropuertos"
        :key="aer.id_aeropuerto"
      >
        <router-link :to="`/aeropuertos/${aer.id_aeropuerto}`">
          {{ aer.nombre }} ({{ aer.siglas }})
        </router-link>
      </li>
    </ul>
  </div>
</template>
