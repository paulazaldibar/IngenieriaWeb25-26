<script setup>
import { ref, onMounted } from "vue";
import { useRoute } from "vue-router";
import { getAerolinea } from "../api/api.js";

const route = useRoute();
const aerolinea = ref(null);
const cargando = ref(true);

onMounted(async () => {
  try {
    const id = route.params.id;
    const resp = await getAerolinea(id);
    aerolinea.value = resp.data;
  } catch (error) {
    console.error("Error cargando aerolínea", error);
  } finally {
    cargando.value = false;
  }
});
</script>

<template>
  <div>
    <p v-if="cargando">Cargando aerolínea...</p>

    <div v-else-if="aerolinea">
      <h2>Detalle Aerolínea: {{ aerolinea.nombre }}</h2>

      <p><strong>Siglas:</strong> {{ aerolinea.siglas }}</p>
      <p><strong>Descripción:</strong> {{ aerolinea.descripcion }}</p>
      <p><strong>País de origen:</strong> {{ aerolinea.pais_origen }}</p>

      <div v-if="aerolinea.logo">
        <img :src="aerolinea.logo" alt="Logo aerolínea" style="max-width: 200px" />
      </div>
    </div>

    <p v-else>No se encontró la aerolínea.</p>
  </div>
</template>
