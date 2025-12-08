<script setup>
import { ref, onMounted } from "vue";
import { useRoute } from "vue-router";
import { getPais } from "../api/api.js";

const route = useRoute();
const pais = ref(null);
const cargando = ref(true);

onMounted(async () => {
  try {
    const id = route.params.id;
    const resp = await getPais(id);
    pais.value = resp.data;
  } catch (error) {
    console.error("Error cargando país", error);
  } finally {
    cargando.value = false;
  }
});
</script>

<template>
  <div>
    <p v-if="cargando">Cargando país...</p>

    <div v-else-if="pais">
      <h2>País: {{ pais.nombre }}</h2>

      <p><strong>Curiosidad:</strong> {{ pais.curiosidad }}</p>

      <div v-if="pais.bandera">
        <img :src="pais.bandera" alt="Bandera" style="max-width: 200px; margin-top: 10px" />
      </div>
    </div>

    <p v-else>No se encontró el país.</p>
  </div>
</template>
