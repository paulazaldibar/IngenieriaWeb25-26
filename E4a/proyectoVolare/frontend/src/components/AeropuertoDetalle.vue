<script setup>
import { ref, onMounted } from "vue";
import { useRoute } from "vue-router";
import { getAeropuerto } from "../api/api.js";

const route = useRoute();
const aeropuerto = ref(null);
const cargando = ref(true);

onMounted(async () => {
  try {
    const id = route.params.id;
    const resp = await getAeropuerto(id);
    aeropuerto.value = resp.data;
  } catch (error) {
    console.error("Error cargando aeropuerto", error);
  } finally {
    cargando.value = false;
  }
});
</script>

<template>
  <div>
    <p v-if="cargando">Cargando aeropuerto...</p>

    <div v-else-if="aeropuerto">
      <h2>Aeropuerto: {{ aeropuerto.nombre }}</h2>

      <p><strong>Siglas:</strong> {{ aeropuerto.siglas }}</p>
      <p><strong>País:</strong> {{ aeropuerto.pais }}</p>

      <div v-if="aeropuerto.foto">
        <img :src="aeropuerto.foto" alt="Foto aeropuerto" style="max-width: 300px" />
      </div>
    </div>

    <p v-else>No se encontró el aeropuerto.</p>
  </div>
</template>
