<script setup>
import { ref, onMounted } from "vue";
import { getAerolineas } from "../api/api.js";

const aerolineas = ref([]);
const cargando = ref(true);

onMounted(async () => {
  try {
    const resp = await getAerolineas();
    aerolineas.value = resp.data;
  } catch (error) {
    console.error("Error cargando aerolíneas", error);
  } finally {
    cargando.value = false;
  }
});
</script>

<template>
  <div>
    <h2>Listado de Aerolíneas (API Django)</h2>
    <p v-if="cargando">Cargando...</p>
    <ul v-else>
      <li v-for="aero in aerolineas" :key="aero.id_aerolinea">
        {{ aero.nombre }} ({{ aero.siglas }})
      </li>
    </ul>
  </div>
</template>
